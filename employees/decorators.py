from django.shortcuts import redirect
def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenicated:
            fn(request,*args,**kwargs)
        else:
            return redirect("signin")
    return wrapper