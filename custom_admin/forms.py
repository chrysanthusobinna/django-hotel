from django import forms
from rooms.models import RoomCategory, RoomCategoryImage

class RoomCategoryForm(forms.ModelForm):
    class Meta:
        model = RoomCategory
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
        }

class RoomCategoryImageForm(forms.ModelForm):
    class Meta:
        model = RoomCategoryImage
        fields = ['image', 'caption']
        widgets = {
            'caption': forms.TextInput(attrs={'placeholder': 'Enter image caption (optional)'}),
        } 