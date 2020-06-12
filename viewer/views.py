#Python

#Django

#Own

from django.shortcuts import render
from viewer.models import User, Case, Profile, OrganSystem, Tutorial, Diagnosis
from viewer.forms import UserForm, UserProfileInfoForm, AnswerForm, UploadFileForm, EditCaseForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import authenticate, login, logout, get_user
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.views.generic import View, TemplateView, ListView, DetailView, CreateView


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


@login_required
def MainPageView(request):
    organsystem_name = request.GET.get("organsystem")
    organsystem = OrganSystem.objects.get(name=organsystem_name)
    tutorials = organsystem.tutorials.all()
    return render(request, 'viewer/main.html', context={'organsystem': organsystem, 'tutorials': tutorials})



# class MainPageView(LoginRequiredMixin, TemplateView):
#     template_name = 'viewer/main.html'
#     model = OrganSystem
#     # login_url = '/'
#     # redirect_field_name = 'viewer/base.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['inject_me'] = 'BASIC INJECTION'
#         return context
#     # dispatch is called when the class instance loads
#     def dispatch(self, request, *args, **kwargs):
#         self.year = kwargs.get('year', "any_default")
#     # other code
#     # needed to have an HttpResponse
#     return super(MainPageView, self).dispatch(request, *args, **kwargs)
# def main_page(request):
#     return render(request, 'viewer/main.html')


@login_required
def CasesView(request, organsystem_name):
    organsystem = OrganSystem.objects.get(name=organsystem_name)
    case_list = Case.objects.all().order_by('id')
    print('goodbye')
    return render(request, 'viewer/cases.html', context={'organsystem': organsystem, 'case_list': case_list})


# class CasesView(LoginRequiredMixin, ListView):
#     model = Case
#     template_name = 'viewer/cases.html'
#     context_object_name = 'case_list'
#
#     def get_queryset(self):
#         return Case.objects.all()

# def cases_page(request):
#     case_list = Case.objects.all()
#     return render(request, 'viewer/cases.html', context={'case_list':case_list})

# @login_required
# class WSIView(LoginRequiredMixin, DetailView):
#     model = Case
#     template_name = 'viewer/wsi.html'


@login_required
def wsi(request, organsystem_name, case_id):
    case = Case.objects.get(pk=case_id)
    case_name_low = case.name.lower()
    case_name = case_name_low.replace(' ', '_')
    case_name_dzi = case_name + '/' + case_name + '.dzi'
    case_dx = case.diagnosis.text

    diagnoses = []
    for diagnosis in Diagnosis.objects.all():
        diagnoses.append(diagnosis.text)

    if request.method == 'GET':
        answer_form = AnswerForm()
        answered = False
        answer = ''

    if request.method == 'POST':
        answer_form = AnswerForm(data=request.POST)
        answered = True

        if answer_form.is_valid():
            answer = answer_form.cleaned_data['text']
            answer_form = AnswerForm(initial={'text': answer})
        else:
            print(answer_form.errors)

    return render(request, 'viewer/wsi.html', context={'dx': case_name, 'dx_dzi': case_name_dzi, 'case': case,
                                                       'answer_form': answer_form, 'answered': answered,
                                                       'teach_points': case.teach_points, 'diagnoses': diagnoses,
                                                       'case_dx': case_dx, 'answer': answer})


@login_required
def upload(request):

    diagnoses = []
    for diagnosis in Diagnosis.objects.all():
        diagnoses.append(diagnosis.text)

    cases = []
    for case in Case.objects.all():
        cases.append(case.name)

    if request.method == 'POST':
        upload_form = UploadFileForm()
        edit_case_form = EditCaseForm(data=request.POST)
        selected = True
        if edit_case_form.is_valid():
            selected_name = edit_case_form.cleaned_data['name']
            selected_case = Case.objects.get(name=selected_name)
    elif request.method == 'GET':
        upload_form = UploadFileForm()
        edit_case_form = EditCaseForm()
        selected = False
        selected_case = ''

    return render(request, 'viewer/upload.html', context={'upload_form': upload_form, 'edit_form': edit_case_form,
                                                          'diagnoses': diagnoses, 'cases': cases,
                                                          'selected_case': selected_case, 'selected': selected})


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

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            Profile.objects.create(user=user)

            registered = True

        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'viewer/registration.html',
                  context={'user_form': user_form, 'registered': registered})
