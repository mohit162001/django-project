from django.forms import ModelForm, TextInput,Textarea
from blog.models import ArticleModel
class ArticleForm(ModelForm):
    class Meta:
        model = ArticleModel
        fields = ["title","author","topic","content"]
        widgets = {
            "title": TextInput(attrs={"placeholder": "Enter title"}),
            "author": TextInput(attrs={"placeholder": "Enter author"}),
            "topic": TextInput(attrs={"placeholder": "Enter topic"}),
            "content": Textarea(attrs={"placeholder": "Write your content here..","rows":12,"cols":50})
        }
         