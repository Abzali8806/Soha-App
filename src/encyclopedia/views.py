from django.shortcuts import render
from django.shortcuts import redirect
from articles.models import Article

# Create your views here.
def home_view(request, *args, **kwargs):
    if request.method == "POST":
        query = request.POST['searched']
        context = {
            "query": query
        }
    context = {}
    return render(request, 'index.html', context)


def results_view(request, *args, **kwargs):
    data = Article.objects.all()
    # print(request.GET)
    query_dict = request.GET
    query = query_dict.get('query')
    # print(data)
    # print(query_dict)
    for dt in data:
        if query == dt.title:
            print(dt)
            # return redirect('article')
        else:
            break
            
    context = {
        "query":query,
        "articles": data
    }
    return render(request, 'results.html', context)


def article_view(request, *args, **kwargs):
    # data = Article.objects.all()
    qd = request.GET
    print(qd)
    context = {}
    return render(request, 'article.html', context)