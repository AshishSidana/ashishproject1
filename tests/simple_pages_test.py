"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'aria-current="page" href="/">Home</a>' in response.data
    assert b'aria-current="page" href="/git">Git</a>' in response.data
    assert b'aria-current="page" href="/docker">Docker</a>' in response.data
    assert b'aria-current="page" href="/python">Python</a>' in response.data
    assert b'aria-current="page" href="/ci-cd">CI/CD</a>' in response.data

def test_request_index(client):
    """This makes the index/home page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data

def test_request_git(client):
    """This makes the Git page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_docker(client):
    """This makes the docker page"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b"Python" in response.data

def test_request_python(client):
    """This makes the python page"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b"Python" in response.data

def test_request_ci_cd(client):
    """This makes the CI/CD page"""
    response = client.get("/ci-cd")
    assert response.status_code == 200
    assert b"CI/CD" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/testpage")
    assert response.status_code == 404