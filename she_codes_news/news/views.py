
from django.views import generic,  View
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm

from typing import Any
from django.db.models.query import QuerySet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from collections import defaultdict


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_stories'] = NewsStory.objects.all()[:4]
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        return context

class StoryView(generic.DetailView):
    model=NewsStory
    template_name='news/story.html'
    context_object_name='story'

class AddStoryView (generic.CreateView):
    form_class=StoryForm
    context_object_name='storyform'
    template_name='news/createStory.html'
    success_url=reverse_lazy('news:index')

    def form_valid (self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class SearchView(View):
    template_name = 'news/authorSearch.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        news_results = NewsStory.objects.filter(author__username__icontains=query)

        # Grouping news stories by author
        grouped_news = defaultdict(list)
        for news in news_results:
            grouped_news[news.author.username].append(news)
        
        context = {
            'news_results': news_results,
            'query': query,
        }

        return render(request, self.template_name, context)
