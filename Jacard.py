import nltk
import re
from hazm import *
import os
class JacardSimilarity():
    def jacardsimilarity(self,doc1_name, doc2_name):
            #hazm test
            hazm_lemmatizer = Lemmatizer()
            print(hazm_lemmatizer.lemmatize('مادربزرگش'))
            lem_doc=[]
            lem_query=[]
            if not os.path.exists("logs"):
                os.mkdir("logs")
            doc1 = open(doc1_name, 'r', encoding='utf8')
            doc2 = open(doc2_name, 'r', encoding='utf8')
            for line in doc1:
                #print(line)
                words = re.findall(r'\w+', line)
                for word in words:
                    print(word)
                    lem_doc.append(hazm_lemmatizer.lemmatize(word))
            print("lemmitzaton doc---"+ str(lem_doc))
            for line in doc2:
                words = re.findall(r'\w+', line)
                for word in words:
                    print(word)
                    lem_query.append(hazm_lemmatizer.lemmatize(word))
            print("lemmitzaton query---"+str(lem_query))
            intersection = set(lem_query).intersection(set(lem_doc))
            union = set(lem_query).union(set(lem_doc))
            print(len(intersection)/len(union))

            fhandw = open('logs/lemm_doc.txt', 'w', encoding='utf8')
            b = " ".join(str(e) for e in lem_doc)
            fhandw.write(str(b))

            fhandw = open('logs/lemm_query.txt', 'w', encoding='utf8')
            b = " ".join(str(e) for e in lem_query)
            fhandw.write(str(b))

