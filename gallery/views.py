from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from .forms import UploadForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import BaseFormView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from .models import Post

def display_images(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'gallery/index.html', {'posts' : posts})

def image_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery:success')
    else:
        form = UploadForm()
    return render(request, 'gallery/upload.html', {'form' : form})


def success(request):
    return render(request, 'gallery/success.html', {})
