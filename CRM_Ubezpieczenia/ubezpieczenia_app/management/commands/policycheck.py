from django.core.management.base import BaseCommand
from ubezpieczenia_app.models import Policy
from datetime import datetime
from sms import send_sms


class Command(BaseCommand):
    help = "Sprawdzanie terminu ważności polisy"

    def handle(self, *args, **options):
        policies = Policy.objects.all()
        date_format = "%Y-%m-%d"

        for policy in policies:

            time = policy.date_end.strftime("%Y-%m-%d")
            now = datetime.now().strftime("%Y-%m-%d")
            date_end = datetime.strptime(time, date_format).date()
            date_now = datetime.strptime(now, date_format).date()

            diff = date_end - date_now
            if (diff.days < 30):

                print("Do końca polisy o nr. {} zostalo {} dni".format(policy.number, diff.days))
                send_sms(
                    'Skontaktuje się w sprawie nowej oferty, pozdrawiam',
                    '+48508920732',
                    [policy.client.phone],
                    fail_silently=False
                )
