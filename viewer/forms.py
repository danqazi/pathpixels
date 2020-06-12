from django import forms
from viewer.models import Profile, Question, Case
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Enter your password'}))

    class Meta:
        model = User
        fields =('first_name', 'last_name', 'username', 'email', 'password')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your desired username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
        }


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

# class RegistrationForm(forms.ModelForm):
#     class Meta():
#         model = MyUser
#         fields = '__all__'

# class QuestionForm(forms.ModelForm):
#
#     class Meta():
#         model = Question
#         fields = ('question',)
#
#         widgets = {
#             'title':forms.TextInput(attrs={'class':'textinputclass'}),
#             'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
#         }


class AnswerForm(forms.Form):
    text = forms.CharField(max_length=250, required=True, label='Answer')


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ('name', 'diagnosis', 'history', 'teach_points')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control autocomp', 'placeholder': 'Enter the name of your case'}),
            'diagnosis': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Enter the associated diagnosis for your case'}),
            'history': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the clinical history'}),
            'teach_points': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your teaching points'})
        }

    file = forms.FileField()


class EditCaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control autocomp',
                                           'placeholder': 'Enter the name of your case'}),
        }

