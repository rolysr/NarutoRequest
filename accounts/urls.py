from accounts.views import RegisterUser
from django.urls import path

app_name='accounts'
urlpatterns = [
	path('register/', RegisterUser.as_view(), name="register"),
]
