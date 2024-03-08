from rest_framework.views import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.viewsets import ViewSet

from app.models import Menu
from app.serializers.MenuSerializer import MenuSerializer


class MenuViewSet(ViewSet):

    def list(self, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True).data

        return Response({'data': serializer}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        menu = get_object_or_404(Menu, pk=pk)
        serializer = MenuSerializer(menu).data
        return Response({'data': serializer}, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = MenuSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(**serializer.validated_data)

        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        menu = get_object_or_404(Menu, pk=pk)
        serializer = MenuSerializer(menu, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(**serializer.validated_data)

        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        menu = get_object_or_404(Menu, pk=pk)
        menu.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
