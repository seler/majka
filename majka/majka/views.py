from django.views.generic import RedirectView


class HomeView(RedirectView):
    url = "/blog/"
    permament = False

home = HomeView.as_view()
