from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from .models import Comments

class comment(LoginRequiredMixin, CreateView):
    model = Comments
    fields = ['comment']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
