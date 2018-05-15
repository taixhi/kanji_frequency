import re
import pickle
import MeCab
import operator
import sys
import csv
import os
from tqdm import tqdm
from heapq import nlargest

with open("/Users/taichikato/Downloads/wikiextractor/corpus/AA/wiki_00") as f:
	content = f.readlines()
letters = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~!@#$%^&}*()_+{|:\"<>?`-=[];',./\n〜！＠＃＄％＾＆＊（）＿＋『』｜：”＜＞？、。・；’「」￥ー＝0123456789０１２３４５６７８９ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴ"
script_dir = os.path.dirname(os.path.realpath(__file__)) + '/'
mode = "kanjis" #Either 漢字摘出: "kanji" or 熟語摘出： "jukugo"
def tokenize():
	tokens=[]
	print("File loaded")
	t = MeCab.Tagger()
	for line in tqdm(content, unit="line", total=len(content), unit_divisor=1024, desc="Finding Jukugos"):
		m = t.parseToNode(line)
		while m:
			tokens.append(m.surface)
			m = m.next
	return tokens
def extract_kanji():
	kanjis=[]
	print("File loaded")
	for line in tqdm(content, unit="line", total=len(content), unit_divisor=1024, desc="Finding Kanjis"):
		for character in list(line):
			if character not in list(letters):
				kanjis.append(character)
	return kanjis
def map_book(tokens):
	print("Begin Mapping")
	hash_map = {}
	if tokens is not None:
		for element in tqdm(tokens, unit="char", desc="HashMapping", ):
			if element in hash_map:
				hash_map[element] = hash_map[element] + 1
			else:
				hash_map[element] = 1
		return hash_map
	else:
		print("No token found")
		return None
def save_obj(obj, name ):
	with open(script_dir + name + '.pkl', 'wb+') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
		print("Saved")

csvfile = "token.csv"
tokens = []
if mode is "kanjis":
	tokens = extract_kanji()
elif mode is "jukugo":
	tokens = tokenize()
map = map_book(tokens)
save_obj(map, "temp/" + mode + "_map")
save_obj(tokens, "temp/" + mode + "_tokens")
print("END")
