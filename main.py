#import logo of gamr from art.py
from art import logo

#Function to find the winner
def bid_winner():
    winner = ""
    highest_bid = 0
    #Loop through each item of dictionary and find which one have highest bid
    for bidder in dict_of_bidders:
        if highest_bid < dict_of_bidders[bidder]:
            highest_bid = dict_of_bidders[bidder]
            winner = bidder
    #Print the result
    print(f"The winner is {winner} with a bid of ${highest_bid}")

#print logo
print(logo)
print("Welcome to the secret auction program.")
#Create the dictionar of bidders
dict_of_bidders = {}

#Continue the game until user want
should_continue = True
while should_continue:
    #Take name and bid from the user
    name = input("What is your name?: ")
    bid = int( input("What's your bid?: "))

    #Add the name and bid in to the dictionary
    dict_of_bidders[name] = bid

    #Ask the user, are there any other bidders or not.
    any_other_bidder = input("Are there any other bidders? Type 'yse' or 'no'.\n")

    #If there is no other bidders then end the game with the results.
    if any_other_bidder == 'no':
        should_continue = False
        #Call the bid_winner function to announce the result.
        bid_winner()
        print("Goodbye")