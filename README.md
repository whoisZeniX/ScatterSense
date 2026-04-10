# ScatterSense

<div align="center">
   
**ScatterSense is a productivity tracking application designed to provide insights into your work sessions. It allows users to log their focus sessions, track energy levels, and analyze performance patterns to optimize productivity.**

<br>

**[ View Live Demo Here ](https://scattersense.onrender.com)**  
*(Replace this with your actual live project link if different)*

</div>

## Features

*   **Session Management:**
    *   **Log Work:** Record session details including date, time period, duration, and task type.
    *   **Energy Tracking:** Monitor your energy levels for each session to understand your peak productivity times.
    *   **History:** View a comprehensive log of all past sessions.
*   **Analytics & Insights:**
    *   **Performance Metrics:** Analyze how different factors contribute to your workflow.
    *   **Visual Data:** Interactive charts to visualize productivity trends over time.
    *   **Optimization:** Identify the best times of day and task types for maximum efficiency.
*   **User Interface:**
    *   **Clean Dashboard:** A streamlined interface for effortless data entry and review.
    *   **Responsive Design:** Accessible on various devices.

## Technologies Used

*   **Backend:** Python, Flask
*   **Database:** SQLite
*   **Frontend:** HTML5, CSS3, JavaScript

## Local Setup and Installation

Follow these steps to get the application running on your local machine.

### 1. Prerequisites

*   Python 3.7+
*   `pip` (Python package installer)

### 2. Clone the Repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/whoisZenix/ScatterSense.git
cd ScatterSense
```

### 3. Create a Virtual Environment

It is highly recommended to create a virtual environment to manage project dependencies.

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

Install the required Python libraries using `pip`.

```bash
pip install -r requirements.txt
```

### 5. Configuration

This project uses a local SQLite database which is initialized automatically.

1.  **Database:** The `scattersense.db` file will be created in the root directory upon the first run.

### 6. Run the Application

Once the setup is complete, you can start the Flask development server:

```bash
python app.py
```

Now, open your web browser and navigate to the following address:

```
http://localhost:5000/
```

You should see the **ScatterSense** dashboard running!

## How to Use

1.  **Access the Dashboard:** Open the application in your browser.
2.  **Log a Session:** Use the submission form to enter your session date, time, duration, energy level, and task type.
3.  **Review Data:** Check the dashboard list to see your logged sessions.
4.  **Analyze Trends:** Use the insights section to understand your productivity habits.
5.  **Manage Entries:** Delete incorrect or old entries as needed.

## Author

-   Name: Zenix
-   Email: zkavish8@gmail.com
-   GitHub: whoisZenix
