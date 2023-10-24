from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from datetime import datetime, date, timedelta
from django.views import View
from .models import User, Record, Ailment, Appointment, Appointment_Meta, State
from django.contrib import messages
from .forms import RecordForm, UserForm, AppointmentForm
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.csrf import csrf_protect
from django.db.models import Count, Q

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
    #return render(request, 'index.html')

def about_us(request):
  template = loader.get_template('about_us.html')
  return HttpResponse(template.render())

def register_request(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = UserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/dashboard")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def login_request1(request):
    if request.method == "POST":
      form = AuthenticationForm(request, data=request.POST)
      if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
          login(request, user)
          messages.info(request, f"You are now logged in as {username}.")
          return redirect("dashboard")
        else:
          messages.error(request,"Invalid username or password.")
      elif not form.is_valid():
        username = request.POST['signin_username']
        password = request.POST['signin_password']
        user = authenticate(username=username, password=password)
        if user is not None:
          login(request, user)
          messages.info(request, f"You are now logged in as {username}.")
          return redirect("dashboard")
        else:
          messages.error(request,"Invalid username or password.")
      else:
        messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")

def dashboard(request):
  if request.user.is_authenticated:
    return render(request, 'dashboard/dashboard_index.html')
  else:
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})   
    #request, 'signin.html', context={'form': form, 'message': message})

def book_appointment_request(request):
    if request.user.is_authenticated:
        user = User.objects.first()
        #user = User.objects.filter(id=request.user.id).values()
        physicians = User.objects.filter(role='Health Worker').values()
        context = {"user":user,"physicians":physicians,}
        return render(request, "dashboard/book_appointment.html", context)
    else:
        return render(request, "login.html")

def do_book_appointment(request):
    if request.user.is_authenticated:
         if request.method == 'POST':

            userId = request.POST.get('patient', 1)
            userdata = User.objects.get(pk=userId)
            consultantId = request.POST.get('consultant', 1)
            consultantdata = User.objects.get(pk=consultantId)

            appointment = Appointment.objects.create(user=userdata, appointment_consultant=consultantdata)
            appointment.description = request.POST.get('description') 
            appointment.status = "open" 
            appointment.added_by = request.user.id
            appointment.created = datetime.now()
            appointment.updated = datetime.now()
            appointment_date_time = ""
            for _key in request.POST:
                print(_key)
                if _key == "appointment_date":
                    appointmentstring = request.POST[_key]
                    appointment_date_time = datetime.strptime(appointmentstring, '%Y-%m-%d') 
                    appointment.appointment_date = appointment_date_time
            appointment.save()

            appointment_date_time = appointment_date_time

            """ appointment = appointment.objects.get(pk=insertedId.pk)
            appointment_meta = Appointment_Meta.objects.create(appointment=appointment, appointment_date_time=appointment_date_time)
            appointment_meta.defered_date_time = datetime.now()
            appointment_meta.added_by = request.user.id
            appointment_meta.created = datetime.now()
            appointment_meta.save() """
            
            email_subject = "New Medical Appointment Notification"
            username = userdata.first_name +" "+ userdata.last_name
            useremail = userdata.email
            recipient_email = consultantdata.email
            html_content = f"""
            <html>
            <head>
                <title>eHealth4Everyone | { email_subject } </title>
            </head>
            <body style="width: 80%; margin: auto"; >
            <header style='color: #000000; background-color: #79ff4d; padding: 30px;'>
            <h2>eHealth4Everyone | { email_subject }</h2>
            </header>
            <div style='background-color: #e6e600; padding: 40px;'>
            <p>This is to notify you that a patient {username}:has booked an appointment with you.</p>
            <ul>
            <li>Date: { appointment_date_time }
            <li>Email Address: { useremail }
            </ul>
            <p>You may contact him as soon as possiblet</p>
            <p>This message is sent automaticlly. If it is not meant for you, please ignore.</p>
            <p>eHealth4Everyone Team</p>
            </div>
            <footer style='color: #000000; background-color: #79ff4d; padding: 30px;'>
            <span style="font-size: 12px;">Do not at any point in time disclose your login details and other online critical data to third-party</span></br>
            <span style="font-size: 12px;">Call <strong>0767317495</strong>, or email <strong>admin@obajesoft.com.ng</strong>.</span>
            </footer>
            </body>
            </html>
            """.format(email_subject=email_subject, recipient_email=recipient_email, username=username, useremail=useremail, appointment_date_time=appointment_date_time)

            email = EmailMessage(email_subject, html_content, ["info@obajesoft.com.ng"], [recipient_email])
            email.content_subtype = "html"
            email.send()
            return render(request, "dashboard/book_appointment.html")
         
def post_record_request(request):
    if request.user.is_authenticated:
        states = State.objects.all().values()
        ailmentsdata = Ailment.objects.all().values()
        context = {'states':states, 'ailments':ailmentsdata}
        return render(request, "dashboard/post_record.html", context)
    else:
        return render(request, "login.html")

