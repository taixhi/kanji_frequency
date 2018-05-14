# kanji_frequency
![Visualisation](https://raw.githubusercontent.com/taixhi/kanji_frequency/master/Kanji%20Frequency.png)
Use the wikipedia dump to produce a kanji frequency csv.
## Requirements
* python3
* tqdm (for progress bars)
* [WikiExtractor](https://github.com/attardi/wikiextractor)

## Setup
To generate the kanji frequency hashmap:
`python3 main.py`
Use the saved hashmap to create a csv:
`python3 load.py`
Optional:
Use [WordItOut](https://worditout.com) for visualisation
