from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Marage

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page")
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'user':
            return redirect('userPage')
        if group == 'admin':
            return view_func(request, *args, **kwargs)
            
    return wrapper_function




# def send_or_accept(view_func):
#     def wrapper_function(request, *args, **kwargs):

#         Marage.objects.get_or_create(user=request.user) 
#         me = request.user.marage.id
#         requester = Marage.objects.get(id=me)

#         if requester.age == '' and requester.caste == '' and requester.gender == '' and requester.height == '' and  requester.profession == '' and requester.gardian_profession == '' and requester.siblings == '' and requester.married_brothers == '' and requester.married_sisters == '' and requester.marrage_times == '' and requester.state == '' and requester.country == None:

#                       js=""" alert("Add your data first ....");
#                       """
#                       context= js2py.EvalJs()
#                       context.execute(js)
#         else:
#             return view_func(request, *args, **kwargs)

#     return wrapper_function
