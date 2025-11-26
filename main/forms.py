from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=100)
    phone = forms.CharField(label='電話番号', max_length=20)
    email = forms.EmailField(label='メールアドレス')
    message = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea)


class ReservationForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=100)
    phone = forms.CharField(label='電話番号', max_length=20)
    email = forms.EmailField(label='メールアドレス')
    people = forms.IntegerField(label='人数', min_value=1)
    date = forms.DateField(label='予約日', widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(label='予約時間', widget=forms.TimeInput(attrs={'type': 'time'}))