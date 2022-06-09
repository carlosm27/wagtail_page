from django.shortcuts import render
from models import BlogCategory


# Create your views here.

def categories(request):
    categories = BlogCategory.objects.all()
    context = {"categories": categories}
    return render(request, "blog_categorie_index_page.html", context)