from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_removes_email():
    response = client.delete(
        "/activities/Chess%20Club/unregister?email=michael@mergington.edu"
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Unregistered michael@mergington.edu from Chess Club"

    get_response = client.get("/activities")
    activities = get_response.json()
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]

    # restore state for later tests
    activities["Chess Club"]["participants"].append("michael@mergington.edu")
