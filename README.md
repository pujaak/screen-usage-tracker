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

---
### Expected Outputs:
<img width="715" alt="1screen usage log" src="https://github.com/user-attachments/assets/e0b96e36-14bb-4346-a505-cbc3faeb723e" />

<img width="564" alt="3screen usage log - the except block code" src="https://github.com/user-attachments/assets/334a254a-92d9-482b-9997-453969f09fd2" />

<img width="555" alt="2screen usage log" src="https://github.com/user-attachments/assets/d19204df-316d-4308-8964-7c0a6a7cfd9f" />

#### usage_log.csv Output:
<img width="836" alt="usage_log-csv" src="https://github.com/user-attachments/assets/60e2a036-a7f0-475d-87b2-8c4e1e664c4c" />
