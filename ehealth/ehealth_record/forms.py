from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from django.contrib.auth.models import User
from .models import User, Ailment, Record, Appointment


# Create your forms here.
class UserForm(UserCreationForm):
	first_name = forms.CharField(label="First Name", max_length=20, required=True)
	last_name = forms.CharField(label="Last Name", max_length=20, required=True)
	phone_number = forms.CharField(label="Phone No", max_length=20, required=True)
	CHOICES = [('User Patient', 'User/Patient'), ('Health Worker', 'Health Worker'), ]
	role = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, label="User Role", required=True)
	
	class Meta:
		model = User
		fields = ('email',)

	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.phone_number = self.cleaned_data['phone_number']
		user.role = self.cleaned_data['role']
		if commit:
			user.save()
		return user

class UserCreationForm(UserCreationForm):
	first_name = forms.CharField(label="First Name", max_length=20, required=True)
	last_name = forms.CharField(label="First Name", max_length=20, required=True)
	phone_number = forms.CharField(label="Phone No", max_length=20, required=True)
	CHOICES = [('User Patient', 'User/Patient'), ('Health Worker', 'Health Worker'), ]
	role = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, label="User Role", required=True)

	class Meta:
		model = User
		fields = ('email',)
		
class UserChangeForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('email',)
        
	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		user.phone_number = self.cleaned_data['phone_number']
		user.role = self.cleaned_data['role']
		if commit:
			user.save()
		return user

class AppointmentForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(AppointmentForm, self).__init__(*args, **kwargs)
		self.fields['user'].choices = [
			(patient.id, patient) for patient in User.objects.filter(role='User Patient').values()
		]
		self.fields['appointment_consultant'].choices = [
			(healthworker.id, healthworker) for healthworker in User.objects.filter(role='Health Worker').values()
		]

	class Meta:
		model = Appointment
		fields = '__all__'

	def save(self, commit=True):
		appointment = super(AppointmentForm, self).save(commit=False)
		appointment.user = self.cleaned_data['user']
		appointment.appointment_consultant = self.cleaned_data['appointment_consultant']
		if commit:
			appointment.save()
		return appointment
	
class RecordForm(forms.Form):
	user = forms.ChoiceField(
		choices=[(user.pk, user.first_name+" "+user.last_name) for user in User.objects.all()]
	)
	ailment = forms.ChoiceField(
		choices=[(ailment.pk, ailment.name) for ailment in Ailment.objects.all()]
	)
	diagnosis = forms.CharField(
        label='Diagnosis', required=False, widget=forms.Textarea(attrs={'rows':2})
    )
	prescription = forms.CharField(
        label='Prescription', required=False, widget=forms.Textarea(attrs={'rows':2})
    )
	ailment = forms.ChoiceField()
	
	def __init__(self, *args, **kwargs):
		super(RecordForm, self).__init__(*args, **kwargs)

		self.fields['ailment'].choices = [
			(ailment.pk, ailment) for ailment in Ailment.objects.all()
		]
	
	class Meta:
		model = Record
		fields = '__all__'

	def save(self, commit=True):
		record = super(RecordForm, self).save(commit=False)
		record.ailment = self.cleaned_data['ailment']
		record.diagnosis = self.cleaned_data['diagnosis']
		record.prescription = self.cleaned_data['prescription']
		if commit:
			record.save()
		return record