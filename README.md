<div align="center">

<h1>ScatterSense </h1>

</div>

A simple productivity tracking dashboard where you can log your work sessions and see when you are actually getting things done. Built to help spot patterns in your workflow—like figuring out if you are actually productive at 2 AM or if you should just go to sleep.

**[Check out the live app here](https://scattersense.onrender.com/)**

---


## Technologies Used

Kept the stack simple:
- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS, JavaScript
- **Database**: SQLite

## Local Setup and Installation

Run on yo machine

### 1. Prerequisites
- Python 3.7+

### 2. Clone the Repository
Pull the code down to your machine:
```bash
git clone https://github.com/whoisZenix/ScatterSense.git
cd ScatterSense
```

### 3. Install Dependencies
recommend setting up a virtual environment:

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

# Install the packages
pip install -r requirements.txt
```

### 4. Run the Application
Start up the Flask server.

```bash
python app.py
```
Open your browser and navigate to `http://localhost:5000`

## How to Use

- **Log a Session**: Use the main form on the dashboard to input your session date, time, duration, energy state, and the type of task you were working on.
- **Review**: Check the dashboard list right below it to see what you just logged.
- **Analyze Trends**: Scroll over to the insights charts to start spotting trends in your workflow once you have enough data.
- **Manage**: Delete old or incorrect entries whenever you need to.

## Built By

- Me 
