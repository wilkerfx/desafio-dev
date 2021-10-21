from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage


class Home(TemplateView):
    template_name = "index.html"


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        file_storage = FileSystemStorage()
        file_storage.save(uploaded_file)
        #print(uploaded_file.name)
        #print(uploaded_file.size)
    return render(request, 'upload.html')



'''def index(request):

    return render(request, 'index.html')'''





'''from django.views.generic.base import TemplateView

from articles.models import Article

class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context'''