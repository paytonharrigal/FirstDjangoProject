"""
To Render HTML web pages 
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article

random_id = random.randint(1,4)


# from DataBase

def home_view(request):

    article_obj = Article.objects.get(id=random_id)

    my_list = [102,13,342,1331,213]
    my_list_str = ""
    for x in my_list:
        my_list_str += f"number is {x}\n"

    context = {
        "my_list_str": my_list_str,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }
    HTML_STRING = render_to_string("home-view.html", context = context)

    
    return HttpResponse(HTML_STRING)