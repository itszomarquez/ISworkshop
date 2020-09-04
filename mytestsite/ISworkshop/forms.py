from django import forms
from .models import ProfilePage
import datetime

class ProfilePageForm(forms.ModelForm):
    email = forms.EmailField(
        label = '', 
        widget = forms.TextInput(attrs = {'placeholder': 'Email', 'class':'email'}), 
        max_length = 60
    )

    student_number = forms.CharField(
        label = '', 
        widget = forms.TextInput(attrs = {'placeholder': 'Student Number', 'class':'student_number'}), 
        max_length = 9
    )

    first_name = forms.CharField(
        label = '', 
        widget = forms.TextInput(attrs = {'placeholder': 'First Name', 'class':'first_name'}), 
        max_length = 60
    )

    last_name = forms.CharField(
        label = '', 
        widget = forms.TextInput(attrs = {'placeholder': 'Last Name', 'class':'last_name'}), 
        max_length = 60
    )
    graduation_year = forms.IntegerField(
        min_value = datetime.date.today().year,
        max_value = datetime.date.today().year + 10,
        label = 'Expected year of graduation', 
        widget = forms.NumberInput(attrs = {'class':'graduation_year'}),
    )
    
    degree = forms.ChoiceField(
        choices= ProfilePage.DEGREES,
        label = 'Degree',
        widget = forms.Select(attrs = {'class':'degree'})
    )

    program = forms.ChoiceField(
        choices= ProfilePage.PROGRAMS,
        widget = forms.Select(attrs = {'class':'program'})
    )
    class Meta:
        model = ProfilePage
        fields = ('email', 'student_number', 'first_name', 'last_name', 'graduation_year', 'degree', 'program', 'profile_picture',)
