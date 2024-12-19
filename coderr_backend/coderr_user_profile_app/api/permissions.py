from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in ['GET', 'PATCH']:
            is_owner_or_admin = bool(request.user == obj.user or request.user.is_superuser)
            return bool(request.user and is_owner_or_admin)
