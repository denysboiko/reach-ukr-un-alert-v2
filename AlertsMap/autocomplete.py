from agnocomplete.register import register
from agnocomplete.core import AgnocompleteChoices, AgnocompleteModel
from AlertsMap.models import *


class AutocompleteColor(AgnocompleteChoices):
    choices = (
        ('green', 'Green'),
        ('gray', 'Gray'),
        ('blue', 'Blue'),
        ('grey', 'Grey'),
    )


class AutocompletePerson(AgnocompleteModel):
    model = Organization
    fields = ['organization_name',]

# Registration
register(AutocompleteColor)
register(AutocompletePerson)