from django.views.generic.edit import FormView
from .forms import EmailForm

from django.http import HttpResponse


class ReviewEmailView(FormView):
    template_name = 'review.html'
    form_class = EmailForm

    def form_valid(self, form):
        form.send_email()
        msg = 'Thanks for your review'
        return HttpResponse(msg)
