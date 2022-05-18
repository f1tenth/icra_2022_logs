F1Tenth Log Player
==================

This Repo can replay the F1Tenth Log files generated by Riders.

# Installation

First install [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html), if you haven't.

```bash
virtualenv -p python3 venv
source venv/bin/activate
```

After that, install dependencies:

```bash
pip install -e src/gym
pip install -e src/player
```

Finally run `main.py`:

```bash
python src/main.py
```