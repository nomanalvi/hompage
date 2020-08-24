from django import forms
from. models import Allcourses

class NameForm(forms.Form):
    CHOICES = (
        (11, 'A'),
        (12, 'B'),
        (13, 'C'),
        (21, 'D'),
        (22, 'E'),
        (31, 'F'),
        (32, 'G'),
    )
    your_name = forms.CharField(label='Your name', max_length=100)
    Courses = forms.ChoiceField(choices=CHOICES)
