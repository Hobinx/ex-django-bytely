from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404, render
from analytics.models import ClickEvent
from .models import BytelyURL
from .forms import SubmitUrlForm
from .utils import absolute_location


class HomeView(View):
    def get(self, request, *args, **kwargs):
        print('get in home')
        form = SubmitUrlForm()
        context = {
            'title': 'Bytely',
            'form': form
        }

        return render(request, 'shortener/home.html', context)

    def post(self, request, *args, **kwargs):
        print('post in home')
        form = SubmitUrlForm(request.POST)

        context = {
            'title': 'Bytely.co',
            'form': form
        }

        template = 'shortener/home.html'
        if form.is_valid():
            url = form.cleaned_data.get('url')
            obj, created = BytelyURL.objects.get_or_create(url=url)
            context = {
                'object': obj,
                'created': created
            }
            if created:
                template = 'shortener/success.html'
            else:
                template = 'shortener/already-exists.html'

        return render(request, template, context=context)


class BytelyRedirectView(View):

    def get(self, request, shortcode=None, *args, **kwargs):
        print('get in redirect')
        obj = get_object_or_404(BytelyURL, shortcode=shortcode)
        ClickEvent.objects.create_event(obj)
        return HttpResponseRedirect(absolute_location(obj.url))
