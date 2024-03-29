from auth0.api_conn import get_auth0_user
from .models import Users


class AuthUser:
    def __init__(self, auth0, user):
        self.auth0_name = auth0['name']
        self.auth0_id = auth0['user_id']
        self.auth0 = auth0
        self.data = user


def get_user(request):
    user = request.user
    authorized_user = get_auth0_user(user.email)
    if not find(authorized_user):
        user = Users(auth0_id=authorized_user['user_id'], role='user')
        user.save()
    else:
        user = Users.objects.get(auth0_id=authorized_user['user_id'])
    return AuthUser(authorized_user, user)


def find(auth0_user):
    return Users.objects.filter(auth0_id=auth0_user['user_id']).exists()


def get_user_object(request):
    user = request.user
    authorized_user = get_auth0_user(user.email)
    if not find(authorized_user):
        return
    user = Users.objects.get(auth0_id=authorized_user['user_id'])
    return user


def is_authenticated(request):
    return not(request.user.is_anonymous)


def get_all_users():
    return Users.objects.all()


def anonimate_user(id):
    user = Users.objects.get(id=id)
    user.auth0_id = 'removed'
    user.save()
    return
