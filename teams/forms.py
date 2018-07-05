from django import forms
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from organizations.backends import invitation_backend
from .models import TeamMember, Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name', )

class TeamMemberAdminForm(forms.ModelForm):
    """
    Form class for editing OrganizationMembers *and* the linked user model.
    """
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        exclude = ('user', 'is_admin')
        model = TeamMember

    def __init__(self, *args, **kwargs):
        super(TeamMemberAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk is not None:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email

    def save(self, *args, **kwargs):
        """
        This method saves changes to the linked user model.
        """
        if self.instance.pk is None:
            site = Site.objects.get(pk=settings.SITE_ID)
            self.instance.user = invitation_backend().invite_by_email(
                    self.cleaned_data['email'],
                    **{'first_name': self.cleaned_data['first_name'],
                        'last_name': self.cleaned_data['last_name'],
                        'organization': self.cleaned_data['organization'],
                        'domain': site})
        self.instance.user.first_name = self.cleaned_data['first_name']
        self.instance.user.last_name = self.cleaned_data['last_name']
        self.instance.user.email = self.cleaned_data['email']
        self.instance.user.save()
        return super(TeamMemberForm, self).save(*args, **kwargs)

class TeamMemberForm(forms.ModelForm):
    """
    Form class for editing OrganizationMembers *and* the linked user model.
    """
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        exclude = ('user', 'organization')
        model = TeamMember

    def __init__(self, *args, **kwargs):
        super(TeamMemberForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        """
        This method saves changes to the linked user model.
        """
        # Hack in the organization field since we excluded it manually
        self.instance.organization = kwargs.pop('team')
        if self.instance.pk is None:
            site = Site.objects.get(pk=settings.SITE_ID)
            self.instance.user = invitation_backend().invite_by_email(
                    self.cleaned_data['email'],
                    **{'first_name': self.cleaned_data['first_name'],
                        'last_name': self.cleaned_data['last_name'],
                        'organization': self.instance.organization,
                        'domain': site})
        self.instance.user.first_name = self.cleaned_data['first_name']
        self.instance.user.last_name = self.cleaned_data['last_name']
        self.instance.user.email = self.cleaned_data['email']
        self.instance.user.save()
        return super(TeamMemberForm, self).save(*args, **kwargs)

