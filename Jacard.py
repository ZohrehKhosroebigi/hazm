import nltk
import re
from hazm import *
import os
from writing import Writelogs
class JacardSimilarity():
    def jacardsimilarity(self,doc1_name, doc2_name):
            #hazm test
            lem_doc=""
            lem_query=""
            hazm_lemmatizer = Lemmatizer()
            print(hazm_lemmatizer.lemmatize('مادربزرگش'))
            doc1_name='logs/lemm_doc.txt'
            doc2_name='logs/lemm_query.txt'
            if not os.path.exists("logs"):
                os.mkdir("logs")
            doc1 = open(doc1_name, 'r', encoding='utf8')
            doc2 = open(doc2_name, 'r', encoding='utf8')
            for line in doc1:
                lem_doc = lem_doc + line
            for line in doc2:
                lem_query = lem_query + line
           #jacard
            intersection = set(lem_query).intersection(set(lem_doc))
            union = set(lem_query).union(set(lem_doc))
            writeresult=Writelogs()
            writeresult.writing(str(len(intersection)/len(union)))
            print("jacard distance is ------"+str(len(intersection)/len(union)))