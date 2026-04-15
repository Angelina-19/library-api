def test_simple_check(client):
    response = client.get('/')
    assert response.status_code == 200

def test_another_check():
    assert 1 + 1 == 2
