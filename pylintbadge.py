import os.path
import re

def get_pylintScore(file = "pylint_report.txt"):
    content = ""

    # Read the pylint output file and raise an error if it does not exist
    if not os.path.isfile(file):
        raise FileNotFoundError(f"Pylint output file not found at {file}")

    with open(file, "r", encoding="utf8") as f:
        content = f.read()
        print(content)

    # Extract the score from the pylint output by looking fo the patter: Your code has been rated at 9.83/10 (previous run: 9.83/10, +0.00)
    pattern = r"(?<=rated at )(\d+\.\d+)"
    match = re.search(pattern, content)

    return match.group(0)



def get_color(score):
    if score > 9:
        return 'brightgreen'
    if score > 8:
        return 'green'
    if score > 7.5:
        return 'yellowgreen'
    if score > 6.6:
        return 'yellow'
    if score > 5.0:
        return 'orange'
    if score > 0.00:
        return 'red'
    return 'bloodred'

README_PATH = "README.md"
NUMERIC_SCORE = get_pylintScore()
BADGE_TEXT = 'PyLint'
BADGE_COLOR = get_color(float(NUMERIC_SCORE))

if not os.path.isfile(README_PATH):
    raise FileNotFoundError(f"README.md path is wrong, no file can be located at {README_PATH}")

with open(README_PATH, "r", encoding="utf8") as f:
    content = f.read()

query = f"{BADGE_TEXT}-{NUMERIC_SCORE}-{BADGE_COLOR}?logo=python&logoColor=white"
badge_url = f"https://img.shields.io/badge/{query}"

patt = r"(?<=!\[pylint]\()(.*?)(?=\))"
if re.search(patt, content) is None:
    raise ValueError("Pylint badge not found! Be sure to put an empty one which acts as a placeholder "
                     "if this is your first run. Check README.md for examples!")

result = re.sub(patt, badge_url, content)
with open(README_PATH, "w", encoding="utf8") as f:
    f.write(result)