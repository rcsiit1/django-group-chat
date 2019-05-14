from django.urls import path, include
from . import views

urlpatterns=[
    
    path('save/',views.save,name='save'),
	path('login/',views.login,name='login'),
	path('register_redirect/',views.register_redirect,name='register_redirect'),
	path('',views.register,name='register'),
	path('after_login/',views.after_login,name='after_login'),
	path('check_user/',views.check_user,name='check_user'),
	path('logout/',views.logout,name='logout'),
	path('navigation/',views.navigation,name='navigation'),
	path('chat/',views.chat,name='chat'),
	path('chat_sender/',views.chat_sender,name='chat_sender'),
	path('fetch/',views.fetch,name='fetch'),
	path('room/',views.room,name='room'),
	path('selectRoom/',views.selectRoom,name='selectRoom'),
	

	
	
	#temp testing
	path('test/',views.test,name='test'),
	path('check_login/',views.check_login,name='check_login'),
]