from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user:
            # return account == request.user
            return obj == request.user
        return False