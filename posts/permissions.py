from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    '''
        TASK: Override the has_object_permission to 
         allow read-only for all requests but for edit and delete,
         the author must be the same as the current logged-in user
    '''

    def has_object_permission(self, request, view, obj):
        # read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS: # SAFE_METHODS is a tuple containing GET, OPTIONS, and HEAD. Signifies read-only request
            return True
        
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user