# from typing import Any
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from news.models import NewsStory

class CreateAccountView (CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user/createAccount.html'

class UserAccountView(generic.DetailView):
    model = CustomUser
    template_name = 'user/my-profile.html'
    context_object_name = 'user'
    fields = ["first_name", "last_name" , "email", "profile_pic", "username", "about"]

    def get_context_data(self, **kwargs ) :
        context = super().get_context_data(**kwargs)
        context['user_stories']=NewsStory.objects.filter(author=self.kwargs['pk'])
        return context