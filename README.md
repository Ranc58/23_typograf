# Typograf Service

This script prepares your text for publish.

**Operations:**
- quotes replacement `'` and `"` to `« »`.
- replace hyphens with dashes where it's need.
- in telephone numbers replace hyphens with short dashes.
- linking numbers with subsequent words with an indissoluble space.
- delete excess spaces and line-breaks.
- linking any words of 1-2 characters followed by words.

# How to install

1. Recomended use venv or virtualenv for better isolation.\
   Venv setup example: \
   `python3 -m venv myenv`\
   `source myenv/bin/activate`
2. Install requirements: \
   `pip3 install -r requirements.txt` (alternatively try add `sudo` before command)

# How to launch:
```
$python server.py
```
If all OK, You'll see in CLI:
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Then go to your browser `http://127.0.0.1:5000/`. 

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
