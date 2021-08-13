from django.contrib import admin

# 추가한 내용
from .models import *

admin.site.register(User)
admin.site.register(Animal)
admin.site.register(csCenter)