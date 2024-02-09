"""Views for api app"""
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from api.models import Game,GameDeveloper
from api.serializers import GameSerializer,GameDeveloperSerializer


# Create your views here.

class GameView(APIView):
    """Game view"""
    serializer = GameSerializer
    queryset = Game.objects.filter(deleted_at=None)

    def get(self,request: Request, game_id=None) -> Response:
        """Get all Games"""


    def post(self,request: Request) -> Response:
        """Create Game"""


    def delete(self,request: Request, game_id) -> Response:
        """delete game"""

class GameDeveloperView(APIView):
    """Game Developer view"""
    serializer = GameDeveloperSerializer
    queryset = GameDeveloper.objects.all()

    def get(self,request: Request,game_developer_id: int = None) -> Response:
        """Get all Game Developers"""
        results = None

        if game_developer_id:
            try :
                results = GameDeveloper.objects.get(id=game_developer_id)
                serializer = self.serializer(results,many=False)
                return Response({
                    "status":"ok",
                    "data":serializer.data
                },status=status.HTTP_200_OK)
            except GameDeveloper.DoesNotExist:
                return Response({
                    "status":"not found",
                    "data":[]
                },status=status.HTTP_404_NOT_FOUND)

        results = GameDeveloper.objects.filter(deleted_at=None)

        serializer = self.serializer(results,many=True)

        return Response({
            "status":"ok",
            "data":serializer.data
        },status=status.HTTP_200_OK)

    def post(self,request: Request) -> Response:
        """Create Game Developer"""

        serializer = GameDeveloperSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "status":"created",
                "data":serializer.data
            },status=status.HTTP_201_CREATED)

        return Response({
            "status":"bad request",
            "data":serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)

    def put(self,request: Request, game_developer_id: int) -> Response:
        """Update Game Developer"""
        try:
            results = GameDeveloper.objects.get(id=game_developer_id)
        except GameDeveloper.DoesNotExist:
            return Response({
                "status":"not found",
                "data":[]
            },status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer(results,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "status":"updated",
                "data":serializer.data
            },status=status.HTTP_200_OK)

        return Response({
            "status":"bad request",
            "data":serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request:Request,game_developer_id: int) -> Response:
        """Delete Game Developer"""

        try:
            results = GameDeveloper.objects.get(id=game_developer_id)
        except GameDeveloper.DoesNotExist:
            return Response({
                "status":"not found",
                "data":[]
            },status=status.HTTP_404_NOT_FOUND)


        if request.data.get("soft_delete"):
            results.soft_delete()
        else:
            results.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
