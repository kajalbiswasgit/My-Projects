# Q1. Create a dictionary of your profile (name, age, city)
# Q2. Print only the city from your dictionary
# Q3. Update the age to a new value
# Q4. Add a new key-value: "profession": "Tester"
# Q5. Delete the city key from dictionary
# Q6. Check if "name" key exists in your dictionary
# Q7. Print all keys
# Q8. Print all values
# Q9. Use items() to print all key-value pairs
# Q10. Add another person’s data using update()

profile = {"Name:": "Kajal", "age:": 29, "city:": "Purulia"}
print ("City:",profile["city:"])
profile ["age:"]= 28
profile ["profession:"]= "Testter"
del profile ["age:"]
if "Name:" in profile:
    print ("yes its exist")
else:
    print ("name: not exist")
print ("All keys:",profile.keys())
print ("All values:",profile.values())
print ("All keys and values:",profile.items())
profile.update ({"Name:": "Shreya", "Designation:":"Staff nurse"})
print ("All keys and values:",profile.items())
