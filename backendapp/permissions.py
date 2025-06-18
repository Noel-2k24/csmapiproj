from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'RoleId') and request.user.RoleId.RoleName.lower() == 'admin'

class IsDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'RoleId') and request.user.RoleId.RoleName.lower() == 'doctor'

class IsReceptionist(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'RoleId') and request.user.RoleId.RoleName.lower() == 'receptionist'

class IsAuthenticatedStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'id') and request.user.IsActive
