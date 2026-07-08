📅 DAY 1
Theme

Professional Development Environment

Today's goal is not data analysis.

Today's goal is to become comfortable with the tools you'll use throughout the project.

🎯 Today's Learning Objectives

By the end of Day 1, you'll be able to:

Understand how Python projects are organized.
Create a professional project structure.
Use the Windows terminal confidently.
Create and activate a virtual environment.
Install packages with pip.
Initialize a Git repository.
Create a GitHub repository.
Push your project to GitHub.
Write meaningful commits.
Understand why each file exists.
📋 Today's Checklist

We will complete these 18 missions.

Mission	Topic
1	Check Python installation
2	Check VS Code
3	Check Git
4	Create project folder
5	Open project in VS Code
6	Understand the folder structure
7	Open the integrated terminal
8	Create a virtual environment
9	Activate the virtual environment
10	Understand pip
11	Install project packages
12	Generate requirements.txt
13	Create README.md
14	Create .gitignore
15	Initialize Git
16	Create the first commit
17	Push to GitHub
18	Verify everything
📂 Today's Project Structure

📅 Day 1 Overview
✅ Mission 1

Verify Development Environment

✅ Mission 2

Create Professional Project Structure

✅ Mission 3

Virtual Environment

🔜 Mission 4

Professional Dependency Management

Learn:

What pip is
How package installation works
How requirements.txt works
Semantic versioning
Best practices
🔜 Mission 5

Git Fundamentals

Learn:

What Git actually is
Repository
Commit
Working Tree
Staging Area
HEAD
Branch
🔜 Mission 6

Initialize the Git Repository

🔜 Mission 7

Create a Professional README

🔜 Mission 8

Create .gitignore

🔜 Mission 9

First Professional Commit

🔜 Mission 10

Create GitHub Repository & Push


By the end of today, your project should look like this:

Humanitarian_Analytics_Project/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   ├── processed/
│
├── python_scripts/
│
├── tasks/
│
├── solutions/
│
├── reports/
│
├── outputs/
│
├── images/
│
├── docs/
│
└── ALL_SYNTAX.py
📁 Files for Day 1

Unlike the following days, Day 1 has no datasets because we're not analyzing data yet.

Today's files are:

README.md
.gitignore
requirements.txt
Project folder structure

We'll create them together so you understand every line.

🚀 Mission 1 — Verify Your Development Environment

    Open PowerShell (or the VS Code terminal if you already have VS Code open) and run these commands one by one:

    python --version

    Then:

    pip --version

    Then:

    git --version

    Finally:

    code --version

