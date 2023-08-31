from django import forms
from core.models import Twits

class TwitForm(forms.ModelForm):
# форма для создания твита
    class Meta:
        model = Twits 
        fields = ["text", "answer_to_twit", "tag"]
        widgets = {
        "text": forms.Textarea(attrs={"placeholder": "Что нового?"}), 
        "answer_to_twit": forms.HiddenInput(),
        "tag": forms.CheckboxSelectMultiple(),
}