from django.urls import path
from .views import index, user, reaction
from .controller import reaction_controller

app_name = 'match'

urlpatterns = [
    path('', index.top, name='index'),
    path('users/regist/', user.regist, name='regist'),
    path('login/', index.Login.as_view(), name='login'),
    path('logout/', index.Logout.as_view(), name='logout'),
    path('users/', user.gets, name='users'),
    path('users/profile/<int:user_id>', user.profile, name='profile'),
    path('users/profile/<int:user_id>/edit/', user.edit, name='profile_edit'),
    path('reactions/', reaction_controller.create, name='reactions'),
    path('matching/', reaction.matching, name='matching'),
]
