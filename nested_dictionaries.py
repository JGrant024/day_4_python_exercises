# Given the following dictionary:

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

# Write a python expression that gets the email address of Ramit.
# Write a python expression that gets the first of Ramit's interests.
# Write a python expression that gets the email address of Jasmine.
# Write a python expression that gets the second of Jan's two interests.
# NOTE: "Python expression" just means something like print(dictionary[key]). Although, in two of the above, using a for loop will be helpfu!


ramit_email = ramit['email']
print(ramit_email)

ramits_interests = ramit['interests'][0]
print(ramits_interests)


#This gets the email of Jasmine. Creating a variable with the value of dictionary getting the index of friends getting the first(0 index) of friends name jasmine, then the email. Then print the results 
jasmine_email = ramit['friends'][0]['email']
print(jasmine_email)

# This get the second interest of Jan, creating a variable with the value of ramit getting the index of friends 1 and interest 1 which will print the second interest of Jan. 
jans_interest = ramit['friends'][1]['interests'][1] 
print(jans_interest)
    
