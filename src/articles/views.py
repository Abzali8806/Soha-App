from django.shortcuts import render
from .forms import ArticleForm
from .models import Article

# Create your views here.
def sandbox_view(request, *args, **kwargs):
    form = ArticleForm
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid:
            form.save()
    
    context = {'form': form}
    return render(request, 'sandbox.html', context)