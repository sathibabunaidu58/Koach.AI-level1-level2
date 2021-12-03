from django.forms import ModelForm

from .models import Register

class Registration_form(ModelForm):
    class Meta:
        model=Register
        fields = '__all__'
