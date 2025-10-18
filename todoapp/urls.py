from django.urls import path,include
from . import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),         # Sign up page
    path('login/', views.log_in, name='login'),       # Login page
    path('logout/', views.log_out, name='logout'),    # Logout
    path('', views.add_task, name='add_task'),            # Home page (requires login)
    path('delete/<int:task_id>/',views.delete_task,name='delete')
]
