from uuid import uuid4
from random import sample
from my_recommender.models.models import User, Project


usernames = ["codewizard", "snekking-dev", "bughunter", "algomancer", "fastapifan"]
all_skills = ["python", "fastapi", "docker", "ml", "nlp", "sql", "pandas"]
all_interests = ["ai", "web", "infra", "education", "health"]
all_tags = ["python", "fastapi", "ml", "web", "devops"]


def generate_fake_users(n=5) -> list[User]:
    """
    Generate a random fake user.
    
    Args:
        n (int): number of user to create
    
    Returns:
        users (list[User]): list of random generated users
    """ 
    users = []

    for name in usernames[:n]:
        user = User(
            user_id=uuid4(),
            username=name,
            skills=sample(all_skills, k=2),
            interests=sample(all_interests, k=2),
            starred_projects=[],
            contributed_projects=[],
            github_url=f"https://github.com/{name}", 
        )

        users.append(user)

    return users


def generate_fake_projects(n=5, user_list=None) -> list[Project]:
    """
    Generate random user projects. 
    
    Args:
        n (int): number of projects 
        user_list (list[User]): a list of users
    
    Returns:
        projects (list[Project]): list of random generated projects
    """ 
    projects = []
    
    for i in range(n):
        project_name = f"Project {i}"
        description = f"Description for {project_name}"
        chosen_user = sample(user_list, k=2)

        project = Project(
                id=uuid4(),
                name=project_name,
                description=description,
                tags=sample(all_tags, k=2),
                contributors=[user.user_id for user in chosen_user],
                github_url=f"https://github.com/{project_name.lower().replace(' ', '-')}"
        )

        projects.append(project)

    return projects        


if __name__ == "__main__":
    users = generate_fake_users()
    projects = generate_fake_projects(user_list=users)
    print(f"Fake Users: {users}")  
    print(f"Fake Projects: {projects}")  


