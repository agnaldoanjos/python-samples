from app.models import Person
from app import db

def get_all_people():
    people = Person.query.all()
    return [
        {"id": p.id, "name": p.name, "born_date": p.born_date, "document": p.document}
        for p in people
    ]

def create_person(data):
    new_person = Person(
        name=data['name'],
        born_date=data['born_date'],
        document=data['document']
    )
    db.session.add(new_person)
    db.session.commit()
    return {
        "id": new_person.id,
        "name": new_person.name,
        "born_date": new_person.born_date,
        "document": new_person.document
    }

def get_person(person_id):
    person = Person.query.get(person_id)
    if not person:
        return {"error": "Person not found"}, 404
    return {
        "id": person.id,
        "name": person.name,
        "born_date": person.born_date,
        "document": person.document
    }

def update_person(person_id, data):
    person = Person.query.get(person_id)
    if not person:
        return {"error": "Person not found"}, 404
    person.name = data.get('name', person.name)
    person.born_date = data.get('born_date', person.born_date)
    person.document = data.get('document', person.document)
    db.session.commit()
    return {"message": "Person updated successfully"}

def delete_person(person_id):
    person = Person.query.get(person_id)
    if not person:
        return {"error": "Person not found"}, 404
    db.session.delete(person)
    db.session.commit()
    return {"message": "Person deleted successfully"}
