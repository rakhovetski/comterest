from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from account.models import Profile
from team.forms import TeamForm
from team.models import Team


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
                  'team/add_team.html',
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
    return render(request, 'team/edit_team.html', {'team_form': team_form,})


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
            messages.success(request, 'If you want to delete the Team, you need to check the box')
            return redirect('account:team:delete_team', pk=pk)
    return render(request,
                  'team/confirm_delete_team.html',
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
    return render(request, 'team/show_team.html', context=context)
