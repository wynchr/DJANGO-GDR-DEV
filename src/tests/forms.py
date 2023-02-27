"""
=======================================================================================================================
.DESCRIPTION
    Test for TEST Application

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.01	01/01/2023  CWY	Initial Version

.COMMENTS
    .
=======================================================================================================================
"""
from django import forms

JOBS = (
    ("python", "Développeur Python"),
    ("powershell", "Développeur Powershell"),
    ("javascript", "Développeur Javascript"),
)


class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=8, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    job = forms.ChoiceField(choices=JOBS)
    cgu_accept = forms.BooleanField(initial=True)
    description = forms.CharField(max_length=200, required=False, widget=forms.Textarea())

    # validation au niveau du serveur
    def clean_pseudo(self):
        pseudo = self.cleaned_data.get("pseudo")
        if "$" in pseudo:
            raise forms.ValidationError("le pseudo ne peut pas contenir de $")
        return pseudo
