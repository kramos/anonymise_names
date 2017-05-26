from nltk.tag.stanford import StanfordNERTagger
import sys

dirty = sys.argv[1]

st = StanfordNERTagger('stanford-ner/english.all.3class.distsim.crf.ser.gz', 'stanford-ner/stanford-ner.jar')

parsed = st.tag(dirty.split())
cleaned = ''
for key in parsed:
  if key[1] == 'PERSON':
    cleaned += 'PERSON '
  else:
    cleaned += key[0] + ' '

cleaned = cleaned.replace('her', 'their')
cleaned = cleaned.replace('his', 'their')
print(cleaned)
