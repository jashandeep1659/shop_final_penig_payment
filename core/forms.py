from django import forms

class SearchForm(forms.Form):
	query = forms.CharField()



class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()
