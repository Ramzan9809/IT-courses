from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
        label="Имя"
    )
    surname = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Ваша фамилия'}),
        label="Фамилия"
    )
    phone = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Ваш телефон'}),
        label="Телефон"
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Ваш email'}),
        label="Email"
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Ваше сообщение'}),
        label="Сообщение"
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Имя не должно содержать цифры.")
        return name

    def clean_surname(self):
        surname = self.cleaned_data.get('surname')
        if any(char.isdigit() for char in surname):
            raise forms.ValidationError("Фамилия не должна содержать цифры.")
        return surname

   
