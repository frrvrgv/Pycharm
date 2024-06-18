import json

person_dict = {'name': 'bob',
               'language': ["English","French"],
               'married': True,
               'age': 67,
                'id': 7654
}
with open('person.txt', 'w') as json_file:
    json.dump(person_dict, json_file, indent = 4, sort_keys=True)