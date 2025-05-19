from django import forms
from rooms.models import RoomCategory, RoomCategoryImage
from cloudinary.models import CloudinaryResource


class RoomCategoryForm(forms.ModelForm):
    class Meta:
        model = RoomCategory
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'price': forms.NumberInput(attrs={'step': '0.01', 'min': '1'}),
        }

    def __init__(self, *args, **kwargs):
        self.is_edit = kwargs.pop('is_edit', False)
        super().__init__(*args, **kwargs)
        if not self.is_edit:
            self.fields['image'].required = True

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 1:
            raise forms.ValidationError("Price must be at least 1.")
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not self.is_edit and not image:
            raise forms.ValidationError(
                "Image is required for new room categories."
                )

        if image and not isinstance(image, CloudinaryResource):
            # Check file size (5MB limit)
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    "Image file size must be no more than 5MB."
                    )

            # Check file type
            allowed_types = [
                'image/jpeg', 'image/png',
                'image/gif', 'image/webp'
                ]
            if image.content_type not in allowed_types:
                raise forms.ValidationError(
                    "Image is required for new room categories."
                )
        return image


class RoomCategoryImageForm(forms.ModelForm):
    class Meta:
        model = RoomCategoryImage
        fields = ['image', 'caption']
        widgets = {
            'caption': forms.TextInput(
                attrs={'placeholder': 'Enter image caption (optional)'}
            ),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and not isinstance(image, CloudinaryResource):
            # Check file size (5MB limit)
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    "Image file size must be no more than 5MB."
                    )

            # Check file type
            allowed_types = [
                'image/jpeg', 'image/png',
                'image/gif', 'image/webp'
                ]
            if image.content_type not in allowed_types:
                raise forms.ValidationError(
                    "Only JPEG, PNG, GIF and WebP images are allowed."
                    )
        return image
