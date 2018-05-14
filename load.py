import operator
import pickle
import csv
script_dir = os.path.dirname(__file__)
kanjis = pickle.load(open(script_dir + "kanji_map.pkl", "rb"))
sortedkanjis = sorted(kanjis.items(), key=operator.itemgetter(1))

csvfile = "frqdist.csv"
with open(script_dir + csvfile, "w+") as output:
    writer = csv.writer(output, lineterminator='\n')
    for key,val in sortedkanjis:
        writer.writerow([key,val]) 