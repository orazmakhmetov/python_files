user_input = input("Enter a Phrase: ")
phrase = (user_input.replace('of', '')).split()
acronym = " "
for word in phrase:
    acronym = acronym + word[0].upper()
    print(f'Acronym of {user_input} is {acronym}')
    
    
