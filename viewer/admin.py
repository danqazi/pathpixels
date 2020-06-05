from django.contrib import admin
# Register your models here.
from viewer.models import Case, UserProfileInfo, Question, UserAnswer

admin.site.register(Case)
admin.site.register(UserProfileInfo)
admin.site.register(Question)
admin.site.register(UserAnswer)
# admin.site.register(models.UserAnswer)
