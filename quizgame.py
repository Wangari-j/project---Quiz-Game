geographyquiz = input("Which is the highest mountain in Africa? ")
print(geographyquiz)
score = 0


if geographyquiz == "Mt. Kilimanjaro":
    print("Correct!")
    score += 1 #is equal to score + 1
else:
    print("Incorrect!")
   

geographyquiz2 = input("Which is the longest river? ")

if geographyquiz2 == "Nile":
    print("Correct!") 
    score += 1

else:
    print("Incorrect!")
   

geoquiz = input("Which country has the highest population in Africa? ")

if geoquiz == "Nigeria":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
   

geoquiz2 = input("Which country has the biggest land mass in Africa? ")

if geoquiz2 == "Algeria":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    

geoquiz1 = input("How many countries are in Africa? ")
if geoquiz1 == "54":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    

print("You got " + str(score) + " Correct!")
print("You got " + str((score / 5) *100) +  "%.")
