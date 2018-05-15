import operator
import pickle
import csv
import sys
import os
script_dir = os.path.dirname(os.path.realpath(__file__)) + '/'
kanjis = pickle.load(open(script_dir + "kanji_map.pkl", "rb"))
# sortedkanjis = sorted(kanjis.items(), key=operator.itemgetter(1))

csvfile = "years.csv"
with open(script_dir + csvfile, "w+") as output:
	writer = csv.writer(output)
	for key, val in kanjis.items():
		writer.writerow([key, val])