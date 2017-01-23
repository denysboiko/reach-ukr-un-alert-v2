from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message sent directly from Python code.',
    'denys.boiko@reach-initiative.org',
    ['denys.boiko@reach-initiative.org'],
    # , 'jeremy.wetterwald@reach-initiative.org'
    fail_silently=False
)