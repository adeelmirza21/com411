genre=str(input("what type of genre do you like to read"))

if genre == "thriller":
    print("You like thriller books")
    print("finished reading book!")

elif genre == "comedy":
    print("you like comedy books")
    print("finished reading book")

elif genre == "horror":
    print("you like horror books")
    print("finished reading book")

else:
    print("you like", genre, "books")
    print("finished reading book")
