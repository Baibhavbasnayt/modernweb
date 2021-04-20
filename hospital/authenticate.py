from django.db.models import Q
from django.shortcuts import redirect

from .models import Admin


class Authenticate:
    def valid_adminlogin(function):
        def login(request):
            try:

                Admin.objects.get(Q(password=request.session['password']) & Q(email=request.session['email']))
                return function(request)

            except:
                return redirect("/login/")

        return login