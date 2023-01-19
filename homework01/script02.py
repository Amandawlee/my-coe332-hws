import names

counter = 0
while (counter != 5):
    fullname = names.get_full_name()
    if (len(fullname) == 9):
        counter = counter + 1
        print(fullname)
