import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids = {}
bidding_finished = False

def find_hightest_bidder(bidding_record):

    highest= 0 
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest}")



    


while not bidding_finished:
    name = input("What is your name\n")
    price = int(input("What is your bid?\n$"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type'yes' or 'no'.").lower()
    if should_continue == "no":
        bidding_finished = True
        find_hightest_bidder(bids)
    elif should_continue == "yes":
        os.system("cls")
