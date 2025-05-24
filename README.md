# My-Recommender

## Overview
A modular Python recommender system that suggests open-source projects to developers based on their skills and interests.

### Features:
- Modular file structure (models, data, ML logic, API)
- Pydantic schemas with UUID support
- Fake data generator for users and projects
- ML-based recommendation using cosine similarity (CountVectorizer)
- FastAPI endpoint to expose the recommendation engine

## File Structure

```
src/my_recommender/
├── api/
│   └── api.py               # FastAPI routes
├── data/
│   └── loader.py            # Fake data generator
├── ml/
│   └── recommender.py       # ML recommendation logic
├── models/
│   └── models.py            # Pydantic schemas
```

## How to Run

1. Install dependencies:
```bash
poetry install
```

2. Run the API:
```bash
poetry run uvicorn my_recommender.api.api:app --reload
```

3. Visit [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

## Example Endpoint

POST `/recommend/projects/`

Input (example User model):
```json
{
  "user_id": "a1b2c3d4-5678-1234-9876-abcdefabcdef",
  "username": "codewizard",
  "skills": ["python", "fastapi"],
  "interests": ["ai", "education"],
  "starred_projects": [],
  "contributed_projects": [],
  "github_url": "https://github.com/codewizard"
}
```

Returns:
- List of top-N recommended projects based on cosine similarity.

---


