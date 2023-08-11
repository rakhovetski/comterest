from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.core.paginator import Paginator
from account.models import Profile, Role, Team
from django.contrib.auth.models import User


def home(request):
    return render(request,
                  'search/main.html')


def profile_list(request, filter_slug=None):
    if not request.user.is_authenticated:
        messages.success(request, 'You must logged in')
        return redirect('search:home')

    if filter_slug:
        profiles = Profile.objects.filter(user__portfolio_projects__role__slug=filter_slug)
    else:
        profiles = Profile.objects.exclude(user=request.user)
    paginator = Paginator(profiles, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'search/profiles_list.html', {'page_obj': page_obj})


def team_list(request, pk=None):
    if not request.user.is_authenticated:
        messages.success(request, 'You must logged in')
        return redirect('search:home')

    if pk:
        teams = Team.objects.filter(pk=pk)
    else:
        teams = Team.objects.all()
    paginator = Paginator(teams, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'search/teams_list.html', {'page_obj': page_obj})


class RoleListView(ListView):
    model = Role
    template_name = 'search/roles_list.html'
    context_object_name = 'roles'


def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        searched = User.objects.filter(username__contains=search)
        return render(request,
                      'search/search.html',
                      {'search': search,
                       'searched': searched})
    return render(request,
                  'search/search.html', {})