from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AndroidAppSerializer

from rest_framework import generics, mixins, permissions, authentication


from .models import AndroidApp


# Create your views here.
# @api_view(["POST"])
# def app_view(request):
#     # instance = AndroidApp.objects.all().order_by("?").first()
#     serializer = AndroidAppSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         return Response(serializer.data)
    
class AndroidAppDetailApiView(generics.RetrieveAPIView):
    queryset = AndroidApp.objects.all()
    serializer_class = AndroidAppSerializer

class AndroidAppListCreateApiView(generics.ListCreateAPIView):
    queryset = AndroidApp.objects.all()
    serializer_class = AndroidAppSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.SessionAuthentication]

    def perform_create(self, serializer):
        serializer.save()
    # lookup_field = 

class AndroidAppUpdateApiView(generics.UpdateAPIView):
    queryset = AndroidApp.objects.all()
    serializer_class = AndroidAppSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()
        # return super().perform_update(serializer)

class AndroidAppDestroyApiView(generics.DestroyAPIView):
    queryset = AndroidApp.objects.all()
    serializer_class = AndroidAppSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


# class AndroidAppMixinView(mixins.CreateModelMixin, mixins.ListModelMixin,
#         mixins.RetrieveModelMixin,
#         generics.GenericAPIView
# ):
#     queryset = AndroidApp.objects.all()
#     serializer_class = AndroidAppSerializer
#     lookup_field = 'pk'

#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get("pk")
#         if pk:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

