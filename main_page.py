from Normalization import Normal
from Toeknization import Tokenization
from Jacard import JacardSimilarity
from Cosine import CosineSimilarity

persian_norm=Normal()
persian_norm.nomal('logs/doc.txt')
persian_token=Tokenization()
persian_token.token(persian_norm.name)

persian_norm1=Normal()
persian_norm1.nomal('logs/doc2.txt')
persian_token1=Tokenization()
persian_token1.token(persian_norm1.name)

persian_jaccard=JacardSimilarity()
persian_jaccard.jacardsimilarity(persian_token.name,persian_token1.name)

persian_cosine=CosineSimilarity()
persian_cosine.cosinesimilarity(persian_token.name,persian_token1.name)



