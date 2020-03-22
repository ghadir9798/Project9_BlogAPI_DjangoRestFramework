from django import forms

from pagedown.widgets import PagedownWidget
from .models import Post


class MyNewWidget(PagedownWidget):

    class Media:
        css = {
            'all': ('../static/css/base.css',)
        }
    

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=MyNewWidget())
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish"
        ]