import factory
from .models import People


class MyModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = People

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    age = factory.Faker("random_int", min=0, max=100)
