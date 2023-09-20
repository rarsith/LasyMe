def access_and_update(doc, path, value_to_add):
    # Split the path into individual keys
    keys = path.split('.')

    # Traverse the document using the keys
    nested_doc = doc
    for key in keys:
        nested_doc = nested_doc.get(key, {})
        print(nested_doc)

    # Check if the attribute is a list and add the value
    if isinstance(nested_doc, list):
        nested_doc.append(value_to_add)

    print(nested_doc)

# Example document
document = {
    'id': '9387435943tytre',
    'name': 'John',
    'features': {
        'eyes': 'blue',
        'skills': ['jumping', 'walking', 'screaming'],
        'hand': {
            'index_finger': ['red', 'transparent', 'crispy']
        }
    }
}

# Access and update the "features.hand.index_finger" attribute
path_to_attribute = "features.skills"
value_to_add = "redME"

access_and_update(document, path_to_attribute, value_to_add)

# Print the updated document
print(document)


#__________________________________________________________________REMOVE_VALUE____________________
def access_and_update(doc, path, value_to_remove):
    # Split the path into individual keys
    keys = path.split('.')

    # Traverse the document using the keys
    nested_doc = doc
    for key in keys:
        nested_doc = nested_doc.get(key, {})
        print(nested_doc)

    # Check if the attribute is a list and remove
    if isinstance(nested_doc, list):
        if value_to_remove is not None and value_to_remove in nested_doc:
            nested_doc.remove(value_to_remove)

    print(nested_doc)

# Example document
document = {
    'id': '9387435943tytre',
    'name': 'John',
    'features': {
        'eyes': 'blue',
        'skills': ['jumping', 'walking', 'screaming'],
        'hand': {
            'index_finger': ['red', 'transparent', 'crispy']
        }
    }
}

# Access and update the "features.hand.index_finger" attribute
path_to_attribute = "features.skills"
value_to_add = "jumping"

access_and_update(document, path_to_attribute, value_to_add)

# Print the updated document
print(document)



root_schema = {
    '1': {
        'parent': None,
        'task_title': '',
        'user': 'arsithra',
        'asigned_to': 'arsithra',
        'start_date': '1-1-2000',
        'end_date': '1-3-2000',
        'hours_duration': 3,
        'due_in': '3',
        'prio': 'high',
        'status': 'high',
        'active': True,
        'task_details': ''
    }
}