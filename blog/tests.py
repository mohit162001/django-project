from django.test import TestCase
from blog.models import ArticleModel
from datetime import datetime
# Create your tests here.
class ArticleTest(TestCase):
    def test_article_create_success(self):
        ArticleModel.objects.create(title="TestTitle",author="TestAUthor",topic="TestTopic",created_at=datetime.now())
        article = ArticleModel.objects.get(title="TestTitle")
        self.assertEqual(article.topic,"TestTopic")