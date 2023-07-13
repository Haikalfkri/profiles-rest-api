from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloAPiView(APIView):
    """Test API View"""
    
    def get(self, request, format=None):
        """Returns a list of APIView featues"""
        an_apiview = [
            'Uses HTTP Methods',
            'Is similiar with traditional django',
            'Gives you the most control',
            'Is mapped manually to URLs',
        ]
        
        return Response(
            {
                'message':'Hello!', 
                'an_apiview': an_apiview,
            }
        )