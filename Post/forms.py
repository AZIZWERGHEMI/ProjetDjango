from django import forms
from .models import EvenClub, EvenSocial, Stage, Logement, Transport

class EvenClubForm(forms.ModelForm):
    
    class Meta:
        model = EvenClub
        fields = ['image', 'legende',  'date_evenement', 'prixC', 'nom', 'domaine','post_type']

class EvenSocialForm(forms.ModelForm):
    
    class Meta:
        model = EvenSocial
        fields = ['image', 'legende', 'date_evenement', 'prixS', 'nom', 'theme','post_type']

class StageForm(forms.ModelForm):
   
    class Meta:
        model = Stage
        fields = ['image', 'legende', 'localisation', 'societe', 'duree', 'sujet', 'specialite','post_type']

class LogementForm(forms.ModelForm):
   
    class Meta:
        model = Logement
        fields = ['image', 'legende',  'localisation', 'prix', 'contact_info','post_type']

class TransportForm(forms.ModelForm):
    
    class Meta:
        model = Transport
        fields = ['image', 'legende',  'destination', 'type_transport', 'contact_info','post_type']
