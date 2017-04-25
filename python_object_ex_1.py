# Write code to:
# 1 Instantiate an instance object of Person with name of 'Sonny', email of
# 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.

# 2 Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com',
# and phone of '495-586-3456', store it in the variable 'jordan'.

# 3 Have sonny greet jordan using the greet method.
# 4 Have jordan greet sonny using the greet method.
# 5 Write a print statement to print the contact info (email and phone) of Sonny.
# 6 Write another print statement to print the contact info of Jordan.

class Person():

    greeting_count = 0
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.num_unique_people_greeted = 0
        self.uniquecounter = []


    def greet(self, other_person):
        print ('Hello {}, I am {}!'.format(other_person, self.name))
        self.greeting_count += 1


#        for other_person in list1:
        if other_person not in self.uniquecounter:
            self.uniquecounter.append(other_person)
            self.num_unique_people_greeted += 1


    def print_contact_info(self):
        print("{}'s email: {} , {}'s phone number: {}".format(self.name, self.email, self.name, self.phone))

    def add_friend(self, other):
        self.friends.append(other)

    def __str__(self):
        return"Contact info for {} : email - {} | phone - {}".format(self.name, self.email, self.phone)
#        print('Person: {} {} {}'.format(self.name, self.email, self.phone))

#    def greeting_count(self, greeting_count):
#        newcount = []
#        if self.name.greet() == True:
#            newcount = count + 1
#            print(newcount)

#    def num_unique_people_greeted():
#        if self


sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

print(jordan.greeting_count)
print(sonny.greeting_count)

sonny.greet('Jordan')
sonny.greet('Jordan')
#jordan.greet('Sonny')

#sonny.print_contact_info()
#jordan.print_contact_info()
#print(sonny.email, sonny.phone)
#print(jordan.email, jordan.phone)

#jordan.friends.append(sonny)
#sonny.friends.append(jordan)
#print(len(jordan.friends))
#print(len(sonny.friends))
#print(sonny.friends)
#print(jordan.friends)
#jordan.add_friend(sonny)
#print(len(jordan.friends))
#print(len(sonny.friends))
#print(jordan.greeting_count)
#print(sonny.greeting_count)
#print(jordan)
print(sonny.num_unique_people_greeted)
#jordan.__str__()
