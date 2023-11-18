from django import forms
from .tasks import sending_review_email_task


class EmailForm(forms.Form):
    name = forms.CharField(label='name', max_length=60)
    email = forms.EmailField(label='email')
    review = forms.CharField(label='review', max_length=500, widget=forms.Textarea)

    def send_email(self):
        sending_review_email_task.apply_async(
            (self.cleaned_data['name'], self.cleaned_data['email'], self.cleaned_data['review']),
            countdown=2
        )
