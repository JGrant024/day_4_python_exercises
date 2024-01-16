# Using the dictionary from the Nested dictionaries exercise above, 
# write a function countFriends() that accepts a dictionary as an argument 
# and returns a new dictionary that includes a new key friends_count:



# Nested dictionary from previous example: 
ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
        'name': 'Jasmine',
        'email': 'jasmine@yahoo.com',
        'interests': ['photography', 'tennis']
        },
        {
        'name': 'Jan',
        'email': 'jan@hotmail.com',
        'interests': ['movies', 'tv']
        }
    ]
}

# End of nested dictionary from previous example 


def countFriends(person):
    friends_count = len(person.get('friends', []))
    return {'friends_count': friends_count}

result = countFriends(ramit)
print(result)
