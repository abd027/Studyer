from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.loginUser, name="login"),
    path('signup/', views.signupUser, name="signup"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    path('user-profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('update-user', views.updateUser, name="update-user"),
    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity")
]
