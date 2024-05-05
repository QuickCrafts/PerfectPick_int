import json
from spyne import Application, rpc, ServiceBase, Iterable, ComplexModel, Integer, Unicode, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import requests

class Book(ComplexModel):
    idBook = Unicode
    author = Unicode
    genres = Unicode
    pages = Integer
    rating = Float
    title = Unicode
    year = Integer
    typename = Unicode

class solicitudSOAP(ServiceBase):
    @rpc(_returns=Iterable(Book))
    def getBooks(self):
        # Construir la solicitud GraphQL
        url = 'http://localhost:9000/graphql'
        headers = {'Content-Type': 'application/json'}
        query = '''
        query{
          GetBooks{
            idBook
            author
            genres
            pages
            rating
            title
            year
            __typename
          }
        }
        '''
        url +=  '?query=' + query
        # Enviar la solicitud GraphQL
        response = requests.get(url ,headers=headers)

        # Devolver la respuesta como un string
        response_json = response.json()
        return [Book(**book) for book in response_json['data']['GetBooks']]

# Crear la aplicación SOAP
application = Application([solicitudSOAP], 'http://example.com/bookservice',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

# Crear el servidor WSGI
wsgi_application = WsgiApplication(application)

# Ejecutar el servidor en el puerto 8082
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    port = 7777
    server = make_server('0.0.0.0', port, wsgi_application)
    print("Servidor en", port)
    server.serve_forever()