from django import forms
from .models import Customer
class CustomerAdminForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
    def clean_age(self):
        age = self.cleaned_data["age"]
        if int(age) >=120 or int(age) <= 1:
            raise forms.ValidationError("年龄只能在1-120之间")
        return age