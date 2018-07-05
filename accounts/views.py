from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth.models import User
from teams.models import TeamMember, Team


# Create your views here.
@login_required
def profile(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    form = UserForm(instance=request.user)
    teams = request.user.organizations_organization.all()
    return render(request, 'accounts/profile.html', {'form': form, 'teams': teams})