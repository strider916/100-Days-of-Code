PLACEHOLDER = "[name]"

# Open file with all the names
with open("names.txt", mode="r") as names_file:
    # for every name in the name file (each on their own line)
    for name in names_file.read().splitlines():
        # Open the template letter
        with open("starting_letter.txt", mode="r") as starting_letter:
            # create a new file while replacing the placeholder text with the name
            with open(f"./ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter:
                new_letter.write(starting_letter.read().replace(PLACEHOLDER, name))
