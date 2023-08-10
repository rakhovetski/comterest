from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, reverse
from account.forms import PortfolioProjectForm, RegisterForm, ProfilePicForm, TeamForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.detail import DetailView

from account.models import Profile, PortfolioProject, Team


def register_user(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, ('You Have successfully register'))
                return redirect('search:home')

    return render(request, 'account/register/register.html', {'form': form})


def edit_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)

        user_form = RegisterForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)

            login(request, user)

            messages.success(request, 'Your Profile Has Been Updated')
            return redirect('account:profile', pk=current_user.pk)
        return render(request, 'account/profile/edit_profile.html', {'user_form': user_form,
                                                                     'profile_form': profile_form})
    else:
        messages.success(request, 'You must be logged in')
        return redirect('search:home')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('account:profile')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have Been Logged In'))
            return redirect('search:home')
        else:
            messages.success(request, ('There was an error in logged in'))
            return redirect('account:login')
    return render(request,
                  'account/login/login.html')


def user_logout(request):
    logout(request)
    messages.success(request, ('You Have Been Logged Out'))
    return redirect('search:home')


def show_profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        projects = PortfolioProject.objects.filter(user_id=pk).order_by('-created_at')
        teams = Team.objects.filter(profile__id=profile.pk)

        if request.method == 'POST':
            current_user_profile = request.user.profile

            action = request.POST['follow']
            if action == 'unfollow':
                current_user_profile.follows.remove(profile)
            elif action == 'follow':
                current_user_profile.follows.add(profile)
            current_user_profile.save()
        context = {
            'profile': profile,
            'projects': projects,
            'teams': teams
        }
        return render(request, 'account/profile/profile.html', context=context)
    else:
        messages.success(request, 'You must logged in')
        return redirect('search:home')


def add_project(request):
    if request.user.is_authenticated:
        project_form = PortfolioProjectForm(request.POST or None)
        if request.method == 'POST':
            if project_form.is_valid():
                project = project_form.save(commit=False)
                project.user = request.user
                project_form.save_m2m()
                project.save()
                return redirect('account:profile', pk=request.user.pk)
        return render(request,
                      'account/profile/add_project.html',
                      {'project_form': project_form})
    else:
        messages.success(request, 'You must logged in')
        return redirect('search:home')


class PortfolioProjectDetailView(DetailView):
    model = PortfolioProject
    template_name = 'account/profile/show_project.html'
    context_object_name = 'project'


def add_team(request):
    if request.user.is_authenticated:
        team_form = TeamForm(request.POST or None)
        if request.method == 'POST':
            if team_form.is_valid():
                project = team_form.save(commit=False)
                project.save()
                team_form.save_m2m()
                return redirect('account:profile', pk=request.user.pk)
        return render(request,
                      'account/profile/add_team.html',
                      {'team_form': team_form})
    else:
        messages.success(request, 'You must logged in')
        return redirect('search:home')


class TeamDetailView(DetailView):
    model = Team
    template_name = 'account/profile/show_team.html'
    context_object_name = 'team'

