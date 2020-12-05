from rest_framework import permissions

from api.models import UserRole


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == UserRole.ADMIN or
            request.user.is_superuser
        )


class DefaultPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return (
            request.user.is_authenticated and
            request.user.role == UserRole.ADMIN or
            request.user.is_superuser
        )


class ReviewCommentPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return (
            request.user.is_authenticated and
            request.user.role == (UserRole.MODERATOR or UserRole.ADMIN) or
            request.user == obj.author
        )
