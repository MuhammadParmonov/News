from django import forms
from .models import News, Category

# CATEGORY_CHOICES = []
# for cat in Category.objects.all():
#     CATEGORY_CHOICES.append((cat.id, cat.nomi))

class NewsForm(forms.ModelForm):
    nomi = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Yangilik nomi'
    }))
    mazmuni = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Yangilik mazmuni'
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))
    # category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = News
        fields = ["nomi", "mazmuni", "image", "category"]

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs["class"] = "form-select"
        self.fields['category'].widget.attrs["style"] = "width: 300px"
        
class CategoryForm(forms.ModelForm):
    nomi = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Kategoriya nomi'
    }))
    mazmuni = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Kategoriya mazmuni'
    }), required=False)
    class Meta:
        model = Category
        fields = ["nomi", "mazmuni"]