import json
test = { }
score = 0
number = 1
f = open("test.txt",'r')
test = json.load(f)
f.close()

print("python quiz program")
print(" enter t for True or f for False")
name = input("Enter your full name :")
for tes in test.keys():
    print("test",number," : ",tes)
    result = input("The result is ")
    if result.upper() == test[tes].upper():
        score = score + 1
        print("correct")
    else:
        print("wrong")
    number = number + 1
goal={name:score}
m=open("scores.txt",'w')
goal=json.dump(goal,m)
m.close()
      
