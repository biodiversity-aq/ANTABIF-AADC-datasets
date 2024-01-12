# ANTABIF AADC datasets

This repo contains Python script (Python 3.11) to get datasets from:

- AADC IPT
- AADC DiGIR
- ANTABIF IPT

The script gets dataset title from these installation and the following comparisons were done to identify duplicates.

- common dataset titles between AADC IPT and ANTABIF IPT
- common dataset titles between AADC DiGIR and ANTABIF IPT

All datasets from all the IPT and DiGIR instances above were written into file `data/datasets_from_installations.txt`.

## Repo structure

```markdown
.
├── README.md
├── data        : directory to store data generated from script from src/
├── requirements.txt    : list of required packages
└── src         : directory of source code
```

## Getting started

### Setting Up a Virtual Environment

To get started, we recommend setting up a Python virtual environment. This ensures that you have all the necessary dependencies installed and that our project does not interfere with your other Python projects. Here's how you can set it up:
Prerequisites

Before you begin, make sure you have Python installed on your system. This project is compatible with Python 3.x. You can check your Python version by running:

```bash
python3 --version
```

### Step-by-Step Guide

1. Clone the Project Repository (if you haven't already):

```bash
git clone git@github.com:biodiversity-aq/ANTABIF-AADC-datasets.git
cd ANTABIF-AADC-datasets
```

2. Create the Virtual Environment:
Execute the following command in your project's root directory:

- For Windows:

```bash

python -m venv venv
```

- For macOS and Linux:

```bash
python3 -m venv venv
```

This creates a venv directory in your project folder, containing the Python interpreter and other necessary files.

3. Activate the Virtual Environment:
To activate the virtual environment, use the appropriate command for your operating system:

- Windows:

```bash
.\venv\Scripts\activate
```

- macOS and Linux:

```bash
source venv/bin/activate
```
You'll know the virtual environment is active when you see its name (venv) appear at the beginning of your command prompt.

4. Install Project Dependencies:
With the virtual environment active, install the project dependencies:

```bash
pip install -r requirements.txt
```

This command installs all the necessary Python packages as specified in the requirements.txt file.

5. Exiting the Virtual Environment:

When you've finished working on the project, you can deactivate the virtual environment by running:

```bash
deactivate
```

### Note

It's important to ensure that the virtual environment is active whenever you work on the project.
If there are updates to the project dependencies, re-run pip install -r requirements.txt to stay up to date.