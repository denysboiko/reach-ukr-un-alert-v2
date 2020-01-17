from django.template import Template, Context
from django.core.mail import EmailMessage
from .models import MailConfig


def notify_mail(to_list, cc_list, instance, clusters, needs, url):

    config = MailConfig.objects.filter(pk=1).first()

    subject = config.subject + instance.settlement.settlement_name
    from_email = config.from_email

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

    template = Template(config.body)
    message = template.render(Context(ctx))

    email = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
    email.content_subtype = 'html'
    email.send(fail_silently=False)