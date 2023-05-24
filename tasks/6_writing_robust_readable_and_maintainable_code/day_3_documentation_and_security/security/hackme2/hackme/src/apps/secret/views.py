from django.views.generic import TemplateView


class SecretView(TemplateView):
    template_name = "secret.html"
