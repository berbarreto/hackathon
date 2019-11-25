import pandas as pd
import requests
from zipfile import ZipFile
import glob

URL = r'https://archive.ics.uci.edu/ml/machine-learning-databases/00501/PRSA2017_Data_20130301-20170228.zip'
ARCHIVE = r'PRSA2017_Data_20130301-20170228.zip'
PATH = r'data/PRSA_Data_20130301-20170228/'

r = requests.get(URL)

with open('data/' + ARCHIVE, "wb") as code:
    code.write(r.content)

with ZipFile('data/' + ARCHIVE, 'r') as zip:
    zip.extractall('data/')

all_files = glob.glob(PATH + '/*.csv')
df = pd.concat(pd.read_csv(f) for f in all_files)
df.to_csv('data/processed/allFiles.csv')

