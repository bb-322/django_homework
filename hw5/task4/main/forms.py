from django import forms

choices = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
]

class ReviewForm(forms.Form):
    email = forms.EmailField(max_length=255)
    description = forms.CharField(max_length=500)
    rating = forms.ChoiceField(choices=choices)
    phone_number = forms.IntegerField(widget=forms.NumberInput)
    picture = forms.FileField(required=False)