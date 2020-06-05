from django import forms
from viewer.models import UserProfileInfo, UserAnswer, Question
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields =('first_name', 'last_name', 'username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        exclude = ('user',)

# class RegistrationForm(forms.ModelForm):
#     class Meta():
#         model = MyUser
#         fields = '__all__'

class QuestionForm(forms.ModelForm):

    class Meta():
        model = Question
        fields = ('question',)

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class AnswerForm(forms.ModelForm):
    class Meta():
        model = UserAnswer
        fields = ('answer',)

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
