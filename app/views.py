from rest_framework.views import APIView, Response
from rest_framework.generics import get_object_or_404
from rest_framework import status

from app.models import Menu
from app.serializers.MenuSerializer import MenuSerializer


class MenuAPI(APIView):
    allowed_methods = ['get', 'post', 'put', 'delete']

    def get(self, request):
        if request.data.get('pk'):
            menu = get_object_or_404(Menu, pk=request.data.get('pk'))
            serializer = MenuSerializer(menu).data
            return Response({'data': serializer}, status=status.HTTP_200_OK)

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True).data

        return Response({'data': serializer}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(**serializer.validated_data)

        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

    def put(self, request):
        menu = get_object_or_404(Menu, pk=request.data.get("pk"))
        serializer = MenuSerializer(menu, data=request)
        serializer.is_valid(raise_exception=True)
        serializer.save(**serializer.validated_data)

        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request):
        menu = get_object_or_404(Menu, pk=request.data.get("pk"))
        menu.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
