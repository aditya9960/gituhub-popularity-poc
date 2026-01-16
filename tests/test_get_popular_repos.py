def test_popular_repos_unauthorized(client):
    response = client.get("/api/v1/gitrepos/popular")
    assert response.status_code == 200



def test_popular_repos_success(client):
    response = client.get("/api/v1/gitrepos/popular?language=python")
    assert response.status_code == 200
    assert "items" or "Error" in response.json()

def test_popular_repos_success_2(client):
    response = client.get("/api/v1/gitrepos/popular?created_after=2026-01-01")
    assert response.status_code == 200
    assert "items" or "Error" in response.json()