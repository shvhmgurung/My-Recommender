from fastapi import FastAPI
from fastapi.responses import JSONResponse
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
    """
    Show sample recommendations for a demo user right on the homepage.
    """
    demo_user = users[0]  # Just pick the first fake user
    recs = recommend_projects(demo_user, projects, top_n=3)

    return JSONResponse({
        "demo_user": demo_user.model_dump(mode="json"),
        "recommendations": [p.model_dump(mode="json") for p in recs]
    })

@app.post("/recommend/projects/", response_model=List[Project])
def get_recommendations(user: User, top_n: int = 3):
    """
    Recommend projects to a user.
    """
    recs = recommend_projects(user, projects, top_n=top_n)
    return recs