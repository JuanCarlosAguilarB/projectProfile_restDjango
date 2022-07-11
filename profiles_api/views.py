from rest_framework.views import APIView # esta importación para traer las vistas basadas de APIviews
from rest_framework.response import Response # esta importación para traer los métodos response de http
from rest_framework import status 
from .serializers import HelloSerializer


class HelloApiView(APIView):
    """Esta clase va a ser una clase de una api view de prueba """
    
    serializer_class = HelloSerializer
    
    def get(self,request,format=None) :
        '''Retornar lista de caracteristicas del apiview''' 
        an_apiview = [
            'usamos métodos de HTTP cómo funciones (get,post, push, delete)',
            'es similar a una vista tradicional de Django',
            'Nos da mayor control sobre la lógica de nuestra aplicaución',
            'Está mapeando manualmente a los Urls   '
        ]    
        # cada función HTTP que agreguemos debe retornar un response object
            # este response debe convertir la información en formato json, por lo que esta info 
                #debe ser o bien una lista o un formato json
        return Response({'message':'helo','an_apiview':an_apiview})
    
    # definiendo el método post de la api
    def post(self,request):
        '''crea un mensaje con nuestra api'''
        serializer = self.serializer_class(data=request.data)
        # ya declarado el serializador, debemos ver si este es válido o no 
        if serializer.is_valid():
            name = serializer.validated_data.get('name') ## este name es el que definimos en nuestro seralizer.py
            return Response({'name':name})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
    
    def put(self,request,pk=None):
        '''maneja la actulización de los objetos '''
        return Response({'method':'PUT'})
    def patch(self,request,pk=None):
        '''maneja la actualización parcial de un objeto'''
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        '''manela la supresión de objetos'''
        return Response({'method':'DELETE'})
        
    