<!-- project overview and usage -->
# 🖥️ Screen Usage Tracker
A CLI application that tracks your active screen time, desktop apps, and websites (via browser tab titles). Useful for productivity tracking, or building time-management habits.

<img width="661" alt="1screen usage total active time in minutes" src="https://github.com/user-attachments/assets/08663c97-7f3f-4be8-aa00-e92b30fb8b40" />


## Features
- Tracks active desktop applications
- Infers website usage via browser window titles
- Logs app + website usage to a timestamped CSV
- Detects idle time

## Quick Start
### Step 1. Clone the Repository

```bash
git clone https://github.com/pujaak/screen-usage-tracker.git
cd screen-usage-tracker
```



### Step 2. Create a virtual environment
- Windows:
```bash
python -m venv venv
```
- MacOS:
```bash
python3 -m venv env
```

### Step 3. Activate the virtual environment
- Windows:
```bash
.\venv\Scripts\activate 
```
- git bash: 
```bash
source venv/Scripts/activate
```
- MacOS:
```bash
source env/bin/activate
```


### Step 4. Install the Required Libraries
```bash
pip install -r requirements.txt
```

### Step 5. Run the project:

```bash
python main.py
```
---
## To Use the Project:
Once you have done all the [Quick Start](#quick-start) steps. Then you can start using the application anytime you want to, just by following the three steps, given below:
### Step 1. Go to the project folder and open terminal
### Step 2. Activate the virtual environment
- Windows:
```bash
.\venv\Scripts\activate 
```
- git bash: 
```bash
source venv/Scripts/activate
```
- MacOS:
```bash
source env/bin/activate
```
### Step 3. Run the project 
```bash
python main.py
```
---


#### usage_log.csv Output:
![image](https://github.com/user-attachments/assets/4b42ba1d-9bba-475a-a544-5bbd6a326f64)


