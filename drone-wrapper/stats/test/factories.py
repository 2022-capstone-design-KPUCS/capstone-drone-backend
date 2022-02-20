import factory


class AdminFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'stats.Administrator'
        
        django_get_or_create = ('username',)

    id = factory.Faker('uuid4')
    username = factory.Sequence(lambda n: f'testuser{n}')
    password = factory.Faker('password', length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True


class FlightFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'stats.Flight'

    id = factory.Faker('uuid4')
    flight_record_url = factory.Faker('url')
    flight_start_time = factory.Faker('date_time_between', start_date='-30d', end_date='now')
    flight_end_time = factory.Faker('date_time_between', start_date='-30d', end_date='now')
    flight_path = factory.Faker('pydecimal', left_digits=10, right_digits=10, positive=True)
    flight_status = factory.Faker('boolean')


class DeckFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'stats.Deck'

    id = factory.Faker('uuid4')
    deck_name = factory.Faker('word')
    deck_status = factory.Faker('boolean')


class DroneFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'stats.Drone'

    id = factory.Faker('uuid4')
    admin_id = factory.SubFactory(AdminFactory.id)
    surveilance_area = factory.Faker('address')
    flight = factory.SubFactory(FlightFactory)
    deck = factory.SubFactory(DeckFactory)
