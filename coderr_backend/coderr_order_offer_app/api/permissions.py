from rest_framework import permissions

class IsBusinessAndAuthenticated(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):

        is_authenticated = bool(request.user and  request.user.is_authenticated)
        if request.method  in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST':
            is_business = bool(request.user.profile.type == 'business')
            return bool(is_authenticated and is_business)
        elif request.method in ['DELETE','PATCH', 'PUT']:
            is_owner_or_admin = bool( obj.user == request.user or request.user.is_superuser)
            return bool( is_authenticated and is_owner_or_admin)
        


class IsAuthorized(permissions.BasePermission):
    
    def has_permission(self, request, view):

        is_authenticated = bool(request.user and  request.user.is_authenticated)
        if request.method  in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST':
            is_customer = bool(request.user.profile.type == 'customer')
            return bool(is_authenticated and is_customer) 
        elif request.method == 'DELETE':
            return bool( is_authenticated and request.user.is_superuser)
        # elif request.method == 'PATCH':
        #     return bool( is_authenticated and obj.offer_detail.offer.first().user == request.user.profile)
        elif request.method == 'PUT':
            return False
        
