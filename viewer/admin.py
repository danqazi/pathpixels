from django.contrib import admin
# Register your models here.
from viewer.models import Case, Profile, Question, Diagnosis

admin.site.register(Case)
admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Diagnosis)
