from django import forms
from rooms.models import RoomCategory, RoomCategoryImage

class RoomCategoryForm(forms.ModelForm):
    class Meta:
        model = RoomCategory
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'price': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price

class RoomCategoryImageForm(forms.ModelForm):
    class Meta:
        model = RoomCategoryImage
        fields = ['image', 'caption']
        widgets = {
            'caption': forms.TextInput(attrs={'placeholder': 'Enter image caption (optional)'}),
        } 