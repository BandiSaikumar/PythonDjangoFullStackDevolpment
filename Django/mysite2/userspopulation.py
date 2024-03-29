import os

from django.core.exceptions import FieldError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite2.settings')


import django
django.setup()

from App2.models import user
from faker import Faker

fakegen = Faker()

def population(N = 5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fakegen.name()
        fake_last_name = fakegen.name()
        fake_email = fakegen.email()

        users = user.objects.get_or_create(first_name = fake_first_name,last_name = fake_last_name,email = fake_email)[0]
if __name__ == "__main__":
    print(" Population Databases! ")
    population(100)
    print(" Completed! ")

