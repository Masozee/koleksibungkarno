from django import forms

from .models import Inquiry


class InquiryForm(forms.ModelForm):
    Nama = forms.CharField(required=True, max_length=50)
    Email = forms.EmailField(required=True)
    Judul = forms.CharField(required=True, max_length=50)
    Pertanyaan = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Inquiry
        fields = ('Nama', 'Email', 'Judul', 'Pertanyaan')



