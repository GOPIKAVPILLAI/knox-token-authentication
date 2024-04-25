from django.urls import path,include
import auth_app.views
from knox import views
urlpatterns = [
   
    path('login/',auth_app.views.LoginView.as_view(), name='knox_login'),
    path('logout/', views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('register/',auth_app.views.CreateUserAPI.as_view()),
    path('view/<int:pk>',auth_app.views.ViewUserAPI.as_view()),
    path('adminview/',auth_app.views.my_view)
#     path('forgot_password/',),
#     path('reset_password/',),
]
