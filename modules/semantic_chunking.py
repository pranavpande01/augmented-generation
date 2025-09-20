import nltk
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

try:
    nltk.data.path("/workspaces/augmented-generation/utils")
    nltk.data.find("tokenizers/punkt")
except:
    nltk.download("punkt",download_dir="/workspaces/augmented-generation/utils")

def semantic_chunker(text:str,similarity_threshhold: float=0.82):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    sentences=nltk.sent_tokenize(text)
    return sentences

