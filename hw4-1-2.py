# Kyle Bautista (AMDG) 10/12/20

card1 = int(input("What is the number of your first card? "))
card2 = int(input("What is the number of your second card? "))

if (card1 + card2) == 21:
    print("Safe!")
else:
    print("Bust!")
