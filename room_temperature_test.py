room_temp=input("Enter current room temperature: ")
room_temp = int(room_temp)
print("\n")
print("+++++++++++")
if room_temp > 32:
    print("its sooo hot out there!")
elif room_temp<=32 and room_temp>=10:
    print("What a pleasant weather today!")
else:
    print("Ooo..so chilly!")
