from django.shortcuts import render
from viewer.models import User, Case
from viewer.forms import UserForm, UserProfileInfoForm, AnswerForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import authenticate, login, logout, get_user
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.views.generic import View, TemplateView, ListView, DetailView, CreateView

# Create your views here.
class CBView(View):
    def get(self, request):
        return HttpResponse('Class Based Views are cool!')

class TestView(TemplateView):
    template_name = 'viewer/wsi.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'BASIC INJECTION'
        return context


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return render(request, 'viewer/profile.html', {"username": username})

        else:
            print("Someone tried to log in and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'viewer/base.html', {})


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'viewer/base.html', {})

# @login_required
class MainPageView(LoginRequiredMixin, TemplateView):
    template_name = 'viewer/gyn_main.html'
    # login_url = '/'
    # redirect_field_name = 'viewer/base.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'BASIC INJECTION'
        return context

# def main_page(request):
#     return render(request, 'viewer/gyn_main.html')

# @login_required
class CasesView(LoginRequiredMixin, ListView):
    model = Case
    template_name = 'viewer/gyn_cases.html'
    context_object_name = 'case_list'

    def get_queryset(self):
        return Case.objects.all()

# def cases_page(request):
#     case_list = Case.objects.all()
#     return render(request, 'viewer/gyn_cases.html', context={'case_list':case_list})

# @login_required
# class WSIView(LoginRequiredMixin, DetailView):
#     model = Case
#     template_name = 'viewer/wsi.html'

def wsi(request, case_id):
    case = Case.objects.get(pk=case_id)

    if request.method == 'POST':
        answer_form = AnswerForm(data=request.POST)

        if answer_form.is_valid():
            answer = user_form.save()
            answer.save()

        else:
            print(answer_form.errors)
    else:
        answer_form = AnswerForm()

    case_name_low = case.diagnosis.lower()
    case_name = case_name_low.replace(' ', '_')
    case_name_dzi = case_name + '/' + case_name + '.dzi'

    return render(request, 'viewer/wsi.html', context={'dx':case_name, 'dx_dzi':case_name_dzi, 'case':case, 'answer_form':answer_form})

@login_required
def profile(request):
    username = get_user(request).username
    return render(request, 'viewer/profile.html', {"username": username})

# def submit_answer(request):
#     form = forms.AnswerForm()
#
#     if request.method == 'POST':
#         form = forms.AnswerForm(request.POST)
#
#         if form.is_valid():
#             pass
#
#     return render(request, 'viewer/wsi.html', context={'form': form})
#
def registration(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'viewer/registration.html',
                  context={'user_form':user_form, 'profile_form': profile_form,
                  'registered': registered})
