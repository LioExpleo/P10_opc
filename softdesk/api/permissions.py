from rest_framework import permissions

class UserAuthentif(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

class UserAuthCreatProject(permissions.DjangoModelPermissions): # Le user authentifié est le créateur du projet
    def has_object_permission(self, request, view, obj):
        if obj.author_user_id == request.user: # si l'utilisateur connecté est author_user_id
            return True
        return False

class UserAuthCreatIssue(permissions.BasePermission): # Le user authentifié est le créateur de issue
    def has_object_permission(self, request, view, obj):
        if obj.author_user_id == request.user: # si l'utilisateur connecté est author_user_id
            return True
        return False

class UserAuthCreatComment(permissions.BasePermission): # Le user authentifié est le créateur du comment


    def has_object_permission(self, request, view, obj):
        if obj.author_user_id == request.user: # si l'utilisateur connecté est author_user_id
            return True
        return False

class UserIsContribProjet(permissions.BasePermission): # Le user authentifié est le contributeur du projet
    def has_object_permission(self, request, view, obj):
        if obj.contributors == request.user: # si l'utilisateur connecté fait partie des contributeurs du modele projet
            return True
        return False

class UserIsContribContrib(permissions.BasePermission): # Le user authentifié est le créateur du projet
    #def has_permission(self, request, view):
    #    return request.user and request.user.is_authenticated
    def has_permission(self, request, view):
        # si authorisation connecté est autentifié post ok
        if request.user.is_authenticated:
            return True
    def has_object_permission(self, request, view, obj):
        if obj.user_id == request.user: # si l'utilisateur connecté fait partie des contributeurs du modele contributeur
            # return True
            return True
        return False







