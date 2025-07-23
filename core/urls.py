# urls.py (studentoverflow/urls.py)
# ----------------------------------
from django.contrib import admin
from django.urls import path
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('question/<int:question_id>/', core_views.question_detail, name='question_detail'),
    path('ask/', core_views.ask_question, name='ask_question'),
    path('signup/', core_views.signup_view, name='signup'),
    path('login/', core_views.login_view, name='login'),
    path('logout/', core_views.logout_view, name='logout'),
]
