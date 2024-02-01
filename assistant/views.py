from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserSpeechView(APIView):
    def post(self, request, *args, **kwargs):
        user_text = request.data.get('text', None)

        if not user_text:
            return Response({"error": "Texto não fornecido."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"received_text": user_text}, status=status.HTTP_200_OK)
    
