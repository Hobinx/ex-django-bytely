from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404, render
from .models import BytelyURL
from .forms import SubmitUrlForm


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm()
        context = {
            'title': 'Submit URL',
            'form': form
        }
        return render(request, 'shortener/home.html', context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        if form.is_valid():
            pass
        context = {
            'form': form
        }
        return render(request, 'shortener/home.html', context)


class BytelyRedirectView(View):

    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(BytelyURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
