from rest_framework import permissions

class IsOrganizerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow organizers to edit their own profile.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
            
        # Write permissions are only allowed to the organizer's user
        return obj.user == request.user 