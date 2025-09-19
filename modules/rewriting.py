import numpy as np
import nltk
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

try:
    nltk.data.find("tokenizers/punkt")
except:
    nltk.download('punkt')

def chunker(text:str,similarity_threshhold:float=0.82):
     mode=SentenceTransformer('all-MiniLM-L6-v2')
     sentences=nltk.sent_tokenize(text)
     print(sentences)

a=chunker("hello how is she doing right now are you haveing acidity or not?")
print(a)
#/workspaces/augmented-generation/modules/rewriting.py