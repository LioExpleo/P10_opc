from rest_framework import permissions

from .models import Projects, Contributor

from .serializers import Projects

class UserAuthentif(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False



class UserIsContribProject(permissions.BasePermission):

    print("Permission : UserIsContribProject")

    def has_object_permission(self, request, view, obj):
        # print("You are here : IsAuthorOfProject.has_permission")
        print()
        print("request_method : ", (request.method))
        print("request_user : ", request.user)

        print("DONNEES DE LA TABLE PROJET")
        print("objet_project_id : ", obj.project_id)
        print("objet_title : ", obj.title)
        print("objet_description : ", obj.description)
        print("objet_type : ", obj.type)
        print("objet_author_user_id : ", obj.author_user_id)
        print("objet_contributors : ", obj.contributors.all())


        if (
            #request.method == "POST"
            #or request.method == "PUT"
            request.method == "PUT"
            or request.method == "DELETE"
            #or request.method == "POST"
        ):
            user = request.user
            print("USER", user)
            print("VIEW.KWARGS", view.kwargs)
            print("USER_ID", user.id)
            '''
            try:
                project_id = view.kwargs["projects_pk"]
                print("PROJECT_ID", project_id)
            except:
                project_id = view.kwargs.get('pk')
                #project_id = view.kwargs["pk"]
                #project_id = 32
                print("PROJECT_ID", project_id)
            try:
                contributor_instance = Contributor.objects.get(
                    user_id=user.id, project_id=project_id
                )
                print("======== CONTRIBUTOR_INSTANCE ========", contributor_instance)
                print()
                if contributor_instance.role == "AUTHOR":
                    print("PERMISSION GRANTED")
                    return True
            except:
                print("Contributor_instance does not exist")
                print("PERMISSION DENIED")
            '''
            print("PERMISSION DENIED")
            return False



        elif request.method == "GET":
            return True
        elif request.method == "POST":
            return True



#--------------------------------------------------------------------------




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
'''
class UserIsContribProjet(permissions.BasePermission): # Le user authentifié est le contributeur du projet
    def has_object_permission(self, request, view, obj):
        if obj.contributors == request.user: # si l'utilisateur connecté fait partie des contributeurs du modele projet
            return True
        return False
'''
class UserIsContribProjetcxxx(permissions.BasePermission): # Le user authentifié est le créateur du projet
    #def has_permission(self, request, view):
    #    return request.user and request.user.is_authenticated
    '''
    def has_permission(self, request, view):
        # si authorisation connecté est autentifié post ok
        if request.user.is_authenticated:
            return True
        return False
    '''
    def has_object_permission(self, request, view, obj):
        if obj.contributors == request.user: # si l'utilisateur connecté est dans liste des contributeurs projet
            return True
        return False

class UserIsContribProjetDetail(permissions.BasePermission): # Le user authentifié est le créateur du projet
    #def has_permission(self, request, view):
    #    return request.user and request.user.is_authenticated
    def has_permission(self, request, view):
        # si authorisation connecté est autentifié post ok
        if request.user.is_authenticated:
            return False
        return False
    def has_object_permission(self, request, view, obj):
        if request.user in obj.contributors.all(): # si l'utilisateur connecté est dans liste des contributeurs projet
            return True
        return False





