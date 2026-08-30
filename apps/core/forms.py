from django import forms
from .models import ContactMessage, JobOffer

class ContactForm(forms.ModelForm):
    # Honeypot field for bot protection (should be left empty by real humans)
    website_url = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'style': 'display:none !important;', 'tabindex': '-1', 'autocomplete': 'off'})
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your full name',
                'required': True,
                'aria-required': 'true'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'your.email@example.com',
                'required': True,
                'aria-required': 'true'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Subject or Project Idea',
                'required': True,
                'aria-required': 'true'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'How can we work together or collaborate?',
                'rows': 5,
                'required': True,
                'aria-required': 'true'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('website_url'):
            raise forms.ValidationError("Spam detected.")
        return cleaned_data


class JobOfferForm(forms.ModelForm):
    # Honeypot field for bot protection
    website_url = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'style': 'display:none !important;', 'tabindex': '-1', 'autocomplete': 'off'})
    )

    class Meta:
        model = JobOffer
        fields = [
            'company_name', 'contact_person', 'contact_email', 'contact_phone', 'company_website',
            'job_title', 'job_category', 'employment_type', 'work_location',
            'offered_salary', 'salary_currency', 'expected_start_date',
            'job_description'
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. GIRA Ltd, GCIC Rwanda, Tech Institute',
                'required': True
            }),
            'contact_person': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Hiring Manager or Recruiter Name',
                'required': True
            }),
            'contact_email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'recruiter@company.com or hr@company.rw',
                'required': True
            }),
            'contact_phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '+250 78X XXX XXX / WhatsApp',
            }),
            'company_website': forms.URLInput(attrs={
                'class': 'form-input',
                'placeholder': 'https://company.rw or organization website',
            }),
            'job_title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. IT Officer, Systems Administrator, Full-Stack Django Developer',
                'required': True
            }),
            'job_category': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'employment_type': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'work_location': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. Kigali (Kacyiru / Nyarugenge), Remote, or Hybrid',
                'required': True
            }),
            'offered_salary': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. 1,500,000 RWF / month, $2,500 USD / month, or Project Budget',
                'required': True
            }),
            'salary_currency': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'expected_start_date': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. Immediate, Next 2 weeks, or Next Month',
            }),
            'job_description': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Please outline key IT responsibilities, software requirements, systems to maintain, or goals for this role...',
                'rows': 5,
                'required': True
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('website_url'):
            raise forms.ValidationError("Spam detected.")
        return cleaned_data
