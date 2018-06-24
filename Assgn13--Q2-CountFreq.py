import re
import string
frequency={}
count_freq=open('count.txt','r')
string=count_freq.read().lower()
pattrn=re.findall(r'\b[a-z]{3,15}\b',string)

for word in pattrn:
    count=frequency.get(word,0)
    frequency[word]=count + 1
    
frequency_list=frequency.keys()

for words in frequency_list:
    print(words, frequency[words])
