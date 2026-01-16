from fastapi import APIRouter
from typing import Optional
from app.utility.github_client import  search_repositories
from app.utility.popularity_score import compute_score


router = APIRouter(prefix="/urls", tags=["urls-v1"])

@router.get("/popular")
def get_popular_repos(language: Optional[str] = None, created_after: Optional[str] = None):
    print("I am here")
    try:
        repos = search_repositories(language, created_after)
        # print(len(repos))
        return [
            {
                "name": r["name"],
                "owner": r["owner"]["login"],
                "stars": r["stargazers_count"],
                "forks": r["forks_count"],
                "score": compute_score(r),
            }
            for r in repos
        ]
    except Exception as e:
        # print(str(e))
        return [{"Error": "Something went wrong"}]

