import arxiv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from tqdm import tqdm

searchfor = []
with open('./journals.txt', 'r') as f:
    searchfor = f.readlines()
searchfor = [x.strip() for x in searchfor]
    
papers = []
with open('arxiv_data.json', 'r') as f:
    for x in tqdm(f):
        flag = False
        journal = json.loads(x)['journal-ref']
        if journal:
            for y in searchfor:
                if journal.find(y) != -1:
                    flag = True
                    break
        if flag:
            papers.append(json.loads(x))