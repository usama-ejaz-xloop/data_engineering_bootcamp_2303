from django.views.generic import CreateView
from .models import TODOItem


class HomepageView(CreateView):
    model = TODOItem
    template_name = "index.html"
    fields = ["content"]

    def get_success_url(self):
        return "/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        filter_name = self.request.GET.get("filter", "all")
        context["filter"] = filter_name

        if filter_name == "all":
            context["todo_items"] = TODOItem.objects.all()
        elif filter_name == "long":
            context["todo_items"] = TODOItem.objects.filter(content__regex=r".{100}.*")
        else:
            assert False
        return context
