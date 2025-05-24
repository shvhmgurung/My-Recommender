from fastapi import FastAPI
from typing import List
from my_recommender.models.models import User, Project
from my_recommender.ml.recommender import recommend_projects
from my_recommender.data.loader import generate_fake_users, generate_fake_projects

app = FastAPI(title="Dev Recommender API")

# Generate fake data at startup (can replace with DB or real data in v2)
users = generate_fake_users(7)
projects = generate_fake_projects(5, user_list=users)

@app.get("/")
def root():
    return {"msg": "Dev Recommender System is running."}

@app.post("/recommend/projects/", response_model=List[Project])
def get_recommendations(user: User, top_n: int = 3):
    """
    Recommend projects to a user.
    """
    recs = recommend_projects(user, projects, top_n=top_n)
    return recs