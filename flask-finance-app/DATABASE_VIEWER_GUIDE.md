# How to View Your SQLite Database

## 🏆 BEST OPTION: DB Browser for SQLite (Recommended)

### Download & Install:

**Direct Download Link:**
https://sqlitebrowser.org/dl/

**For Windows:**
1. Download: `DB.Browser.for.SQLite-v3.12.2-win64.msi` (or latest version)
2. Run the installer
3. Follow installation wizard
4. Done!

**Alternative portable version (no install needed):**
https://github.com/sqlitebrowser/sqlitebrowser/releases
- Download the `.zip` file
- Extract and run `DB Browser for SQLite.exe`

### How to Use:
1. Open DB Browser for SQLite
2. Click "Open Database" button
3. Navigate to: `c:/financial marketing/flask-finance-app/finance.db`
4. Browse all tables with visual interface!

**Features:**
- ✅ View all tables in tabs
- ✅ Edit data directly
- ✅ Run SQL queries
- ✅ Export data to CSV/JSON
- ✅ See database structure
- ✅ FREE and open source

---

## 🔧 OPTION 2: Python Script (Already Created)

I've created scripts for you in the flask-finance-app folder:

### Quick Summary:
```bash
python show_db.py
```

### Detailed View:
```bash
python view_database.py
```

---

## 💻 OPTION 3: VS Code Extension

**Extension Name:** SQLite Viewer

### Install:
1. Open VS Code
2. Click Extensions icon (Ctrl+Shift+X)
3. Search: "SQLite Viewer" by alexcvzz
4. Click "Install"

### Use:
1. In VS Code file explorer, find `finance.db`
2. Right-click → "Open Database"
3. View tables in VS Code!

---

## 🌐 OPTION 4: Online Viewer (No Install)

**Website:** https://sqliteviewer.app/

### Steps:
1. Go to the website
2. Click "Choose File"
3. Select your `finance.db` file
4. View in browser!

**Note:** Your data stays local, not uploaded to server

---

## 🖥️ OPTION 5: Command Line (For Advanced Users)

### Using PowerShell:

```powershell
# Check if sqlite3 is available
sqlite3 --version

# If not installed, download from:
# https://www.sqlite.org/download.html

# Open database
cd "c:/financial marketing/flask-finance-app"
sqlite3 finance.db

# SQLite commands:
.tables              # List all tables
.schema users        # Show table structure
SELECT * FROM users; # View data
.quit                # Exit
```

---

## 📊 Your Database Structure:

### Tables:
1. **users** - User accounts and financial info
2. **portfolio** - Stock holdings
3. **chat_history** - AI chatbot conversations
4. **advisor_requests** - Human advisor consultation requests

### Current Data:
- 1 user (Mythri)
- 8 portfolio stocks
- 4 chat messages
- 1 advisor request

---

## 🚀 Quick Start (Easiest Method):

**I recommend DB Browser for SQLite:**

1. Download: https://sqlitebrowser.org/dl/
2. Install (2 minutes)
3. Open → Select finance.db
4. Done! Visual interface ready

**Portable version (no install):**
https://github.com/sqlitebrowser/sqlitebrowser/releases/download/v3.12.2/DB.Browser.for.SQLite-3.12.2-win64.zip

Extract and run directly!
