from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import BaseFormView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea
        }

class PostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = PostForm
    model = Post
    template_name = 'guestbook/post.html'
    #fields = ['comment']
    success_url = reverse_lazy('guestbook:index')
    def form_valid(self, form):
        # Set the form's author to the submitter if the form is valid
        form.instance.author = self.request.user
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

def index(request):
    posts = Post.objects.all().order_by('-date')
    context = {"posts": posts}
    return render(request, 'guestbook/index.html', context)


# Create guestbook/urls.py with the following content:
from django.urls import path

from . import views

app_name = 'guestbook'
urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.PostView.as_view(), name='post'),
]
