from rest_framework import permissions

class IsBusinessAndAuthenticated(permissions.BasePermission):
    
    def has_permission(self, request, view):

        is_authenticated = bool(request.user and  request.user.is_authenticated)
        if request.method  in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST' and is_authenticated:
            is_business = bool(request.user.profile.type == 'business')
            return is_business
        elif request.method in ['DELETE','PATCH', 'PUT']:
            return False
        

class IsBusinessAndOwner(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):

        is_authenticated = bool(request.user and  request.user.is_authenticated)
        if request.method  in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST' and is_authenticated:
            is_business = bool(request.user.profile.type == 'business')
            return  is_business
        elif request.method in ['DELETE','PATCH'] and is_authenticated:
            is_owner = bool( obj.user == request.user.profile)
            return bool(request.user.is_superuser or is_owner)
        

class IsAuthorized(permissions.BasePermission):
    
    def has_permission(self, request, view):

        is_authenticated = bool(request.user and  request.user.is_authenticated)
        if request.method  in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST' and is_authenticated:
            is_customer = bool(request.user.profile.type == 'customer')
            return is_customer
        elif request.method == 'DELETE' and is_authenticated:
            return request.user.is_superuser
        elif request.method in ['PUT', 'PATCH']:
            return False
        

        

class IsBusinessUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        is_authenticated = bool(request.user and  request.user.is_authenticated)
        if request.method  in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST':
            is_customer = bool(request.user.profile.type == 'customer')
            return bool(is_authenticated and is_customer) 
        elif request.method == 'DELETE':
            return bool( is_authenticated )
        elif is_authenticated and request.method in ['DELETE','PATCH']:
            is_admin = bool(request.user.is_superuser)
            is_owner = bool(obj.offer_detail.offer.first().user == request.user.profile)
            return bool( is_admin or is_owner)
        elif request.method == 'PUT':
            return False