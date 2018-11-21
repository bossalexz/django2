from django import forms
from .models import Project, Persona


class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = [
			'title',
			'description',
			'image',
		]
		labels = {
			'title' : 'titulo',
			'description' : 'descripcion',
			'image' : 'imagen',
		}
		widgets = {
			'title' : forms.TextInput(attrs={'class':'form-control'}),
			'description' : forms.TextInput(attrs={'class':'form-control'}),
			'image' : '',
		}
#forms.FileField()
class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields = [
			'username',
			'password',
			'email',
		]
		labels = {
			'username' : 'username',
			'password' : 'password',
			'email' : 'email',
		}
		widgets = {
			'username' : forms.TextInput(attrs={'class':'form-control'}),
			'password' : forms.TextInput(attrs={'class':'form-control'}),
			'email' : forms.EmailField(),
		}
#forms.FileField()
