from django.shortcuts import render, reverse, HttpResponseRedirect
from tracker.models import MyUser, Bug
from tracker.forms import LoginForm, SignupForm, BugForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bugtracker import settings

# Create your views here.
@login_required
def index(request):
    data = Bug.objects.all()
    return render(request, 'index.html', {'data': data})

@login_required
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(
                username=data['username'],
                displayname=data['displayname'],
                password=data['password1'],
            )
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()
    return render(request, 'SignupForm.html', {'form': form})

def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate( 
                request, 
                username = data['username'], 
                password = data['password']
                )
            if user:
                login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next' , reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'LoginForm.html', {'form': form})

def addBug(request, id):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.get(id=id)
            Bug.objects.create(
                title=data['title'],
                description=data['description'],
                author=user
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = BugForm()
    return render(request, 'addBug.html', {'form': form})

@login_required
def EditBug(request, id):
    bug = Bug.objects.get(id=id)
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            bug.title = data['title']
            bug.description = data['description']
            bug.save()
        return HttpResponseRedirect(reverse('buginfo', args=(id,)))
    form = BugForm(initial={
        'title': bug.title,
        'description': bug.description,
    })
    return render(request, 'addBug.html', {'form': form})

@login_required
def buginfo(request, id):
    bug = Bug.objects.get(id=id)
    return render(request, 'buginfo.html', {'bug': bug})

@login_required
def AuthorInfo(request, id):
    assigned = Bug.objects.filter(assigned_to=id)
    done = Bug.objects.filter(completed_by=id)
    author = Bug.objects.filter(author=id)
    return render(request,'authorinfo.html', {'assigned': assigned, 'author': author, 'done': done})

@login_required
def InProgress(request, id):
    bug = Bug.objects.get(id=id)
    bug.status = "In Progress"
    bug.assigned_to = request.user
    bug.completed_by = None
    bug.save()
    return HttpResponseRedirect(reverse('buginfo', args=(id,)))

@login_required
def Done(request, id):
    bug = Bug.objects.get(id=id)
    bug.status = "Done"
    bug.completed_by = request.user
    bug.assigned_to = None
    bug.save()
    return HttpResponseRedirect(reverse('buginfo', args=(id,)))

@login_required
def Invalid(request, id):
    bug = Bug.objects.get(id=id)
    bug.status = "Invalid"
    bug.assigned_to = None
    bug.completed_by = None
    bug.save()
    return HttpResponseRedirect(reverse('buginfo', args=(id,)))

def logoutview(request):
    logout(request)
    messages.info(request, 'Logged out successfully!')
    return HttpResponseRedirect(reverse('homepage'))
