from django.urls import path
from viewer import views

app_name = 'viewer'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('main/', views.MainPageView, name='main_page'),
    path('main/cases/<str:organsystem_name>/', views.CasesView, name='cases_page'),
    path('main/cases/<str:organsystem_name>/<int:case_id>/', views.wsi, name='wsi'),
    path('register/', views.registration, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.upload, name='upload')
]

