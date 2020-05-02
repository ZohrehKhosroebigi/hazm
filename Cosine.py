import logging
import numpy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
class CosineSimilarity():
    def cosinesimilarity(self,doc1,doc2):

        logging.basicConfig(level=logging.DEBUG,filename='logs/cosine.logs', filemode='w')
        #doc1 = open(doc1, 'r', encoding='utf8')
        #doc2 = open(doc2, 'r', encoding='utf8')

        doc1 = open('logs/lemm_doc.txt', 'r', encoding='utf8')
        doc2 = open('logs/lemm_query.txt', 'r', encoding='utf8')

        for line in doc1:
            dataset1=line
            #dataset1 = 'خدا'
        for line in doc2:
            dataset2=line
            #dataset2 = 'خدا حافظ'
        dataset = [dataset1,dataset2]
        vectorizer = TfidfVectorizer()
        X_tfidf = vectorizer.fit_transform(dataset)
         # ...you say you are already at this point here...

        sims = cosine_similarity(X_tfidf, X_tfidf)
        rank = list(reversed(numpy.argsort(sims[0])))

        #logging.debug("\nTdidf: \n%s" % X_tfidf.toarray())
        logging.debug("\nSims: \n%s", sims)
        logging.debug("\nRank: \n%s", rank)