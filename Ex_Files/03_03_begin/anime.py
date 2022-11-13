import csv
from pprint import pprint
with open('/workspaces/linkedin-github-python-1/Ex_Files/03_01_begin/anime.csv', 'r') as f:
    read = csv.DictReader(f)
    out = list(read)
with open('anime.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(out)
