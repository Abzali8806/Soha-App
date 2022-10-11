from django.shortcuts import render

# Create your views here.
def login_view(request, *args, **kwargs):
    form = ArticleForm
    context = {'form': form}
    return render(request, 'login.html', context)