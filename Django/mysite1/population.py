import os

from django.core.exceptions import FieldError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite1.settings')

import django
django.setup()

#Fake population script
import random
from App1.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','News','Marketplace','Game']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def population(N = 5):

    # try:

    for entry in range(N):

        #Get the topic of entry
        top = add_topic()

        #Create the fake data of entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

        #Create the fake access record of webpage
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, data = fake_date)[0]
    # except ValueError:
    #     print(" Invalid input ")
    # except FieldError:
    #     print(" Invalid input ")

if __name__ == "__main__":
    print(" Population script! ")
    population(50)
    print(" Population complete! ")
