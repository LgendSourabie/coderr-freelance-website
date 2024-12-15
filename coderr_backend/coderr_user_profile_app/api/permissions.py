from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in ['GET', 'PATCH']:
            return bool(request.user and request.user == obj.user or request.user.is_superuser)
