print("When entering the options, please enter them exactly as presented.")
print("The world is ending")
print("The year is 69420, and Artificial Intelligence has taken control of the world. It is your job to find survivors and supplies. Be careful, most automated or electronic devices may be controlled by the enemies.")
print("You were across the country from your family studying mechanical engineering in college. When the first attack occured, you were flying back home.")
print("Unfortunately, your plane got controlled by AI and crash-landed into a lake. It is your job to find supplies and reach your family.")
print("You wake up in the plane and take off your seatbelt, seeing the destruction around you. You have 5 minutes before the plane sinks beneath the lake.")
q = int(input("Enter '1' if you want to help other passengers or enter '2' if you want to ignore the cries to gather supplies and escape the plane instead. "))
if q == 1:
    print ("You barely mananaged to escape with 3 other people. One is a doctor, the second is another student, and the third is a profesional athlete.")
    print("You see an abandoned warehouse.")
    s = int(input("Enter '1' to enter the warehouse or enter '2' to stay."))
    if s == 1:   
        print("As you enter the warehouse, you cut yourself on a rusty pipe. Luckily, the doctor has medical equipment that healed you. As you explore the warehouse, you find food and weapons.")
    elif s == 2: 
        print("Eventually, you go delirious due to a lack of water and kill the doctor. Later, you get cut on a twig and die without proper medical attention.")
elif q == 2:
    print ("You managed to gather supplies and escape the plane. However, the supplies were not good.")
    print("You see an abandoned warehouse")
    r = int(input("Enter '1' if you decide to go inside or enter '2' if you decide to stay with the supplies you have."))
    if r == 1:
        print("As you enter the warehouse, you get cut on a rusty pipe you tried pulling out. Without proper care, you die of an infected arm.")
    if r == 2:
        print("Your supplies are useless and you die of starvation.")
s = input("With your newly found supplies you are able to make it to a new town. As you search through the town, y

 
