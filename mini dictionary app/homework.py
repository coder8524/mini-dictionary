word = input("enter a word of you're choice: ")
dictionary1 = {}
for item in word:
    if item.isalpha():

        item = item.lower()
        if item in dictionary1:
            dictionary1[item] += 1
        else:
            dictionary1[item] = 1
for i,j in dictionary1.items():
    print(i,":",j)

    