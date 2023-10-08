from django import forms

#форма для выбора модели и версии робота, а также для указывания адреса электронной почты, на которую нужно отправить письмо
class OrderForm(forms.Form):
     models = [('R2', 'R2'),
               ('L3', 'L3'),
               ('X5', 'X5'),]
     email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': "Введите вашу почту",  'type': "text"})) 
     versions = forms.CharField(max_length=2, required=True, widget=forms.TextInput(attrs={'placeholder': "Введите версию",  'type': "text"}))
     dropdown_model = forms.ChoiceField(choices= models,)