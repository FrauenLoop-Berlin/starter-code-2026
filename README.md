# Café Cozy — Minimal Flask site

Simple Flask website with a small SQLite database. Contains two pages: Home and About.

Setup

1. Create a virtual environment and install dependencies:

For macOS / Linux:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

For Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

For Windows Command Prompt:

```cmd
python -m venv venv
venv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

2. Initialize the SQLite database (creates `instance/coffee.db` and sample menu):

```bash
python init_db.py
```

3. Run the app:

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

Files

- `app.py`: Flask application
- `init_db.py`: creates SQLite DB and sample data
- `templates/`: HTML templates (Home and About)
- `static/css/style.css`: basic styles
- `static/img/`: images to use in the project

