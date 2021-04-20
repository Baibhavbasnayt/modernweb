from django.contrib import admin
from .models import Doctor, Department, Admin


admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Admin)


