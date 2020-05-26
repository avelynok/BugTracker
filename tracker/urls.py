from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginview, name='loginview'),
    path('addbug/<int:id>', views.addBug, name='addbug'),
    path('buginfo/<int:id>', views.buginfo, name='buginfo'),
    path('authorinfo/<int:id>', views.AuthorInfo, name='authorinfo'),
    path('inprogress/edit/<int:id>', views.InProgress, name='inprogress'),
    path('done/edit/<int:id>', views.Done, name='done'),
    path('invalid/edit/<int:id>', views.Invalid, name='invalid'),
    path('editbug/edit/<int:id>', views.EditBug, name='edit'),
    path('logout/', views.logoutview, name='logoutview')
]