from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article

# Article app views.

""" Get list of all aricles """
class ArticleListView(ListView):
    model = Article
    template_name = 'articles/articles_list.html'


""" GET specific article with article id """
class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_detail.html"


""" POST (edit) specific article with article id """
class ArticleEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'summary', 'body', 'photo')
    template_name = "articles/article_edit.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


""" POST (delete) specific aritcle with article id """
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "articles/article_delete.html"
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


""" POST (create) article """
class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView,):
    model = Article
    fields = ('title', 'summary', 'body', 'photo',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

    template_name = "articles/article_create.html"