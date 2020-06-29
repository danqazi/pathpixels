from django.contrib import admin
# Register your models here.
from viewer.models import Case, Profile, Question, Diagnosis, OrganSystem, Tutorial, Quiz, Performance

admin.site.register(Case)
admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Diagnosis)
admin.site.register(OrganSystem)
admin.site.register(Tutorial)
admin.site.register(Quiz)
admin.site.register(Performance)

