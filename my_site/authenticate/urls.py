from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('login/', views.login_user, name ='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('add_post/', views.add_post, name='add_post'),
    path('nopermission/', views.no_permission, name='no_permission'),
    path('savepost/', views.save_post, name='savepost'),
    path('showpost/', views.show_post, name='showpost'),
    path('add_finance/', views.add_finance, name='addfinance'),
    path('save_finance/', views.save_finance, name='savefinance'),
    path('showfinance/', views.show_finance, name='showfinance'),
]

