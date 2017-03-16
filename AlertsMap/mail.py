from django.core.mail import send_mail
from django.core.mail import EmailMessage

def notify_mail(to_list, cc_list, location):

    email = EmailMessage(
        subject='New alert',
        body='New alert has been created in ' + location,
        from_email='denys.boiko@reach-initiative.org',
        to=to_list,
        # ['denys.boiko@reach-initiative.org'],
        cc=cc_list
        # ['d.zhivchik.b@gmail.com']
    )

    email.send(fail_silently=False)

    print('Message sent!')