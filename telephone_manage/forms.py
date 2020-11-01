from django import forms
from django.forms import widgets, models
from telephone_manage.models import tels


class ProjectForm(forms.Form):
    name = forms.CharField(label="所属人",
                           max_length=100,
                           widget=widgets.TextInput(attrs={'class':"form-control"}))
    fund = forms.CharField(label='所属资产',
                          max_length=100,
                          widget=widgets.RadioSelect(choices=(('个人','个人'),('公司','公司'))))

    # fund = forms.CharField(label="所属资产",
    #                     max_length=100,
    #                      widget=widgets.TextInput(attrs={'class': "form-control"}))
    #sys = forms.CharField(verbose_name='系统',
    #                       max_length=5,
    #                       choices=(('ios', 'IOS'), ('android', 'Android')))
    sys = forms.CharField(label='系统',
                          max_length=100,
                          widget=widgets.RadioSelect(choices=(('IOS','IOS'),('Android','Android'))))

    type = forms.CharField(label="型号",
                           max_length=100,
                           widget=widgets.TextInput(attrs={'class': "form-control"}))
    version = forms.CharField(label="版本",
                           max_length=100,
                           widget=widgets.TextInput(attrs={'class': "form-control"}))

class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = tels
        fields = ['name','fund','sys','type','version']