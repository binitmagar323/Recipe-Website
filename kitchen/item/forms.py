from django import forms 

from .models import Item

INPUT_CLASSES = 'w-1/4 py-4 px-5 mr-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model= Item
        fields = ('name','category','image','description','ingredient','process',)

        widgets= {
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
            'category': forms.Select(attrs={
            'class': INPUT_CLASSES
        }),
            'image': forms.FileInput(attrs={
            'class': INPUT_CLASSES
        }),
           'description': forms.Textarea(attrs={
            'class': INPUT_CLASSES
        }),
            'ingredient': forms.Textarea(attrs={
            'class': INPUT_CLASSES
        }),
            'process': forms.Textarea(attrs={
            'class': INPUT_CLASSES
        })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model= Item
        fields = ('name','image','description','ingredient','process',)

        widgets= {
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
            'image': forms.FileInput(attrs={
            'class': INPUT_CLASSES
        }),
           'description': forms.Textarea(attrs={
            'class': INPUT_CLASSES
        }),
            'ingredient': forms.Textarea(attrs={
            'class': INPUT_CLASSES
        }),
            'process': forms.Textarea(attrs={
            'class': INPUT_CLASSES
        })
        }