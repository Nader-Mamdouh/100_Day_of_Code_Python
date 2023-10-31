PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as data:
   names = data.readlines()
   #print(names)
with open("./Input/Letters/starting_letter.txt") as letter:
   letter_content = letter.read()
   for name in names:
       striped_name = name.strip()
       new_letter = letter_content.replace(PLACEHOLDER, striped_name)
       #print(new_letter)
       with open(f"./Output/ReadyToSend/letter_for_{striped_name}.txt" , mode="w") as email:
           email.write(new_letter)
