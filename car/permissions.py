from rest_framework import permissions

#! For cars, only the get operation can be done by any user, but only the admin user can perform the post delete put operations.

class IsStaffOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return bool(request.user and request.user.is_staff)