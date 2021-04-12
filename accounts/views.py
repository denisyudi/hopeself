from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.conf import settings

def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'accounts/index.html')

def admin_confirm(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'accounts/adminconfirm.html')

def medico_confirm(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'accounts/medicoconfirm.html')

def paciente_confirm(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'accounts/pacienteconfirm.html')

def admin_register(request):
    form = forms.AdminRegisterForm()
    if request.method == 'POST':
        form = forms.AdminRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            grupo_admin = Group.objects.get_or_create(name='ADMIN')
            grupo_admin[0].user_set.add(user)
            return HttpResponseRedirect('adminlogin')
    return render(request, 'accounts/adminregister.html', {'form': form})

def medico_register(request):
    userForm = forms.MedicoRegisterForm()
    medicoForm = forms.MedicoForm()
    mydict = {'userForm': userForm, 'medicoForm': medicoForm}
    if request.method=='POST':
        userForm = forms.MedicoRegisterForm(request.POST)
        medicoForm = forms.MedicoForm(request.POST,request.FILES)
        if userForm.is_valid() and medicoForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            medico = medicoForm.save(commit=False)
            medico.user = user
            medico = medico.save()
            grupo_medico = Group.objects.get_or_create(name='MEDICO')
            grupo_medico[0].user_set.add(user)
        return HttpResponseRedirect('medicologin')
    return render(request, 'accounts/medicoregister.html', context=mydict)

def paciente_register(request):
    userForm = forms.PacienteRegisterForm()
    pacienteForm = forms.PacienteForm()
    mydict = {'userForm': userForm, 'pacienteForm': pacienteForm}
    if request.method=='POST':
        userForm = forms.PacienteRegisterForm(request.POST)
        pacienteForm = forms.PacienteForm(request.POST,request.FILES)
        if userForm.is_valid() and pacienteForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            paciente=pacienteForm.save(commit=False)
            paciente.user=user
            paciente.assignedDoctorId=request.POST.get('assignedDoctorId')
            paciente = paciente.save()
            grupo_paciente = Group.objects.get_or_create(name='PACIENTE')
            grupo_paciente[0].user_set.add(user)
        return HttpResponseRedirect('pacientelogin')
    return render(request, 'accounts/pacienteregister.html', context=mydict)

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_medico(user):
    return user.groups.filter(name='MEDICO').exists()
def is_paciente(user):
    return user.groups.filter(name='PACIENTE').exists()

