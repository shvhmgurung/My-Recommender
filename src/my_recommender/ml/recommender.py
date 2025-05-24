from typing import List
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from my_recommender.models.models import User, Project

def recommend_projects(user: User, projects: List[Project], top_n: int = 3) -> List[Project]:
    """
    Recommend projects to a user using cosine similarity of skills/interests vs. project tags.
    """
    user_text = " ".join(user.skills + user.interests)
    project_texts = [" ".join(proj.tags) for proj in projects]
    corpus = [user_text] + project_texts

    vec = CountVectorizer().fit_transform(corpus)
    vectors = vec.toarray()

    user_vec = vectors[0].reshape(1, -1)
    project_vecs = vectors[1:]
    similarities = cosine_similarity(user_vec, project_vecs)[0]

    top_indices = similarities.argsort()[-top_n:][::-1]
    recommended = [projects[i] for i in top_indices]

    return recommended