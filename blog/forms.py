from django.forms import ModelForm, TextInput
from blog.models import ArticleModel
class ArticleForm(ModelForm):
    class Meta:
        model = ArticleModel
        fields = ["title","author","topic"]
        widgets = {
            "title": TextInput(attrs={"placeholder": "Enter title"}),
            "author": TextInput(attrs={"placeholder": "Enter author"}),
            "topic": TextInput(attrs={"placeholder": "Enter topic"}),
        }
         