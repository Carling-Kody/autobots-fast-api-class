import requests

def test_math():
    assert 2 + 2 == 4

def test_get_todos():
    response = requests.get("https://df-flask-todo-api-class.herokuapp.com/todos")
    assert response.status_code == 200

def test_add_todo():
    pass

def test_delete_todo():
    pass

def test_mark_todo_complete():
    pass
