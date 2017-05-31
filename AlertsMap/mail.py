from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage

def notify_mail(to_list, cc_list, instance, clusters, needs, url):
    # ,

    subject = 'Ukraine Alert Map: New alert in ' + instance.settlement.settlement_name

    from_email = 'ocha.im.ukr.aws@gmail.com'
    # ocha.im.ukraine @ gmail.com
    ctx = {
        'location': instance.location(),
        'clusters': ', '.join(clusters),
        'no_affected': instance.no_affected,
        'alert_type': instance.alert_type,
        'needs': ', '.join(needs),
        'context': instance.context,
        'description': instance.description,
        'conflict_related': instance.related_to_conflict(),
        'date_referal': instance.date_referal,
        'url': url
    }

    message = get_template('email/email.html').render(ctx)

    email = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
    email.content_subtype = 'html'
    email.send(fail_silently=False)