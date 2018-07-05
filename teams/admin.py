from django.contrib import admin
from organizations.models import (Organization, OrganizationUser,
    OrganizationOwner)
from .forms import TeamMemberAdminForm
from .models import Team, TeamMember

class TeamMemberAdmin(admin.ModelAdmin):
    form = TeamMemberAdminForm

admin.site.unregister(Organization)
admin.site.unregister(OrganizationUser)
admin.site.unregister(OrganizationOwner)
admin.site.register(Team)
admin.site.register(TeamMember, TeamMemberAdmin)