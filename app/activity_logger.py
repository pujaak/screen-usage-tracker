#  logs data to CSV
import csv
from datetime import datetime

def log_usage(app_name, window_title, active_time):
    with open("usage_log.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            app_name,
            window_title,
            f"{active_time} min"
        ])
        
       


# testing
# log_usage("chrome", "youtube", 60)
# # Print the contents of the CSV file
# with open("usage_log.csv", "r", encoding="utf-8") as f:
#     print(f.read())
# --------