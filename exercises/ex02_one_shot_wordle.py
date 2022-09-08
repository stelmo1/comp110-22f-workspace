"""Making a one shot wordle."""

__author__: str = "730573475"

#getting the main variables set up
secret: str = "python"
guess: str = str(input(f"What is your {len(secret)}-letter guess? "))

#getting the emojis set up here, so they're easier to call
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

#making sure that the user is inputting the right length
while len(guess) != len(secret):
            guess = str(input(f"That was not {len(secret)} letters! Try again: "))

#setting up tracking variables for the various loops
i: int = 0
track: int = 0 
result: str = ""
somewhere: bool = False

#the main loop! to check each letter and give it a corresponding emoji
while i < len(secret):
    if guess[i] == secret[i]:
        #this one has to go first because otherwise it gets messy
        result += GREEN_BOX
    else:
        while track < len(secret) and somewhere == False:
            #this loop is to see if the letter is anywhere, its gotta go before the white box one or else it gets messy
            if guess[i] == secret[track]:
                somewhere = True
            else:
                track += 1
        if somewhere == True:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
    #gotta add and reset some stuff so the loop will end/work properly
    i += 1
    track = 0 
    somewhere = False
print(result)

if guess == secret:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")        