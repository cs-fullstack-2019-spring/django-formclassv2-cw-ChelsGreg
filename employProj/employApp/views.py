from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm

# Create your views here.

# FOR OPENING PAGE OF SERVER
def index(request):
    return HttpResponse("Ehhh")

# TO DISPLAY/HOLD INFO WITHIN EMPLOYEE FORM
def employForm(request):
    employForm = EmployeeForm()
    context={
        "employForm": employForm
    }
    # TO SEND INFO TO HTML PAGE
    return render(request, 'employApp/index.html', context)


# TO TRANSFER INFO SUBMITTED THROUGH FORM INTO INFO-HTML PAGE/OR RETURN TO FORM PAGE
def employInfo(request):

    # IF INFO IS SUBMITTED
    if(request.method == 'POST'):

        # TO DISPLAY IN CONSOLE
        print(request.POST)

        # TO DISPLAY SPECIFIC OBJECT ENTERED ON INFO PAGE
        context={
            "name": request.POST["name"],
            "dob": request.POST["dob"],
            "position": request.POST["position"],
            "salary": request.POST["salary"],
        }

        # TO SEND INFO TO HTML PAGE
        return render(request, 'employApp/info.html', context)
    else:
        employForm = EmployeeForm()
        context = {
            "employForm": employForm,
        }
    return render(request, 'employApp/index.html', context)

