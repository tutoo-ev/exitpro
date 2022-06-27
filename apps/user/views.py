"""

from django.contrib.auth.hashers import make_password
from django.shortcuts import render

# from rest_framework import viewsets, status, mixins, generics
from rest_framework.decorators import action
from rest_framework.response import Response


# from apps.user.models import User
from apps.user.serializers import CreateUserSerializer, UserViewSerializer
from django.shortcuts import get_object_or_404

#
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = CreateUserSerializer
#
#     @action(detail=False, methods=['post'])
#     def create_user(self, request, *args, **kwargs):
#         serializer = CreateUserSerializer(data=request.data)
#         if serializer.is_valid():
#             user_obj = serializer.save(password=make_password(serializer.validated_data['password']))
#             custom_data = {
#                 "status": True,
#                 "message": 'User created successfully.',
#             }
#             return Response(custom_data, status=status.HTTP_200_OK)
#         else:
#             custom_data = {
#                 "status": False,
#                 "message": serializer.errors,
#             }
#             return Response(custom_data, status=status.HTTP_400_BAD_REQUEST)
#
#
#
#
#
#
# class UsersListCreateView(mixins.ListModelMixin,
#                            mixins.CreateModelMixin,
#                            generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = CreateUserSerializer
#
#     def post(self, request, *args, **kwargs):
#
#         return self.create(request, *args, **kwargs)
#
#
"""


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import CreateUserSerializer, UserViewSerializer, SingleUserSerializer, UserTypeUpdateSerializer, \
    UserDepartmentUpdateSerializer, UserAttritionDetailSerializer, UserAttritionHRSerializer, \
    UserAttritionICTSerializer
from .permissions import IsHR, IsAdmin, IsEmployee


class RegisterAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, format=None):
        """Creates/ registers a user"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # token generation
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
                }
            # we are sending token instead of serialized data
            # serializer_data = serializer.data
            return Response(response_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UsersListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserViewSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """Lists out all the users"""
        return self.list(request, *args, **kwargs)


class UserUpdateView(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


    def get(self, request, *args, **kwargs):
        """Retrieves a user based on a given id (pk)"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Updates a user based on the given id (pk) """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
        return self.update(request, *args, **kwargs)


class UserDepartmentUpdateView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserDepartmentUpdateSerializer
    permission_classes = [IsAuthenticated, IsHR]


    def get(self, request, *args, **kwargs):
        """Retrieves a user's department details based on a given id (pk)"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Updates a user's department details based on the given id (pk) """
        return self.update(request, *args, **kwargs)


class UserRetrieveUpdateDeleteView(mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin,
                                   generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = SingleUserSerializer
    permission_classes = [IsAuthenticated, IsHR]


    def get(self, request, *args, **kwargs):
        """Retrieves a user  detail based on a given id (pk)"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Updates a user detail based on the given id (pk)"""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Deletes a user based on the particular id (pk)"""
        return self.destroy(request, *args, **kwargs)


class UserTypeDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserTypeUpdateSerializer
    permission_classes = [IsAuthenticated, IsHR]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserTypeUpdateSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserTypeUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    def post(self, request, format = None):
        """Accepts the 'refresh_token' and blacklists it."""
        # Details from jwt settings
        try:
            refresh_token = request.data.get('refresh_token')
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist()
            return Response({'message':'successfully logged out'},status= status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserAttritionRetrieveUpdateView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserAttritionDetailSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


    def get(self, request, *args, **kwargs):
        """Retrieves a user's attrition details based on a given id (pk)"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Updates a user's attrition details based on the given id (pk) """
        return self.update(request, *args, **kwargs)


class UserAttritionHRRetrieveUpdateView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserAttritionHRSerializer
    permission_classes = [IsAuthenticated, IsHR]


    def get(self, request, *args, **kwargs):
        """Retrieves a user's attrition ICT details based on a given id (pk)"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Updates a user's attrition ICT details based on the given id (pk) """
        return self.update(request, *args, **kwargs)


class UserAttritionICTRetrieveUpdateView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserAttritionICTSerializer
    permission_classes = [IsAuthenticated, IsHR]

    def get(self, request, *args, **kwargs):
        """Retrieves a user's attrition ICT details based on a given id (pk)"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Updates a user's attrition ICT details based on the given id (pk) """
        return self.update(request, *args, **kwargs)

