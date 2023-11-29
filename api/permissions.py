from rest_framework.permissions import BasePermission


# RULES_CHOICES = [
#         ('Chef de délégation','Chef de délégation'),
#         ('Jury / Organisme de contrôle','Jury / Organisme de contrôle'),
#         ('Media','Media')
#     ]

class IsChefDelegation(BasePermission):
    def has_permission(self, request, view):
        # Vérifiez si l'utilisateur est authentifié
        if not request.user.is_authenticated:
            return False

        if request.user.rule == "Chef de délégation":
            return True 

        return False


