from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """ Test API View """

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP mehtods as function (get, post, patch, put, delete)',
            'Is similar to a tradition Django View',
            'Give otu the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({
            'message': 'Hello!',
            'an_apiview': an_apiview
        })
