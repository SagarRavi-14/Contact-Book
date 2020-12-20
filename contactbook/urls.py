from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),   
    path('dashboard/',views.dashboard, name='dashboard'),
    path('addcontact/',views.addcontact, name='addcontact'),
    path('update/<int:myid>/',views.update, name='update'),
    path('delete/<int:id>/',views.detail_delete, name='detail_delete'),
     path('confirmdelete/<int:id>',views.confirm_delete, name='confirm_delete'),
    path('search/',views.search, name='search'),
    path('signup/',views.handleSignup, name='handleSignup'),
    path('login/',views.handleLogin, name='handleLogin'),
    path('logout/',views.handleLogout, name='handleLogout'),
]

