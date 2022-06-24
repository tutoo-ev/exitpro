from django.urls import path, include
# from rest_framework.routers import DefaultRouter


from .views import RegisterAPIView, UsersListView, UserRetrieveUpdateDeleteView, \
    UserUpdateView, UserTypeDetailAPIView, LogoutAPIView, UserDepartmentUpdateView, UserAttritionRetrieveUpdateView, \
    UserAttritionHRRetrieveUpdateView, UserAttritionICTRetrieveUpdateView


# router = DefaultRouter()
# router.register('api', UserViewSet, basename='create_user')

urlpatterns = [
    # path('', include(router.urls)),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('', UsersListView.as_view(), name='all_users'),
    path('<int:pk>', UserRetrieveUpdateDeleteView.as_view(), name='single_user'),
    # path('user/<int:pk>', UserUpdateView.as_view(), name='update_user'),
    path('user_type/<int:pk>', UserTypeDetailAPIView.as_view(), name='update_user_type'),
    path('user_department/<int:pk>', UserDepartmentUpdateView.as_view(), name='update_user_department'),
    path('attrition/<int:pk>', UserAttritionRetrieveUpdateView.as_view(), name='user_attrition_update'),
    path('hr/<int:pk>', UserAttritionHRRetrieveUpdateView.as_view(), name='user_attrition_HR_update'),
    path('ict/<int:pk>', UserAttritionICTRetrieveUpdateView.as_view(), name='user_attrition_ICT_update'),

    path('logout', LogoutAPIView.as_view(), name='logout')

]

