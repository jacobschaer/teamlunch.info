from django.db import models
from organizations.models import Organization, OrganizationUser

class Team(Organization):
    class Meta:
        proxy = True

class TeamMember(OrganizationUser):
    class Meta:
        proxy = True