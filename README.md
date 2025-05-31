<!-- project overview and usage -->
# 🖥️ Screen Usage Tracker

Tracks your active screen time, desktop apps, and websites (via browser tab titles). Useful for productivity tracking, or building time-management habits.

## Features
- Tracks active desktop applications
- Infers website usage via browser window titles
- Logs app + website usage to a timestamped CSV
- Detects idle time
- Customizable idle timeout and log interval


## Project Setup
### Clone the Repository

```bash
git clone https://github.com/pujaak/screen-usage-tracker.git
cd screen-usage-tracker
```



### Set Up Virtual Environment
1. Create a virtual environment
```bash
python -m venv venv
```
2. Activate the virtual environment
Windows:
```bash
.\venv\Scripts\activate 
```
or (if above doesn't work)
```bash
source venv/Scripts/activate
```

### Install Required Libraries
```bash
pip install -r requirements.txt
```
---
### Run the project:
```bash
python main.py
```
