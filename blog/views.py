from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from django.views import View
from datetime import datetime
from blog.models import ArticleModel,ContactModel
from django.utils import timezone
from blog.forms import ArticleForm
# from blog.forms import ArticleForm
# Create your views here.
# function based views
# def home(request):
#     if request.method == 'GET':
#         return HttpResponse("[GET] Welocm to my blog")
#     if request.method == 'POST':
#         return HttpResponse("[POST] Welocm to my blog")
# def about_us(request):
#     if request.method == 'GET':
#         return HttpResponse("[GET] About us")
    
#     if request.method == 'POST':
#         return HttpResponse("[POST] About us")

# class based views

class Home(View):
    def get(self,request):
        return render(request,'home.html')
    def post(self,reguest):
        return HttpResponse("[POST] Welocm to my blog")
    

class Article(View):
    def get(self,request):
        articles = ArticleModel.objects.all()
        '''
        # articles = [
        #     {
        #         'title': 'Article 1',
        #         'author': 'Jhon Wick',
        #         'topic': 'Self respect',
        #         'Created_at': datetime.now()
        #     },
        #     {
        #         'title': 'Article 2',
        #         'author': 'Alice',
        #         'topic': 'Mountain love',
        #         'Created_at': datetime.now()
        #     },
        #     {
        #         'title': 'Article 3',
        #         'author': 'Julie',
        #         'topic': 'Summer side',
        #         'Created_at': datetime.now()
        #     },
        #     {
        #         'title': 'Article 4',
        #         'author': 'Bruce',
        #         'topic': 'Another way',
        #         'Created_at': datetime.now()
        #     },
        #     {
        #         'title': 'Article 5',
        #         'author': 'Anthony',
        #         'topic': 'Economy crises',
        #         'Created_at': datetime.now()
        #     }
        # ]

        '''
        return render(request,'articles.html',{"articles":articles, "form": ArticleForm})
        # return render(request,'articles.html',{"articles":articles})

    def post(self,request):
        form = ArticleForm(request.POST)
        if form.is_valid():
           form.instance.created_at = datetime.now()
           form.save()
           return redirect("/blog/articles")
        else:
            articles = ArticleModel.objects.all()
            return render(request, 'articles.html', {"articles": articles, "form": ArticleForm})
        # title = request.POST['title']
        # author = request.POST['author']
        # topic = request.POST['topic']
        # print(title,author,topic)
        # ArticleModel.objects.create(title=title,author=author,topic=topic,created_at=datetime.now())
        # return redirect("/blog/articles")

class ArticleDetails(View):
    def get(self,request,id):
        try:
            article = ArticleModel.objects.get(id=id)
            return render(request,'aticledetails.html',{"article":article})
        except ArticleModel.DoesNotExist:
            return HttpResponseNotFound()
        
class DeleteArticle(View):
    def get(self,request,id):
        try:
            artcile = ArticleModel.objects.get(id=id)
            artcile.delete()
            print("Deleted Article: " + str(artcile.title))
            return redirect("/blog/articles")
        except:
            return HttpResponse("can not delete the itee")

class About_us(View):
    def get(self,request):
        return render(request,'about.html')
    def post(self,reguest):
        return HttpResponse("[POST] About us")


class Contact(View):
    def get(self,request):
        return render(request,'contact.html')
    
    def post(self,request):
        name = request.POST['name']
        email= request.POST['email']
        number=request.POST['number']
        message=request.POST['message']
        gender=request.POST['gender']
        print(name,email,number,message,gender)
        ContactModel.objects.create(name=name,email=email,number=number,message=message,gender=gender)
        return redirect('/blog')