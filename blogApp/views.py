from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import BlogPost


class NewPost(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title', 'body', 'image']
    template_name = 'blogApp/newPost.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class AllPost(ListView):
    model = BlogPost
    template_name = 'blogApp/blog.html'
    context_object_name = 'post'
    ordering = ['-createdAt']

class Index(TemplateView):
    template_name='blogApp/index.html'

class Gallery(TemplateView):
    template_name='blogApp/gallery.html'

class About(TemplateView):
    template_name='blogApp/about.html'
    
class Agriculture(TemplateView):
    template_name='blogApp/agriculture.html'

class Contact(TemplateView):
    template_name='blogApp/contact.html'

class Donate(TemplateView):
    template_name='blogApp/donate.html'

class Ecology(TemplateView):
    template_name='blogApp/ecology.html'

class Portfolio(TemplateView):
    template_name='blogApp/portfolio.html'

class Social(TemplateView):
    template_name='blogApp/social.html'

class Child(TemplateView):
    template_name='blogApp/child.html'


class DetailPost(DetailView):
    model = BlogPost
    template_name = 'blogApp/detailPost.html'
    context_object_name = 'post'


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'body', 'image']
    template_name = 'blogApp/newPost.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blogPost = self.get_object()
        if self.request.user == blogPost.author:
            return True
        return False


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    success_url = '/'
    template_name = 'blogApp/confirmDelete.html'

    def test_func(self):
        blogPost = self.get_object()
        if self.request.user == blogPost.author:
            return True
        return False
