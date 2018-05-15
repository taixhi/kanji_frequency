import re
import pickle
import MeCab
import operator
import sys
import csv
import os
from tqdm import tqdm
from heapq import nlargest

script_dir = os.path.dirname(__file__)
tokens = pickle.load(open(script_dir + "kanji_map.pkl", "rb"))
print(tokens)