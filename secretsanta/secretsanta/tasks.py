from random import randint

from .models import Person, SantaRelation


def create_santa_relationships():
    people = list(Person.objects.values_list('id', flat=True))
    for person in Person.objects.all():
        not_matched = True
        while not_matched:
            rand_person = randint(0, len(people) - 1)
            if people[rand_person] == person.id:
                continue
            elif person.excluded.exists():
                if person.excluded.filter(excluded_id=people[rand_person]):
                    continue
            SantaRelation.objects.create(giver=person, recipient_id=people[rand_person])
            not_matched = False
            people.pop(rand_person)
