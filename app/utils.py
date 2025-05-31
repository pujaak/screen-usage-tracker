# window/app helpers
import win32gui
import win32process
import psutil
def get_active_window_title():
    try:
        window = win32gui.GetForegroundWindow() # Returns the handle (unique ID) of the currently active window.
        return win32gui.GetWindowText(window)
    except: 
        return "Unknown Window"
    

def get_active_app_name():
    try:
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd) # Given a window handle, returns the thread ID and process ID associated with that window.
        return psutil.Process(pid).name() # Given a process ID, returns the name of the process (e.g., "chrome.exe")
    except:
        return "Unknown App"

#----test code: 
# # 1. Get the active window handle
# hwnd = win32gui.GetForegroundWindow()
# print(f"Window handle: {hwnd}")
# # 2. Get the process ID from the window handle
# _, pid = win32process.GetWindowThreadProcessId(hwnd)
# print(f"Process ID: {pid}")
# print(f"Process _: {_}")
# # 3. Get the process name from the PID
# pname = psutil.Process(pid).name()
# print(f"Process name: {pname}")
# ------