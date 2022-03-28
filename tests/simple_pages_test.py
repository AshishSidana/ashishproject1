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
    assert b'aria-current="page" href="/glossary">Glossary</a>' in response.data
    assert b'aria-current="page" href="/aaa-testing">AAA</a>' in response.data
    assert b'aria-current="page" href="/oops">OOPs</a>' in response.data
    assert b'aria-current="page" href="/solid">SOLID</a>' in response.data

def test_request_index(client):
    """This makes the index/home page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data

def test_request_about(client):
    """This makes the index/home page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"About" in response.data

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

def test_request_glossary(client):
    """This makes the glossary page"""
    response = client.get("/glossary")
    assert response.status_code == 200
    assert b"Glossary" in response.data

def test_request_aaa(client):
    """This makes the aaa testing page"""
    response = client.get("/aaa-testing")
    assert response.status_code == 200
    assert b"AAA" in response.data

def test_request_oops(client):
    """This makes the oops page"""
    response = client.get("/oops")
    assert response.status_code == 200
    assert b"OOPs" in response.data

def test_request_solid(client):
    """This makes the solid page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b"SOLID" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/testpage")
    assert response.status_code == 404
