from Normalization import Normal
from Toeknization import Tokenization
from Jacard import JacardSimilarity

persian_norm=Normal()
persian_norm.nomal('logs/doc.txt')
persian_token=Tokenization()
persian_token.token(persian_norm.name)

persian_norm1=Normal()
persian_norm1.nomal('logs/doc2.txt')
persian_token1=Tokenization()
persian_token1.token(persian_norm1.name)

persian_similarity=JacardSimilarity()
persian_similarity.jacardsimilarity(persian_token.name,persian_token1.name)

