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
    #保存数据时做一些其他的业务逻辑处理
    def save(self,commit=False):
        obj = super().save(commit=commit)
        if obj.age <=5:
            obj.age = 18
            obj.save()
        return obj