from django import forms
from post.models import Product


class ProductCreateForm(forms.Form):
    image = forms.ImageField(required=False)
    title = forms.CharField(max_length=100)
    price = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if len(title) < 10:
            raise forms.ValidationError("Title to short!")
        return cleaned_data


class CategoryCreateForm(forms.ModelForm):
    title = forms.CharField
    image = forms.ImageField(required=False)


class ReviewCreateForm(forms.ModelForm):
    rating = forms.IntegerField()
    review_title = forms.CharField


class ProductCreateForm2(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'image', 'price']
