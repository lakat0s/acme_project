from django.http import HttpResponse, HttpResponseNotFound
from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'birthday'

@login_required
def simple_view(request):
    return HttpResponse('Страница для залогиненных пользователей!')

urlpatterns = [
    path('', views.BirthdayCreateView.as_view(), name='create'),
    path('list/', views.BirthdayListView.as_view(), name='list'),
    path('<int:pk>/', views.BirthdayDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.BirthdayUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.BirthdayDeleteView.as_view(), name='delete'),
    #path('login_only/', views.simple_view),
    path('<int:pk>/comment/', views.add_comment, name='add_comment'),
]
