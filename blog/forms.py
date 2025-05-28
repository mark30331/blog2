from django import forms
from .models import Comment


# forms inherits from the base Form class
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea
    )


#use modelForm to use an existing form in the database
class CommentForm(forms.ModelForm):
    class Meta:
        #this indicates the model to build
        #  the form for in the meta class
        model = Comment

        #which fields to include instead of all by default
        fields = ['name', 'email', 'body']



class SearchForm(forms.Form):
    query = forms.CharField()
    