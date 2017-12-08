from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404, render
from .models import BytelyURL


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', {})


class BytelyRedirectView(View):

    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(BytelyURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
