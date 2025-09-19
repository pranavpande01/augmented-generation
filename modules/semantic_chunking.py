import nltk
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

try:
    nltk.data.path("/workspaces/augmented-generation/utils")
    nltk.data.find("tokenizers/punkt")
except:
    nltk.download("punkt",download_dir="/workspaces/augmented-generation/utils")