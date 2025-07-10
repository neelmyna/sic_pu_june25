from flask import Flask, jsonify, request
from person_dao import Person, Db_operations

people = Db_operations()
people.create_db()
people.create_table()

app = Flask(__name__)

@app.route('/people',methods=['POST'])
def people_create():
    body = request.get_json()
    new_person = Person(body['name'], body['gender'], body['dob'], body['location'])
    # print(type(new_person))
    id = people.insert_row(new_person)
    person = people.search_row(id)
    person_dict = {'id':person[0], 'name':person[1], 'gender':person[2], 'dob':person[3], 'location': person[4]}
    return jsonify(person_dict)

@app.route('/people/<id>',methods=['GET'])
def people_read_by_id(id):
    person = people.search_row(id)
    if person == None:
        return jsonify("Person not found")
    person_dict = {'id':person[0], 'name':person[1], 'gender':person[2], 'dob':person[3], 'location': person[4]}
    return jsonify(person_dict)

@app.route('/people',methods=['GET'])
def people_read_all():
    people_list = people.list_all_rows()
    people_dict = []
    for person in people_list:
        people_dict.append({'id':person[0], 'name':person[1], 'gender':person[2], 'dob':person[3], 'location': person[4]})
    return jsonify(people_dict)

@app.route('/people/<id>',methods=['PUT'])
def people_update(id):
    body = request.get_json()
    old_peron_obj = people.search_row(id)
    if not old_peron_obj:
        return jsonify({'message': 'Person not found'})
    new_person_obj = []
    new_person_obj.append(body['name'])
    new_person_obj.append(body['gender'])
    new_person_obj.append(body['location'])
    new_person_obj.append(body['dob'])
    new_person_obj.append(id)
    new_person_obj = tuple(new_person_obj)
    people.update_row(new_person_obj)

    person = people.search_row(id)
    person_dict = {'id':person[0], 'name':person[1], 'gender':person[2], 'dob':person[3], 'location': person[4]}
    return jsonify(person_dict)

@app.route('/people/<id>',methods=['DELETE'])
def people_delete(id):
    old_person_obj = people.search_row(id)
    if not old_person_obj:
        return jsonify({'message': 'Person not found', 'is_error': 1})
    people.delete_row(id)
    return jsonify({'message': 'Person is deleted', 'is_error': 0})

app.run(debug=True)
