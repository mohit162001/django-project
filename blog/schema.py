import graphene
from graphene_django import DjangoObjectType
from .models import ArticleModel
from datetime import datetime
class ArticleType(DjangoObjectType):
    class Meta:
        model = ArticleModel
        fields = "__all__"

class Query(graphene.ObjectType):
    articles = graphene.List(ArticleType)
    def resolve_articles(root,info):
        return ArticleModel.objects.all()
    
    article = graphene.Field(ArticleType,id=graphene.String())
    def resolve_article(root,info,id):
        return ArticleModel.objects.get(id=id)
    
    
class ArticleCreate(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author = graphene.String(required=True)
        topic = graphene.String(required=True)
        content = graphene.String(required=True)

    
    article = graphene.Field(ArticleType)
    @classmethod
    def mutate(cls,root,info,title,author,topic,content):
        article = ArticleModel.objects.create(title=title,topic=topic,author=author,content=content,created_at=datetime.now())
        article.save()
        return ArticleCreate(article=article)
    
class ArticleUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        title = graphene.String()
        author = graphene.String()
        topic = graphene.String()
        content = graphene.String()
    article = graphene.Field(ArticleType)
    @classmethod
    def mutate(cls,root,info,id,title,author,topic,content):
        article = ArticleModel.objects.get(id=id)
        article.title = title
        article.author = author
        article.topic = topic
        article.content = content
        article.created_at = datetime.now()
        article.save()
        return ArticleUpdate(article=article)  
    
class ArticleDelete(graphene.Mutation):
    class Arguments:
        id=graphene.String(required=True)
    mess = graphene.String()
    @classmethod
    def mutate(cls,root,info,id):
        article = ArticleModel.objects.get(id=id)
        article.delete()
        return ArticleDelete(mess = "Article deleted successfully")
        
        
class Mutation(graphene.ObjectType):
    create_Article = ArticleCreate.Field()
    delete_Article = ArticleDelete.Field()
    update_Article  =ArticleUpdate.Field()
    
schema = graphene.Schema(query=Query,mutation=Mutation)