def do_post_record(request):
    if request.user.is_authenticated:
         if request.method == 'POST':
            userId = request.user.id
            userdata = User.objects.get(pk=userId)
            stateId = request.POST.get('state')
            statedata = State.objects.get(id=stateId)
            ailmentId = request.POST.get('ailment')

            user  = User.objects.get(pk=userdata.id)
            state  = State.objects.get(pk=statedata.id)
            ailment = Ailment.objects.get(pk=ailmentId)

            record = Record.objects.create(user=user, state=state, ailment=ailment)
            record.diagnosis = request.POST.get('diagnosis')
            record.prescription = ""
            record.added_by = request.user.id
            record.created = datetime.now()
            record.updated = datetime.now()
            record.save() 

            return render(request, "dashboard/post_record.html")

def view_patient_request(request):
    if request.user.is_authenticated:
        patients = User.objects.select_related().filter(role="User Patient").all()
        ailments = Ailment.objects.all().values()
        context = {"patients":patients, "ailments":ailments}
        return render(request, "dashboard/view_patient.html", context)
    else:
        return render(request, "login.html")

def patient_request(request, id):
    if request.user.is_authenticated:
        user = User.objects.filter(id=id).get()
        patient = User.objects.get(pk=id)
        records = Record.objects.filter(user=user).values()
        context = {"patient":patient, "records":records}
        return render(request, "dashboard/patient.html", context)
    else:
        return render(request, "login.html")
    
def view_record_request(request):
    if request.user.is_authenticated:
        records = Record.objects.select_related().all()
        ailments = Ailment.objects.all().values()
        context = {"records":records, "ailments":ailments}
        return render(request, "dashboard/view_record.html", context)
    else:
        return render(request, "login.html")
    
def view_statistics_request(request):
    if request.user.is_authenticated:
        patientrecord = Record.objects.select_related().all()
        ailments = Ailment.objects.annotate(num=Count("record"))
        
        datapoints = list()
        for x in ailments:
            datapoints.append({ "label": x.name,  "y": x.num  })

        context = {"patientrecord":patientrecord, "datapoints" : datapoints}
        return render(request, "dashboard/view_statistics.html", context)
    else:
        return render(request, "login.html")

def getRecordsByAilment(request):
    patient = request.GET.get('p')

    #userdata = User.objects.get(pk=patient).values()
    queryset = User.objects.raw('SELECT * FROM User')
    appointments = list(queryset) 
    response_data = {
        "appointments": appointments,
	}
    return JsonResponse(response_data)

def getPatientAppointment(request):
  patient = request.GET.get('p')
  user = User.objects.filter(id=int(patient)).get()
  appointments = Appointment.objects.filter(user=user)

  appointmentdata = {}
  for appointment in appointments:
        appointmentdata = Appointment.objects.filter(user=user).values('id', 'status')
  appointments = list(appointmentdata)
  response_data = {
    "appointments": appointments,
	}
  return JsonResponse(response_data)

def getPatientByAilment(request):
    ailmentid = request.GET.get('p')
    ailment = Ailment.objects.filter(pk=int(ailmentid)).get()
    recordspatients = Record.objects.filter(ailment=ailment).values('user_id')
    #recordspatients = Record.objects.filter(ailment=ailment).annotate(count=Count('user')).values()
    #print(recordspatients)
    thelist = []
    for x in recordspatients:
        thelist.append(x["user_id"])
    uniquepatient = list(set(thelist))
    
    patientsdata = []
    for patient in uniquepatient:
        patientsdata = User.objects.filter(id=patient).values()
    patients = list(patientsdata)

    response_data = {
        "patients": patients,
    }
    return JsonResponse(response_data)

def getPhysicianByName(request):
    patient_name = request.GET.get('p')

    #physicians = User.objects.filter(role='Health Worker').filter(Q(first_name__contains=patient_name) | Q(last_name__contains=patient_name))
    physicians = User.objects.filter(role='Health Worker').filter(first_name__contains=patient_name)
    physiciandata = {}
    for physician in physicians:
        physiciandata = User.objects.filter(id=physician.id).values()
    physician = list(physiciandata)
    response_data = {
        "physician": physician,
    }
    return JsonResponse(response_data)


def getPatientAppointment(request):
  patient = request.GET.get('p')
  user = User.objects.filter(id=int(patient)).get()
  appointments = Appointment.objects.filter(user=user)

  appointmentdata = {}
  for appointment in appointments:
        appointmentdata = Appointment.objects.filter(user=user).values('id', 'status')
  appointments = list(appointmentdata)
  response_data = {
    "appointments": appointments,
	}
  return JsonResponse(response_data) 


def view_request_my_appointments(request):
    if request.user.is_authenticated:
        userId = request.POST.get('patient', 1)
        userdata = User.objects.get(pk=userId)
        physicianId = request.user.id
        physiciandata = User.objects.get(pk=physicianId)
        appointments = Appointment.objects.filter(appointment_consultant=physiciandata).select_related('user')

        context = {"appointments":appointments}
        return render(request, "dashboard/view_my_appointments.html", context)
    else:
        return render(request, "login.html")

def view_Appointment_Confirms(request, id, confvalue):
    #appointid = request.GET.get('id')
    #confvalue = request.GET.get('confvalue')
    if request.user.is_authenticated:
        appointment = Appointment.objects.get(pk=id)
        appointment.status = confvalue
        appointment.save()

        return render(request, "dashboard/appointment_confirmation.html")
    else:
        return render(request, "login.html")


