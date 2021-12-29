from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Project


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        projects = Project.objects.all()
        names = [(p.id, p.get_name()) for p in projects]

        self.fields['project'].choices = names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
