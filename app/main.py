class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_ls = []

    for person in people:
        Person(person["name"], person["age"])
        person_ls.append(Person.people[person["name"]])

    for person in people:

        person_instance = Person.people[person["name"]]

        if person.get("wife"):
            person_instance.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            person_instance.husband = Person.people[person["husband"]]

    return person_ls
