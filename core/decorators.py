from django.http import HttpResponse
from functools import wraps


def admin_only(func):
    @wraps(func)
    def decorator(request, *args, **kwargs):
        if request.user.groups.filter(name='admin').exists():
            return func(request, *args, **kwargs)
        return HttpResponse('<b>You are not allowed to visit this page</b>')
    return decorator
