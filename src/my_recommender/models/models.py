from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field
from uuid import UUID



class User(BaseModel):
    """
    API schema representing a user profile for recommendations.
    Intended for future use in database mapping with strict UUID relationships.
    """
    user_id: UUID = Field(..., description="Unique user identifier (UUID)")
    username: str = Field(
         ...,
         min_length=3,
         max_length=30, 
         description="Unique username or handle for the user")
    skills: List[str] = Field(
        ..., 
        min_items=1, 
        description="List of technical skills (must have at least one)")
    interests: List[str] = Field(default_factory=list, description="Broader interests for matching")
    starred_projects: List[UUID] = Field(default_factory=list, description="Project IDs starred by the user")  # UUID references for strict matching, may map to foreign keys in DB
    contributed_projects: List[UUID] = Field(default_factory=list, description="Project IDs the user has contributed to")  # UUID references for strict matching, may map to foreign keys in DB
    github_url: Optional[HttpUrl] = Field(None, description="GitHub profile URL (optional)")

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "b8a8f9cc-04e4-4e6f-9e10-d0544b25e2f3",
                "username": "codewizard",
                "skills": ["python", "fastapi"],
                "interests": ["ai", "education"],
                "starred_projects": ["b8a8f9cc-04e4-4e6f-9e10-d0544b25e2f3"],
                "contributed_projects": ["c2cdb238-3030-4c86-bca7-85c13f1eb3f2"],
                "github_url": "https://github.com/codewizard"
            }
        }



class Project(BaseModel):
    """
    API schema representing an open-source project.
    Designed for future database mapping with strict UUID relationships.
    """
    id: UUID = Field(..., description="Unique project identifier")
    name: str = Field(
        ..., 
        min_length=2, 
        max_length=100, 
        description="Project name (2-100 chars)")
    description: Optional[str] = Field(None, description="Brief description of the project")
    tags: List[str] = Field(default_factory=list, description="List of technologies/tags relevant to the project")
    contributors: List[UUID] = Field(default_factory=list, description="List of user IDs (UUID) who have contributed")  # UUID references for strict matching, may map to foreign keys in DB
    github_url: Optional[HttpUrl] = Field(None, description="Link to the project's GitHub repo (optional)")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "b8a8f9cc-04e4-4e6f-9e10-d0544b25e2f3",
                "name": "FastAPI Recommender",
                "description": "A tool to recommend open source projects to developers.",
                "tags": ["python", "fastapi", "ml"],
                "contributors": ["b8a8f9cc-04e4-4e6f-9e10-d0544b25e2f3", "c2cdb238-3030-4c86-bca7-85c13f1eb3f2-dev"],
                "github_url": "https://github.com/someuser/fastapi-recommender"
            }
        }