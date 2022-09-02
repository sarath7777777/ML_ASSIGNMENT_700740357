#Creating an empty dictionary called dog
Dog = {}
print(Dog)
Dog = {"name" : "doggie", "color" : "brown", "breed" : "labroder", "legs" : "4", "age" : "7"}
print(Dog)
#creating student dictionary
Student = {"first_name" : "SARATH" , "last_name" : "NEKKALAPU", "gender" : "MALE", "age" : "22", "marital status" :"SINGLE",
"skills" : "C,CPP,JAVA", "country" : "INDIA", "city" : "VIJAYAWADA", "address" : "KAMMATURU"}
print(Student)
#printing length
print(len(Student))
#getting skills
print(Student.get("skills"))
print(type(Student["skills"]))