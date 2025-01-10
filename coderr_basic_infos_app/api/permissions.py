from rest_framework import permissions



class IsCustomerReviewer(permissions.BasePermission):

    def has_permission(self, request, view):
        is_authenticated = bool(request.user and  request.user.is_authenticated)
        if request.method =="GET":
            return True
        elif is_authenticated and request.method == 'POST':
            is_customer = bool(request.user.profile.type == 'customer')
            return is_customer
        elif is_authenticated and request.method =='DELETE':
            is_owner_or_admin = bool(request.user.is_superuser)
            return is_owner_or_admin


class IsCustomerAndAuthenticated(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):

        is_authenticated = bool(request.user and  request.user.is_authenticated)
        if request.method =="GET":
            return True
        elif is_authenticated and request.method == 'POST':
            is_customer = bool(obj.reviewer.type == 'customer')
            return is_customer
        elif is_authenticated and request.method in ['PUT','DELETE','PATCH']:
            is_owner_or_admin = bool( obj.reviewer == request.user.profile or request.user.is_superuser)
            return is_owner_or_admin