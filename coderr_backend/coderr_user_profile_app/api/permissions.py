from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in ['GET', 'PATCH']:
            is_owner_or_admin = bool(request.user == obj.user)
            return bool(request.user.is_superuser or is_owner_or_admin)
