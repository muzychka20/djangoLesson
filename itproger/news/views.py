from dataclasses import fields

from django.db.models import Model
from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('-date') # [:1] # for get one item
    return render(request, 'news/news_home.html', {'news': news, 'test': 'test'}) # HttpResponse("<h4>Hello</h4>")


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'news/delete.html'


def create(request):
    error = ""
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Error"

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/create.html', data)