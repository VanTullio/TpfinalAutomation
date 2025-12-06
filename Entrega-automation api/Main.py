import requests

URL_API = "https://jsonplaceholder.typicode.com/"


def get_posts():
     print("Mostrando todos los posts")
    
     response = requests.get(URL_API + "posts") 
    
     print(response.status_code)
    
     data = response.json()
     print(data)

def post_posts():
     print("Crear nuevo registro posts")

     new_posts =  {
    "userId": 400,
    "id": 123,
    "title": "Hola, esta es una prueba que sera eliminada"
  }
     response = requests.post (URL_API + "posts", new_posts)
     print(response)
     data = response.json()
     print(data)
     
     
def delete_posts():
     print("Borrando el registro posts de prueba")

     posts_borrado = {
    "userId": 400,
    "id": 123,
    "title": "Hola, esta es una prueba que sera eliminada"
  }
     response = requests.post (URL_API + "posts", posts_borrado)
     print(response)
     data = response.json()
     print(data)
     print("Quedo eliminado")


get_posts()
post_posts()
delete_posts()



