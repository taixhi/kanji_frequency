import re
import pickle
from tqdm import tqdm
from heapq import nlargest

with open("/Users/taichikato/Downloads/wikiextractor/corpus/AA/wiki_00") as f:
	content = f.readlines()
kanjis=[]
letters = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~!@#$%^&}*()_+{|:\"<>?`-=[];',./\n〜！＠＃＄％＾＆＊（）＿＋『』｜：”＜＞？、。・；’「」￥ー＝0123456789０１２３４５６７８９ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴ"
print("File loaded")
for line in tqdm(content, unit="line", total=len(content), unit_divisor=1024, desc="Finding Kanjis"):
	line = re.sub(letters, '', line)
	for character in list(line):
		if character not in list(letters):
			kanjis.append(character)
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
map = map_book(kanjis)
def save_obj(obj, name ):
	with open('/Users/taichikato/Developer/kanji_frequency/'+ name + '.pkl', 'wb+') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
		print("Saved")

save_obj(map, "kanji_map")
print("END")
