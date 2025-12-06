import pytest

#archivo fixture donde tengo los datos de test

@pytest.fixture
def api_url():
    return "https://jsonplaceholder.typicode.com/"  # se usa web place order 

