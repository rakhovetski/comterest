from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.core.paginator import Paginator
from account.models import Profile, PortfolioProject, Role


def home(request):
    return render(request,
                  'search/main.html')


def profile_list(request, filter_slug=None):
    if request.user.is_authenticated:
        if filter_slug:
            profiles = Profile.objects.filter(user__portfolio_projects__role__slug=filter_slug)
        else:
            profiles = Profile.objects.exclude(user=request.user)
        paginator = Paginator(profiles, 7)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'search/profile_list.html', { 'page_obj': page_obj})
    else:
        messages.success(request, 'You must be logged in')
        return redirect('search:home')


class RoleListView(ListView):
    model = Role
    template_name = 'search/roles_list.html'
    context_object_name = 'roles'


def validate_user_authenticated(request):
    if not request.user.is_authenticated:
        messages.success(request, 'You must be logged in')
        return redirect('search:home')