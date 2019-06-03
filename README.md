# canon_law


A service for referencing Orthodox canon law.

## Self-Host Installation

### Step 1. Python Setup (Linux/MacOS)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -U colorama flask tinydb
```

### Step 1. Python Setup (Windows)
```bat
python3 -m venv venv
.\venv\Scripts\activate
pip install -U colorama flask tinydb
```

### Step 2. Setting Environment Variables

You will need to set your flask environment to `development` or `production`, with the former having an interactive debugger and live reload.

For Linux, you will use `export FLASK_ENV=<option>` where \<option\> is one of settings aforementioned. For Windows, this is `set FLASK_ENV=<option>`.

Finally, set the FLASK_APP environment variable to `canon_law` by doing `export FLASK_APP=canon_law` or `set FLASK_APP=canon_law`, the latter if you are on Windows.

### Step 3. Launch

Do `flask run` and the service should start up. If it doesn't, please [file an issue](https://github.com/vypr/canon_law/issues/new) so I can get to work. :)