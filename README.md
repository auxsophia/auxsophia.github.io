# [www.philosopherscholar.com](https://www.philosopherscholar.com) - Personal Website

This is the source code for my personal webpage: [www.philosopherscholar.com](https://www.philosopherscholar.com).

This site is built using **Pelican**, a static site generator written in Python.

---

## 🛠️ First-Time Setup (New Machine)

To get this site running on a completely fresh machine, you will need Python 3 installed. Then, follow these steps in your terminal or PowerShell:

**1. Clone the repository and navigate into it**
```bash
git clone https://github.com/auxsophia/auxsophia.github.io.git
cd auxsophia.github.io
```

**2. Create and activate a Virtual Environment**
It is highly recommended to isolate the site's dependencies.
* **On Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
* **On Linux/Ubuntu:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

**3. Install Dependencies**
Install Pelican and the Markdown parser. *(Note: If you have created a requirements.txt, you can just run `pip install -r requirements.txt` instead).*
```bash
pip install pelican Markdown
```

---

## 💻 Daily Workflow & Local Development

When you are writing new essays or making layout changes, use this workflow to preview the site locally:

**1. Sync Git Dates (Crucial for the Directory)**
Before building, always run the custom script to pull the correct Git creation/modification dates so the Master Directory sorts correctly:
```bash
python sync_git_dates.py
```

**2. Build the Site**
Compile the Markdown files into static HTML. This will safely rebuild the layout, apply the CSS grids, and move the default blog roll out of the way.
```bash
pelican content
```

**3. Serve Locally**
Spin up the local web server to preview your changes. 
```bash
pelican --listen
```
*(Tip: You can also use `pelican --listen --autoreload` or `pelican -lr` to make the server automatically rebuild the site every time you hit "Save" on a file!)*

Your local site will now be visible in your browser at: `http://localhost:8000`
```