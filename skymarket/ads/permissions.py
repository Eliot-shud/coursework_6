from rest_framework.permissions import BasePermission
from users.managers import UserRoles


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True

        if hasattr(obj, "owner"):
            owner = obj.owner
        elif hasattr(obj, "author"):
            owner = obj.author

        else:
            raise Exception("not Authorization")


class IsStuff(BasePermission):

    def has_permission(self, request, view):
        if request.user.roles == UserRoles.ADMIN:
            return True
