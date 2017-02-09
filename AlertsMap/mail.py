from django.core.mail import send_mail
from django.conf import settings

send_mail(


    subject = 'New alert entry needs to be moderated',
    message = 'New alert entry needs to be moderated',
    from_email ='denys.boiko@reach-initiative.org',
    recipient_list = ['denys.boiko@reach-initiative.org'],
    # , 'jeremy.wetterwald@reach-initiative.org'
    fail_silently=False
)

send_mail