#  main tracking logic - tracks which app and window are active, and logs usage if the user is not idle.
import time
from pynput import keyboard, mouse
from .config import IDLE_TIME_LIMIT, TRACK_INTERVAL, LOG_INTERVAL
from .utils import get_active_app_name, get_active_window_title
from .activity_logger import log_usage

last_input_time = time.time() # Stores the last time the user interacted with keyboard or mouse.

def on_input(event): # Updates last_input_time whenever any input is detected.
    global last_input_time
    last_input_time = time.time()
    


def start_tracking():
    global last_input_time
    # Starts listeners for keyboard and mouse input.
    keyboard.Listener(on_press=on_input).start()
    mouse.Listener(on_move=on_input, on_click=on_input, on_scroll=on_input).start()

    print("🟢 Tracking Started. Press Ctrl+C to stop.")

    # Initializes tracking variables.
    last_app = None
    last_window = None
    activity_duration = 0
    total_active_time = 0  # in seconds

    try:
        while True:
            now = time.time()
            is_active = (now - last_input_time) < IDLE_TIME_LIMIT

            if is_active:
                app = get_active_app_name()
                window = get_active_window_title()

                # # test code to monitor active apps:
                # # Print app, window, and time every 10 seconds
                # if int(now) % 10 == 0:
                #     print(f"[{time.strftime('%H:%M:%S')}] Current app: {app}, window: {window}")
                #     time.sleep(1)  # Prevents multiple prints within the same second
                #     print(f"[{time.strftime('%H:%M:%S')}] Current app: {app}, window: {window}")
                # ------

                if app == last_app and window == last_window:
                    activity_duration += TRACK_INTERVAL
                else: 
                    if activity_duration >= LOG_INTERVAL:
                        log_usage(last_app, last_window, round(activity_duration / 60, 2)) #convert activity_duration from seconds to minute
                        total_active_time += activity_duration  # accumulate
                        print(f"📥 Logged: {last_app}, {last_window}, {round(activity_duration / 60, 2)} min")

                    last_app = app
                    last_window = window
                    activity_duration = TRACK_INTERVAL
            
            else:
                if activity_duration >= LOG_INTERVAL:
                    log_usage(last_app, last_window, round(activity_duration / 60, 2)) #convert activity_duration from seconds to minute
                    total_active_time += activity_duration  # accumulate
                    print(f"⏸️ Idle detected. Logged: {last_app}, {last_window}, {round(activity_duration / 60, 2)} min")

                last_app = None
                last_window = None
                activity_duration = 0

            time.sleep(TRACK_INTERVAL)


    except KeyboardInterrupt:
        print("\n🛑 Tracking stopped. ")
        if activity_duration >= LOG_INTERVAL:
            log_usage(last_app, last_window, round(activity_duration / 60, 2)) #convert activity_duration from seconds to minute
            # total activity duration
            total_active_time += activity_duration  # accumulate
            print(f"✅ Final log saved: {last_app}, {last_window}, {round(activity_duration / 60, 2)} min")
        print(f"🟡 TOTAL ACTIVE SCREEN TIME: {round(total_active_time / 60, 2)} min")
        # to log total active screen time in usage_log.csv in minutes
        log_usage("TOTAL ACTIVE SCREEN TIME: ", "", round(total_active_time / 60, 2))

# # to test tracker.py code: 
# start_tracking()