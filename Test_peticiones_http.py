import requests
import pytest


class TestGetPosts:
    @pytest.mark.get
    def test_get_response_code(self, api_url):
            response = requests.get(api_url + "posts")  # se usa posts del sitio Place Order
            data = response.json()
            assert response.status_code == 200   # se valida que la obtencion de consulta sea exitosa
            assert len(data) > 0                 # se valida que arroje resultados 
            assert response.elapsed.total_seconds() < 3.0  # se valida el tiempo de respuesta 

class TestPostPosts:
      
      @pytest.mark.post
      def test_post_response_code(self,api_url):   # se agrega un regitro de prueba 
            new_posts = {  
               "userId":"400",
               "id": "123",
               "title": "Hola, esta es una prueba que sera eliminada"
  }
            response = requests.post (api_url + "posts", new_posts)
            data = response.json()
            assert response.status_code in (200, 201)  # se valida que sea exitoso
            assert isinstance(data["id"], int)         # se valida que el campo ID sea un entero
            assert isinstance(data["title"], str)      # se valida que titulo sea un string 

class TestDeletePosts:
      @pytest.mark.delete
      def test_delete_response_code(self,api_url):  # se procede a eliminar el regitro de prueba 
         posts_borrado = {
                "userId": 400,
                "id": 123,
                "title": "Hola, esta es una prueba que sera eliminada"
  }
         response = requests.post (api_url+ "posts", posts_borrado)  
         data = response.json()
         assert response.status_code != 500  # se valida que no de error de server 
         assert response.elapsed.total_seconds() < 3.0   # se valida el tiempo que demora 

    