import nltk
from nltk import word_tokenize

sentence = [('the', 'DT'), ('little', 'JJ'), ('yellow', 'JJ'), ('dog', 'NN'), ('barked', 'VBD'), ('at', 'IN'),
            ('the', 'DT'), ('cat', 'NN')]

grammar = 'NP: {<DT>?<JJ>*<NN>}'

cp = nltk.RegexpParser(grammar)
#print(nltk.word_tokenize(str(cp)))
print(cp)
result = cp.parse(sentence)

print(result)
