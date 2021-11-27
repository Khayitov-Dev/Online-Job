from django.urls import path
from .views import(
    index,admin_login,user_login,
    recruiter_login,user_signup,
    user_home,Logout,recruiter_signup,
    recruiter_home,admin_home,view_users,
    delete_user,recruiter_pending
)


urlpatterns = [
    path('',index,name='index'),
    path('admin_login/',admin_login,name='admin_login'),
    path('user_login/',user_login,name='user_login'),
    path('recruiter_login/',recruiter_login,name='recruiter_login'),
    path('user_signup/',user_signup,name='user_signup'),
    path('user_home/',user_home,name='user_home'),
    path('logout/',Logout,name='logout'),
    path('recruiter_signup/',recruiter_signup,name='recruiter_signup'),
    path('recruiter_home/',recruiter_home,name='recruiter_home'),
    path('admin_home/',admin_home,name='admin_home'),
    path('view_users/',view_users,name='view_users'),
    path('delete_user/<int:pk>/',delete_user,name='delete_user'),
    path('recruiter_pending/',recruiter_pending,name='recruiter_pending'),
]