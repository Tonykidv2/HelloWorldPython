# temperatur = -29

# if temperatur > 30:
#     print("It's a hot day")
#     print("Drink water")
#     print("Its a nice day")
# else :
#     print("It's chilly chilly")

# print("done")

weight = input("Weight: ")
weight_type = input("(K)g or (L)bs: ")

# simple validation
while(weight_type.upper() != "L" and weight_type.upper() != "K"):
    weight_type = input("Please enter K or L: ")

if(weight_type.upper() == "L"):
    print("Weight in Kgs: " + str(int(weight) / 2.205))
else:
    print("Weight in Lbs: " + str(int(weight) * 2.205))

print("done")
