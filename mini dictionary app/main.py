user_dictionary = {}
while True:
    print("mini dictionary app")
    print("1. add or update word")
    print('2. retrieve a word')
    print("3. delete a word")
    print("4. view al words")
    print("5. exit")

    list_number = int(input("please select one of the following numbers: "))

    if list_number == 1:
    
        word_add =  input("enter you're word? ")
        definition = input("enter the definition of the word? ")
        user_dictionary[word_add] = definition
        print(f"youre word {word_add} has been added to the dictionary")

    elif list_number == 2:
        retrief = input("enter the word to retrieve")
        if retrief in user_dictionary:
            print(f"{word_add} = {definition}")
        else:
            print(f"this word {retrief} is not in the dictionary")

    elif list_number == 3:
    
        delete = input("which word would you like to delete? ")
        if delete in user_dictionary:
            del user_dictionary[delete]
        else:
            print(f"the word {delete} is not in the dictionary")
    elif list_number == 4:
        print("the word in the dictionary is:")
        for item in user_dictionary:
            print(f"{item},{user_dictionary[item]}" )
    elif list_number == 5:
        print("exiting the dictionary goodbye")
        break
    else:
        print("invalid choice")

