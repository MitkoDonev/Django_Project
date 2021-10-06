from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection

from django.views.generic.edit import FormView


class ContactForm(forms.Form):
    your_name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(required=False, label="Your Email Address")
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


class ContactUs(FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = "/contact/?submitted=True"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        if "submitted" in request.GET:
            context["title"] = request.GET["submitted"]

        return self.render_to_response(context)

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        connection = get_connection("django.core.mail.backends.console.EmailBackend")
        subject = cleaned_data["subject"]
        message = cleaned_data["message"]
        send_mail(
            subject,
            message,
            cleaned_data.get("email", "noreply@example.com"),
            ["donev90@gmail.com"],
            connection=connection,
        )
        return super().form_valid(form)


# def contact(request):
#     submitted = False

#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             connection = get_connection(
#                 "django.core.mail.backends.console.EmailBackend"
#             )
#             subject = cleaned_data["subject"]
#             message = cleaned_data["message"]

#             send_mail(
#                 subject,
#                 message,
#                 cleaned_data.get("email", "noreply@example.com"),
#                 ["donev90@gmail.com"],
#                 connection=connection,
#             )

#             return HttpResponseRedirect("/contact?submitted=True")
#     else:
#         form = ContactForm()
#         if "submitted" in request.GET:
#             submitted = True

#     return render(
#         request, "contact/contact.html", {"form": form, "submitted": submitted}
#     )
