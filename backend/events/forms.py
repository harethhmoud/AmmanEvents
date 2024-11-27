from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from .models import Event

# Creating custom form coz Django DateTime does not support what I want
class EventAdminForm(forms.ModelForm):
    class Meta:
        model = Event # linking form to event model
        fields = '__all__' # all fields in the model are included
        widgets = { 
            'date': AdminSplitDateTime(),
        }
