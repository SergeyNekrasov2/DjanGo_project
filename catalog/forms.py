import os
from django import forms
from .models import Product
from django.core.exceptions import ValidationError


# Список запрещённых слов
FORBIDDEN_WORDS = {"казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"}

def validate_no_forbidden_words(value):
    lower_value = value.lower()
    for word in FORBIDDEN_WORDS:
        if word in lower_value:
            raise ValidationError(f'Уберите спам!')

def validate_image(image):
    # Проверяем размер (5MB = 5 * 1024 * 1024 байт)
    max_size = 5 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError("Размер изображения не должен превышать 5MB.")

    # Проверяем формат (только JPEG и PNG)
    valid_extensions = {'.jpg', '.jpeg', '.png'}
    ext = os.path.splitext(image.name)[1].lower()
    if ext not in valid_extensions:
        raise ValidationError("Допустимые форматы изображений: JPEG, PNG.")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['names', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['names'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите название продукта'  # Текст подсказки внутри поля
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите описание'  # Текст подсказки внутри поля
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'accept': 'image/*'  # Разрешаем только изображения
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control'  # Добавление CSS-класса для стилизации поля
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите цену'  # Текст подсказки внутри поля
        })


    def clean(self):
        cleaned_data = super().clean()
        names = cleaned_data.get('names')
        description = cleaned_data.get('description')
        validate_no_forbidden_words(names)
        validate_no_forbidden_words(description)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не должна быть отрицательной')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            validate_image(image)
        return image


# class ProductModeratorForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['published']
