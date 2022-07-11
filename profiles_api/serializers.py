from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    '''serializa un campo para probar nuestra apiview '''
    
    name = serializers.CharField(max_length=50)
    ## una vez ya creado nuestro serializador, podemos pasar a crear nuestro método post 
        # esto lo hacemos en views.py
    
    
    