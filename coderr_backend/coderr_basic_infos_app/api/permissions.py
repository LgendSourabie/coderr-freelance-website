from rest_framework import permissions



class IsCustomerAndAuthenticated(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):

        is_authenticated = bool(request.user and  request.user.is_authenticated)
        if request.method  in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST':
            is_customer = bool(obj.reviewer.type == 'customer')
            return bool(is_authenticated and is_customer)
        elif request.method in ['DELETE','PATCH', 'PUT']:
            is_owner_or_admin = bool( obj.reviewer == request.user or request.user.is_superuser)
            return bool( is_authenticated and is_owner_or_admin)