from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Team
from .forms import TeamForm, TeamMemberForm

# Create your views here.

@login_required
def view(request, team_slug=None):
    team = Team.objects.get(slug=team_slug)
    lunches = team.lunches.all()
    members = team.users.all()
    return render(request, 'teams/view.html', {'lunches': lunches, 'members': members, 'team':team})

@login_required
def create(request):
    form = TeamForm(request.POST or None)
    if form.is_valid():
        team = form.save()
        # Add the current user to the team
        # Since this is the first user, they will automatically be the admin and owner
        team.add_user(request.user)
        return redirect('teams:view', team.slug)
    return render(request, 'teams/create.html', {'form':form})

@login_required
def invite(request, team_slug=None):
    team = Team.objects.get(slug=team_slug)
    form = TeamMemberForm(request.POST or None)
    if form.is_valid():
        user = form.save(team=team)
        return redirect('teams:view', team.slug)
    else:
        print(form.errors)
    return render(request, 'teams/invite.html', {'form':form})
