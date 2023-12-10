from django.urls import path
from .views import CreateAccountView, UserAccountView

app_name ='users'
urlpatterns =[
    path('create-account/', CreateAccountView.as_view (),
    name='createAccount'),
    path('my-profile/<int:pk>/', UserAccountView.as_view (),
    name='my-profile')
]