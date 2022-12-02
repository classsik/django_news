from django import forms


class NewsAddForm(forms.Form):
    title = forms.CharField(label='Заголовок')
    text = forms.CharField(widget=forms.Textarea, label='Текст')
    publicated = forms.BooleanField(label='Публикация')
    date = forms.DateTimeField(label='Дата публикации')

