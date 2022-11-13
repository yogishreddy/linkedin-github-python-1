import csv
from pprint import pprint
with open('anime.csv','r') as f:
  read= csv.DictReader(f)
  tolist=list(read)
for quotes in tolist:
  if quotes['Anime']=='One Piece':
    pprint(quotes)
    break
