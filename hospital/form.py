from django import forms
from .models import Doctor, Department, Appointment, Admin


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"


