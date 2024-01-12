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
├── src         : directory of source code
└── venv        : manage virtual environment with virtualenv
```

## Getting started

1. Go to the project directory and activate the virtual environment:

- On Windows:

```bash
.\venv\Scripts\activate
```

- On macOS or Linux:

```bash
source venv/bin/activate
```

2. Install required packages

```bash
pip install -r requirements.txt
```

3. Run the Python Script
Run the Python script using the Python interpreter

```bash
python check-duplicated-datasets.py
```

4. Deactivate the virtual environment
When you are done, you can deactivate the virtual environment with the command 
 

```bash
deactivate
```
