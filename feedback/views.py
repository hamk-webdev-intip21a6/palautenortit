from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls.base import reverse_lazy
from .models import Feedback
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from collections import Counter

@login_required
def index_success(request):
    return render(request, "feedback/index_success.html")

class FeedbackCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Feedback
    fields = ['topic', 'rating', 'good', 'bad', 'ideas']
    template_name = "feedback/index.html"
    success_url = reverse_lazy('feedback:index_success')

    def form_valid(self, form):
        feedback = form.save(commit=False)
        feedback.user = self.request.user
        try:
            feedback.validate_unique()
            return super().form_valid(form)
        except ValidationError:
            form.add_error(None, "You have already submitted feedback for this topic.")
            return self.form_invalid(form)