def after_login(request):
    if is_admin(request.user):
        return redirect('admin-main')
    elif is_medico(request.user):
        accountapproval = models.Medico.objects.all().filter(user_id=request.user.id, status=True)
        if accountapproval:
            return redirect('medico-main')
        else:
            return render(request,'accounts/doctor_wait_for_approval.html')
    elif is_paciente(request.user):
        accountapproval = models.Paciente.objects.all().filter(user_id=request.user.id, status=True)
        if accountapproval:
            return redirect('paciente-main')
        else:
            return render(request,'accounts/patient_wait_for_approval.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_main(request):
    medicos = models.Medico.objects.all().order_by('-id')
    pacientes= models.Paciente.objects.all().order_by('-id')
    total_medicos = models.Medico.objects.all().filter(status=True).count()
    pendingdoctorcount = models.Medico.objects.all().filter(status=False).count()

    total_pacientes = models.Paciente.objects.all().filter(status=True).count()
    pendingpatientcount = models.Paciente.objects.all().filter(status=False).count()

    appointmentcount = models.Consulta.objects.all().filter(status=True).count()
    pendingappointmentcount = models.Consulta.objects.all().filter(status=False).count()
    mydict={
        'medicos': medicos,
        'pacientes': pacientes,
        'total_medicos': total_medicos,
        'pendingdoctorcount': pendingdoctorcount,
        'total_pacientes': total_pacientes,
        'pendingpatientcount': pendingpatientcount,
        'appointmentcount': appointmentcount,
        'pendingappointmentcount': pendingappointmentcount,
    }
    return render(request,'accounts/admin_main.html',context=mydict)

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_medicos(request):
    return render(request, 'accounts/admin_medicos.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_lista_medicos(request):
    medicos = models.Medico.objects.all().filter(status=True)
    return render(request, 'accounts/admin_lista_medicos.html', {'medicos': medicos})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_aceita_medico(request):
    medicos = models.Medico.objects.all().filter(status=False)
    return render(request, 'accounts/admin_aceita_medico.html', {'medicos': medicos})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def aceita_medico(request, pk):
    medico = models.Medico.objects.get(id=pk)
    medico.status=True
    medico.save()
    return redirect(reverse('admin-aceita-medico'))

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_pacientes(request):
    return render(request,'accounts/admin_pacientes.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_lista_pacientes(request):
    pacientes = models.Paciente.objects.all().filter(status=True)
    return render(request, 'accounts/admin_lista_pacientes.html', {'pacientes': pacientes})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_consultas(request):
    return render(request,'accounts/admin_consultas.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_lista_consultas(request):
    appointments=models.Consulta.objects.all().filter(status=True)
    return render(request,'accounts/admin_lista_consultas.html',{'appointments':appointments})

@login_required(login_url='medicologin')
@user_passes_test(is_medico)
def medico_main(request):
    patientcount = models.Paciente.objects.all().filter(status=True, assignedDoctorId=request.user.id).count()
    appointmentcount = models.Consulta.objects.all().filter(status=True,doctorId=request.user.id).count()

    appointments=models.Consulta.objects.all().filter(status=True,doctorId=request.user.id).order_by('-id')
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Paciente.objects.all().filter(status=True,user_id__in=patientid).order_by('-id')
    appointments=zip(appointments,patients)
    mydict={
    'patientcount':patientcount,
    'appointmentcount':appointmentcount,
    'appointments':appointments,
    'doctor':models.Medico.objects.get(user_id=request.user.id),
    }
    return render(request,'accounts/medico_main.html',context=mydict)

@login_required(login_url='medicologin')
@user_passes_test(is_medico)
def medico_pacientes(request):
    mydict={
    'doctor':models.Medico.objects.get(user_id=request.user.id),
    }
    return render(request,'accounts/medico_pacientes.html',context=mydict)

@login_required(login_url='medicologin')
@user_passes_test(is_medico)
def medico_lista_pacientes(request):
    patients=models.Paciente.objects.all().filter(status=True,assignedDoctorId=request.user.id)
    doctor=models.Medico.objects.get(user_id=request.user.id)
    return render(request,'accounts/medico_lista_pacientes.html',{'patients':patients,'doctor':doctor})

@login_required(login_url='medicologin')
@user_passes_test(is_medico)
def medico_consultas(request):
    doctor=models.Medico.objects.get(user_id=request.user.id)
    return render(request,'accounts/medico_consultas.html',{'doctor':doctor})

@login_required(login_url='medicologin')
@user_passes_test(is_medico)
def medico_lista_consultas(request):
    doctor=models.Medico.objects.get(user_id=request.user.id)
    appointments=models.Consulta.objects.all().filter(status=True,doctorId=request.user.id)
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Paciente.objects.all().filter(status=True,user_id__in=patientid)
    appointments=zip(appointments,patients)
    return render(request,'accounts/doctor_lista_consultas.html',{'appointments':appointments,'doctor':doctor})

@login_required(login_url='pacientelogin')
@user_passes_test(is_paciente)
def paciente_main(request):
    patient=models.Paciente.objects.get(user_id=request.user.id)
    doctor=models.Medico.objects.get(user_id=patient.assignedDoctorId)
    mydict={
    'patient':patient,
    'doctorName':doctor.get_name,
    'doctorMobile':doctor.mobile,
    'doctorAddress':doctor.address,
    'symptoms':patient.symptoms,
    'doctorDepartment':doctor.department,
    'admitDate':patient.admitDate,
    }
    return render(request,'accounts/paciente_main.html',context=mydict)

@login_required(login_url='pacientelogin')
@user_passes_test(is_paciente)
def paciente_consultas(request):
    patient=models.Paciente.objects.get(user_id=request.user.id)
    return render(request,'accounts/paciente_consultas.html',{'patient':patient})