🎯 Mission 2 — Create the Company Project
📖 Scenario

        You have just joined Global Relief Organization (GRO) as a Junior Data Analyst.

        Your team lead sends you this message:

        "Welcome! Before you start working with our data, create the project structure that every analyst in our department uses."

        Today's goal is to create a professional project structure that you will keep using throughout all 7 days.

        📌 Step 1 — Create the Project Folder

        Choose a location where you keep your coding projects.

        I recommend:

        C:\Users\<YourName>\Documents\Projects\

        or

        D:\Projects\

        Inside it, create a new folder named exactly:

        Humanitarian_Analytics_Project
        📌 Step 2 — Open the Project in VS Code
        Open VS Code.
        Click File → Open Folder...
        Select:
        Humanitarian_Analytics_Project

        Now VS Code should display this folder in the Explorer panel.

        📌 Step 3 — Open the Integrated Terminal

        In VS Code:

        Terminal → New Terminal

        or press

        Ctrl + `

        (the backtick key, usually under Esc).

        Your terminal should now be inside the project folder.

        Verify by running:

        pwd

        or

        Get-Location

        You should see something similar to:

        ...\Humanitarian_Analytics_Project
        📌 Step 4 — Create the Folder Structure

        Inside the project, create the following folders.

        Humanitarian_Analytics_Project/

        data/
            raw/
            cleaned/
            processed/
            external/

        python_scripts/

        tasks/

        solutions/

        reports/

        outputs/

        images/

        docs/

        tests/

        config/
        Option 1 (Recommended)

        Create them manually in VS Code.

        Option 2 (PowerShell)
        mkdir data
        mkdir data\raw
        mkdir data\cleaned
        mkdir data\processed
        mkdir data\external

        mkdir python_scripts
        mkdir tasks
        mkdir solutions
        mkdir reports
        mkdir outputs
        mkdir images
        mkdir docs
        mkdir tests
        mkdir config
        📌 Step 5 — Create the Project Files

        Now create these empty files in the project root:

        README.md

        requirements.txt

        .gitignore

        LICENSE

        main.py

        Later we'll add many more files.

        📌 Step 6 — Create the Python Package Structure

        Inside python_scripts, create these files:

        python_scripts/

        load_data.py

        clean_data.py

        analyze_data.py

        visualize_data.py

        statistics.py

        helpers.py

        config.py

        These are the scripts we'll gradually build over the next 7 days.

        📌 Step 7 — Create the Documentation Structure

        Inside docs create:

        Day01.md

        Day02.md

        Day03.md

        Day04.md

        Day05.md

        Day06.md

        Day07.md

        These will become your personal learning notes and project documentation.

        📌 Step 8 — Create the Tasks Structure

        Inside tasks create:

        Day01_Tasks.md

        Day02_Tasks.md

        Day03_Tasks.md

        Day04_Tasks.md

        Day05_Tasks.md

        Day06_Tasks.md

        Day07_Tasks.md
        📌 Step 9 — Create the Solutions Structure

        Inside solutions create:

        Day01_Solutions.md

        Day02_Solutions.md

        Day03_Solutions.md

        Day04_Solutions.md

        Day05_Solutions.md

        Day06_Solutions.md

        Day07_Solutions.md
        📌 Your Project Should Now Look Like This
        Humanitarian_Analytics_Project/
        │
        ├── README.md
        ├── LICENSE
        ├── requirements.txt
        ├── .gitignore
        ├── main.py
        │
        ├── config/
        ├── data/
        │   ├── raw/
        │   ├── cleaned/
        │   ├── processed/
        │   └── external/
        │
        ├── docs/
        ├── images/
        ├── outputs/
        ├── python_scripts/
        ├── reports/
        ├── solutions/
        ├── tasks/
        └── tests/
        💡 Why Are We Doing This?

        Most tutorials put everything in one folder.

        Real companies don't.

        As projects grow, keeping code, data, documentation, tests, reports, and outputs separate makes the project easier to maintain, collaborate on, and extend. This structure also looks professional when someone reviews your GitHub repository.

        🎯 Your Task

        Complete all the steps above.

        When you're done, send me either:

        A screenshot of the VS Code Explorer, or
        The output of:
        tree /F

        from the project root.

🎯 Mission 3
        Creating a Professional Virtual Environment

        I want to slow down here because this is one of the most important concepts in Python.

        Step 1

        Inside your project terminal run:

        python -m venv .venv

        Notice something important.

        We're naming it

        .venv

        instead of

        venv

        Why?

        Because VS Code automatically recognizes .venv as the project's virtual environment.

        Most modern Python projects use .venv.

        What happened?

        Python created an isolated environment containing:

        Humanitarian_Analytics_Project/

        .venv/

        Scripts/

        Lib/

        Include/

        pyvenv.cfg

        Nothing has been installed yet.

        Only a clean Python environment.

        Step 2

        Activate it.

        PowerShell

        .\.venv\Scripts\Activate

        Command Prompt

        .venv\Scripts\activate.bat
        Step 3

        If successful, your terminal changes.

        Instead of

        PS C:\Projects\Humanitarian_Analytics_Project>

        you should see

        (.venv) PS C:\Projects\Humanitarian_Analytics_Project>

        That small

        (.venv)

        is extremely important.

        It means

        Everything we install now belongs ONLY to this project.

        Why do companies use .venv?

        Because it makes projects:

        ✅ Reproducible

        ✅ Isolated

        ✅ Easy to share

        ✅ Easy to deploy

        Step 4

        Let's verify which Python VS Code is using.

        Run:

        where python

        or

        Get-Command python

        You should see a path similar to

        ...\Humanitarian_Analytics_Project\.venv\Scripts\python.exe

        If you still see the global Python installation, we'll fix it before continuing.

        🧠 Learning Moment

        Don't just memorize this command:

        python -m venv .venv

        Understand it:

        Part	Meaning
        python	Run the Python interpreter
        -m	Run a Python module as a script
        venv	The built-in virtual environment module
        .venv	Create the environment in a folder named .venv

        This pattern (python -m module_name) is common in Python, and you'll see it throughout your career.

        🎯 Your Tasks

        Complete these steps:

        Create the .venv environment.
        Activate it.
        Verify that (.venv) appears in the terminal prompt.
        Run where python (or Get-Command python) and share the output.

🎯 Mission 4 — Professional Dependency Management
        📖 Scenario

        Your manager says:

        "Before anyone else on the team can work on this project, we need to define all the Python libraries it depends on."

        That's what dependency management is.

        What is a Dependency?

        A dependency is simply another package your project needs.

        For example:

        import pandas as pd

        Your code depends on the pandas package.

        If pandas isn't installed, Python raises:

        ModuleNotFoundError: No module named 'pandas'
        What is pip?

        pip stands for Package Installer for Python.

        It downloads packages from the Python Package Index (PyPI).

        Think of it like this:

        Python  ← Operating System

        pip     ← App Store

        PyPI    ← Online Store

        Packages ← Apps
        📦 Packages We'll Install

        We're not installing everything today—only what we'll actually use during this 7-day project.

        Package	Purpose	Used On
        numpy	Numerical computing	Days 2–7
        pandas	Data analysis	Days 2–7
        matplotlib	Visualization	Days 4–7
        scipy	Statistics	Day 5
        statsmodels	Statistical modeling	Days 5–7
        openpyxl	Excel support	Days 2–7

        Later we'll add packages like plotly or scikit-learn if the project grows.

        📌 Step 1 — Install the Packages

        Run these commands one at a time so you can see what each one installs:

        pip install numpy
        pip install pandas
        pip install matplotlib
        pip install scipy
        pip install statsmodels
        pip install openpyxl
        📌 Step 2 — Verify the Installations

        Run:

        pip list

        You should see packages including:

        numpy
        pandas
        matplotlib
        scipy
        statsmodels
        openpyxl
        📌 Step 3 — Generate requirements.txt

        Now run:

        pip freeze > requirements.txt

        Open requirements.txt.

        You'll notice it contains many more packages than the six you installed. That's because some packages depend on other packages, and pip freeze records the entire environment so someone else can recreate it exactly.

        🎓 Mini Challenge

        Before moving on, answer these questions in your own words:

        What is the difference between pip install and pip freeze?
        Why do we install packages inside .venv instead of globally?
        Why is requirements.txt important when sharing a project?

        Don't worry if your answers aren't perfect. This is to help build your understanding.

        