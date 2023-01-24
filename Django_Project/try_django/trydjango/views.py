"""
To Render HTML web pages 
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article



# from DataBase

def home_view(request):
    # from database
    random_id = random.randint(1,4)
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    print(id)
    context = {
        "object_list": article_queryset,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }
    HTML_STRING = render_to_string("home-view.html", context = context)

    
    return HttpResponse(HTML_STRING)