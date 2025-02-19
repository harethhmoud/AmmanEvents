from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from organizers.models import Organizer
#from events.models import Event, TicketTier
#from tickets.models import Ticket
# Register your models here.

admin.site.register(User, UserAdmin)

#admin.site.register(Organizer)

#admin.site.register(Event)

#admin.site.register(Ticket)

#admin.site.register(TicketTier)

