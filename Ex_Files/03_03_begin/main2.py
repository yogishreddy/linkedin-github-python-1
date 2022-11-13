import csv
import json
from pprint import pprint
with open('/workspaces/linkedin-github-python-1/Ex_Files/03_01_begin/anime.csv', 'r') as f:
    read = csv.DictReader(f)
    final = list(read)
with open('anime.json', 'w') as f:
    json.dump(final, f, indent=3)
