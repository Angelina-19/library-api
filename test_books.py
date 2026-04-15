def test_simple_check(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"status": "ok"}
git add .
git commit -m "Add second test for PR check"
git push https://Angelina-19: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@github.com/Angelina-19/library-api.git feature-new-test
git checkout -b feature-new-test
cat <<EOF >> test_books.py
def test_another_check():
    assert 1 + 1 == 2
