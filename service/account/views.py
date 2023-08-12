from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, reverse, get_object_or_404
from account.forms import PortfolioProjectForm, RegisterForm, ProfileForm, TeamForm
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
    if not request.user.is_authenticated:
        messages.success(request, 'You must logged in')
        return redirect('search:home')

    current_user = User.objects.get(id=request.user.id)
    profile_user = Profile.objects.get(user__id=request.user.id)

    user_form = RegisterForm(request.POST or None, request.FILES or None, instance=current_user)
    profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=profile_user)

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
    if not request.user.is_authenticated:
        messages.success(request, 'You must logged in')
        return redirect('search:home')

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


def add_project(request):
    if not request.user.is_authenticated:
        messages.success(request, 'You must logged in')
        return redirect('search:home')

    project_form = PortfolioProjectForm(request.POST or None)
    if request.method == 'POST':
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.user = request.user
            project.save()
            project_form.save_m2m()
            return redirect('account:profile', pk=request.user.pk)
    return render(request,
                  'account/profile/add_project.html',
                  {'project_form': project_form})


def edit_project(request, pk):
    if not request.user.is_authenticated:
        messages.success(request, 'You must logged in')
        return redirect('search:home')

    project = get_object_or_404(PortfolioProject, pk=pk)
    project_form = PortfolioProjectForm(request.POST or None, instance=project)

    if request.user.id != project.user.id:
        messages.success(request, 'You Can\'t Edit That Project!')
        return redirect('search:home')

    if project_form.is_valid():
        project_form.save()
        messages.success(request, 'Your Project Has Been Updated')
        return redirect('account:profile', pk=request.user.pk)
    return render(request, 'account/profile/edit_project.html', {'project_form': project_form})


def delete_project(request, pk):
    if not request.user.is_authenticated:
        messages.success(request, 'You must logged in')
        return redirect('search:home')

    project = get_object_or_404(PortfolioProject, pk=pk)
    if request.method == 'POST':
        if request.user.id == project.user.id:

            confirm_delete = request.POST.get('confirm_delete')

            if confirm_delete:
                project.delete()
                messages.success(request, 'Your Project Has Been Deleted')
                return redirect('account:profile', pk=request.user.pk)
            else:
                messages.success(request, 'If you want to delete the project, you need to check the box')
                return redirect('account:delete_project', pk=pk)
        else:
            messages.success(request, 'You Can\'t Delete That Project!')
            return redirect('search:home')
    return render(request,
                  'account/profile/confirm_delete_project.html',
                  {'pk': pk})


class PortfolioProjectDetailView(DetailView):
    model = PortfolioProject
    template_name = 'account/profile/show_project.html'
    context_object_name = 'project'


def add_team(request):
    if not request.user.is_authenticated:
        messages.success(request, 'You must logged in')
        return redirect('search:home')

    team_form = TeamForm(request.POST or None)
    if request.method == 'POST':
        if team_form.is_valid():
            team = team_form.save(commit=False)
            profile = Profile.objects.get(id=request.user.id)
            team.owner = profile
            team.save()
            team.profile.add(profile)
            team_form.save_m2m()
            return redirect('account:profile', pk=request.user.pk)
    return render(request,
                  'account/team/add_team.html',
                  {'team_form': team_form})


def edit_team(request, pk):
    if not request.user.is_authenticated:
        messages.success(request, 'You must logged in')
        return redirect('search:home')

    team = get_object_or_404(Team, id=pk)

    if request.user.id != team.owner.id:
        messages.success(request, 'You Can\'t Edit That Team!')
        return redirect('search:home')

    team_form = TeamForm(request.POST or None, request.FILES or None, instance=team)

    if team_form.is_valid():
        team_updated = team_form.save(commit=False)
        team_updated.owner = team.owner
        team_updated.save()

        team_form.save_m2m()
        messages.success(request, 'Your Team Has Been Updated')
        return redirect('account:profile', pk=request.user.pk)
    return render(request, 'account/team/edit_team.html', {'team_form': team_form,})


def delete_team(request, pk):
    if not request.user.is_authenticated:
        messages.success(request, 'You must logged in')
        return redirect('search:home')

    if request.method == 'POST':
        team = get_object_or_404(Team, id=pk)

        if request.user.id != team.owner.id:
            messages.success(request, 'You Can\'t Delete That Team!')
            return redirect('search:home')

        confirm_delete = request.POST.get('confirm_delete')

        if confirm_delete:
            team.delete()
            messages.success(request, 'Your Team Has Been Deleted')
            return redirect('account:profile', pk=request.user.pk)
        else:
            messages.success(request, 'If you want to delete the project, you need to check the box')
            return redirect('account:delete_project', pk=pk)
    return render(request,
                  'account/team/confirm_delete_team.html',
                  {'pk': pk})


def show_team(request, pk):
    if not request.user.is_authenticated:
        messages.success(request, 'You must logged in')
        return redirect('search:home')

    team = Team.objects.get(pk=pk)
    profile = Profile.objects.get(user__id=request.user.id)
    team_profiles = team.profile.filter(pk=profile.pk)

    if request.method == 'POST':

        action = request.POST['follow']
        if action == 'unfollow':
            profile.teams.remove(team)
        elif action == 'follow':
            profile.teams.add(team)
        profile.save()
    context = {
        'profile': profile,
        'team': team,
        'team_profiles': team_profiles
    }
    return render(request, 'account/team/show_team.html', context=context)

