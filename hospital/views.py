from django.shortcuts import render, redirect
from .models import Doctor, Department, Appointment
from .form import DoctorForm, DepartmentForm, AppointmentForm, AdminForm
from .authenticate import Authenticate


def index(request):
    experts = Doctor.objects.all()
    services = Department.objects.all()
    return render(request, "hospital/index.html", {'experts': experts, 'services': services})


def admin(request):
    return render(request, 'admin/admin_login.html')

def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')

def admin_signup(request):
    if request.method == "POST":
        adminform = AdminForm(request.POST)
        adminform.save()
        redirect('/')
    adminform = AdminForm()
    return render(request, 'admin/admin_signup.html', {'form': adminform})


def admin_login(request):
    request.session['email'] = request.POST['email']
    request.session['password'] = request.POST['password']
    return redirect('/admindash/')


def login(request):
    return render(request,'admin/admin_login.html')


@Authenticate.valid_adminlogin
def admin(request):
    return render(request, 'admin/dashboard.html')


def department(request):
    services = Department.objects.all()
    return render(request, "hospital/department.html", {'services': services})


def doctor(request):
    experts = Doctor.objects.all()
    return render(request, "hospital/doctors.html", {'experts': experts})


def show_about(request):
    return render(request, "hospital/about.html")


def show_contact(request):
    return render(request, "hospital/contact.html")


def add_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showdoctor/')
            except:
                pass
    else:
        form=DoctorForm()
    return render(request,'admin/doctor/add_doctor.html',{'form':form})


def show_doctor(request):
    doctor = Doctor.objects.all()
    return render(request, 'admin/doctor/show_doctor.html', {'get_doctor_data': doctor})


def update_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    form = DoctorForm(request.POST or None, instance=doctor)
    if form.is_valid():
        form.save()
        return redirect('/showdoctor/')
    else:
        return render(request, 'admin/doctor/add_doctor.html', {'form': form})


def delete_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('/showdoctor/')


def add_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showdepartment/')
            except:
                pass
    else:
        form=DepartmentForm()
    return render(request,'admin/department/add_department.html',{'form':form})


def show_department(request):
    doctor = Department.objects.all()
    return render(request, 'admin/department/show_department.html', {'get_department_data': doctor})


def update_department(request, id):
    doctor = Department.objects.get(id=id)
    form = DepartmentForm(request.POST or None, instance=doctor)
    if form.is_valid():
        form.save()
        return redirect('/showdepartment/')
    else:
        return render(request, 'admin/department/add_department.html', {'form': form})


def delete_department(request, id):
    doctor = Department.objects.get(id=id)
    doctor.delete()
    return redirect('/showdepartment/')


def add_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/appointmentadd/')
            except:
                pass
    else:
        form = AppointmentForm()
    return render(request,'admin/appointment/add_appointment.html', {'form': form})


def show_appointment(request):
    patient = Appointment.objects.all()
    return render(request, 'admin/appointment/show_appointment.html', { 'get_patient_data': patient})


def update_appointment(request, id):
    patient = Appointment.objects.get(id=id)
    form = AppointmentForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        return redirect('/showappointment/')
    else:
        return render(request, 'admin/appointment/add_appointment.html', {'form': form})


def delete_appointment(request, id):
    patient = Appointment.objects.get(id=id)
    patient.delete()
    return redirect('/showappointment/')

