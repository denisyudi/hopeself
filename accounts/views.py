from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse

from . import forms, models


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
    if request.method == 'POST':
        userForm = forms.MedicoRegisterForm(request.POST)
        medicoForm = forms.MedicoForm(request.POST, request.FILES)
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
    if request.method == 'POST':
        userForm = forms.PacienteRegisterForm(request.POST)
        pacienteForm = forms.PacienteForm(request.POST, request.FILES)
        if userForm.is_valid() and pacienteForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            paciente = pacienteForm.save(commit=False)
            paciente.user = user
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
        return redirect('medico-main')
    elif is_paciente(request.user):
        return redirect('paciente-main')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_main(request):
    medicos = models.Medico.objects.all().order_by('-id')
    pacientes = models.Paciente.objects.all().order_by('-id')
    total_medicos = models.Medico.objects.all().filter(status=True).count()
    total_medicos_para_aprovacao = models.Medico.objects.all().filter(status=False).count()
    total_pacientes = models.Paciente.objects.all().filter(status=True).count()
    total_pacientes_para_aprovacao = models.Paciente.objects.all().filter(status=False).count()

    view = {
        'medicos': medicos,
        'pacientes': pacientes,
        'total_medicos': total_medicos,
        'medicos_para_aprovacao': total_medicos_para_aprovacao,
        'total_pacientes': total_pacientes,
        'pacientes_para_aprovacao': total_pacientes_para_aprovacao,
    }
    return render(request, 'accounts/admin_main.html', context=view)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_medicos(request):
    medicos = models.Medico.objects.all()
    return render(request, 'accounts/admin_medicos.html', {'medicos': medicos})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def aceita_medico(request, pk):
    medico = models.Medico.objects.get(id=pk)
    medico.status = True
    medico.save()
    return redirect(reverse('admin-aceita-medico'))


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_pacientes(request):
    pacientes = models.Paciente.objects.all()
    return render(request, 'accounts/admin_pacientes.html', {'pacientes': pacientes})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_notificacoes(request):
    return render(request, 'accounts/admin_notificacoes.html')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dados(request):
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
    return render(request, 'accounts/admin_dados.html', {'form': form})


@login_required(login_url='medicologin')
@user_passes_test(is_medico)
def medico_main(request):
    return render(request, 'accounts/medico_main.html')


@login_required(login_url='medicologin')
@user_passes_test(is_medico)
def medico_pacientes(request):
    mydict = {
        'medicos': models.Medico.objects.get(user_id=request.user.id),
    }
    return render(request, 'accounts/medico_pacientes.html', context=mydict)


@login_required(login_url='medicologin')
@user_passes_test(is_medico)
def medico_consultas(request):
    medico = models.Medico.objects.get(user_id=request.user.id)
    return render(request, 'accounts/medico_consultas.html', {'medico': medico})


@login_required(login_url='medicologin')
@user_passes_test(is_medico)
def medico_notificacoes(request):
    medico = models.Medico.objects.get(user_id=request.user.id)
    return render(request, 'accounts/medico_notificacoes.html', {'medico': medico})


@login_required(login_url='medicologin')
@user_passes_test(is_medico)
def medico_dados(request):
    userForm = forms.MedicoRegisterForm()
    medicoForm = forms.MedicoForm()
    mydict = {'userForm': userForm, 'medicoForm': medicoForm}
    if request.method == 'POST':
        userForm = forms.MedicoRegisterForm(request.POST)
        medicoForm = forms.MedicoForm(request.POST, request.FILES)
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
    return render(request, 'accounts/medico_dados.html', context=mydict)


@login_required(login_url='pacientelogin')
@user_passes_test(is_paciente)
def paciente_main(request):
    paciente = models.Paciente.objects.get(user_id=request.user.id)
    mydict = {
        'paciente': paciente,
    }
    return render(request, 'accounts/paciente_main.html', context=mydict)


@login_required(login_url='pacientelogin')
@user_passes_test(is_paciente)
def paciente_consultas(request):
    paciente = models.Paciente.objects.get(user_id=request.user.id)
    return render(request, 'accounts/paciente_consultas.html', {'paciente': paciente})


@login_required(login_url='pacientelogin')
@user_passes_test(is_paciente)
def paciente_notificacoes(request):
    paciente = models.Paciente.objects.get(user_id=request.user.id)
    return render(request, 'accounts/paciente_notificacoes.html', {'paciente': paciente})


@login_required(login_url='pacientelogin')
@user_passes_test(is_paciente)
def paciente_historico(request):
    paciente = models.Paciente.objects.get(user_id=request.user.id)
    return render(request, 'accounts/paciente_historico.html', {'paciente': paciente})


@login_required(login_url='pacientelogin')
@user_passes_test(is_paciente)
def paciente_agendar_consulta(request):
    paciente = models.Paciente.objects.get(user_id=request.user.id)
    return render(request, 'accounts/paciente_agendar_consulta.html', {'paciente': paciente})


@login_required(login_url='pacientelogin')
@user_passes_test(is_paciente)
def paciente_dados(request):
    userForm = forms.PacienteRegisterForm()
    pacienteForm = forms.PacienteForm()
    mydict = {'userForm': userForm, 'pacienteForm': pacienteForm}
    if request.method == 'POST':
        userForm = forms.PacienteRegisterForm(request.POST)
        pacienteForm = forms.PacienteForm(request.POST, request.FILES)
        if userForm.is_valid() and pacienteForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            paciente = pacienteForm.save(commit=False)
            paciente.user = user
            paciente = paciente.save()
            grupo_paciente = Group.objects.get_or_create(name='PACIENTE')
            grupo_paciente[0].user_set.add(user)
        return HttpResponseRedirect('pacientelogin')
    return render(request, 'accounts/paciente_dados.html', context=mydict)
