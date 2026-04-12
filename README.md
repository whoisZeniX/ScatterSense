# ScatterSense 🎯

Hey everyone! Welcome to ScatterSense. I built this app to help keep track of productivity, work sessions, and energy levels throughout the day. If you've ever wondered when you're actually doing your best work, this might help you figure it out.

**[Check out the live app here!](https://scattersense.onrender.com)**

---

## What does it do?
ScatterSense is a simple dashboard where you can log the work you do. You just drop in:
- What kind of task it was
- How long it took
- Your energy level at the time

Over time, the app builds up data and gives you insights. It helps you realize things like "Oh, I actually get my best coding done at 10 AM when I have high energy" or "I should probably stop writing docs late at night." It's just a handy way to spot patterns in your workflow.

## Tech Stack
I kept the stack pretty straightforward and lightweight:
- **Backend:** Python + Flask
- **Database:** SQLite (no messy config required)
- **Frontend:** HTML, CSS, and basic JavaScript for some interactive bits.

## Running it locally

If you want to poke around the code or run your own private instance, it's really easy to get started:

1. Clone the repo:
   ```bash
   git clone https://github.com/whoisZenix/ScatterSense.git
   cd ScatterSense
   ```

2. Set up a Python virtual environment (so your global packages don't get messed up):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask server! 
   It'll automatically create a local `scattersense.db` SQLite file for you on the first run.
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://localhost:5000`

## Author

Built by **Zenix**.
- Email: zkavish8@gmail.com
- GitHub: [whoisZenix](https://github.com/whoisZenix)

Feel free to open an issue or reach out if you have questions!
