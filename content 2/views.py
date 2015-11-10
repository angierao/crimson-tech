from django.shortcuts import render
from django.shortcuts import get_object_or_404
from models import Article
from models import Content, Image, Contributor

def homepage(request):
	articles = Article.objects.all()
	data = {'articles': articles}
	return render(request,'homepage.html',data)

def detail(request,article_id):
	article = get_object_or_404(Article, pk=article_id)
	return render(request, 'detail.html', {'article':article})