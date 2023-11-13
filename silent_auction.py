from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

bids = []

def submit_bid():
  bid = {} 
  bidder_name = input("What is your name?: ")
  bidder_amount = int(input("what's your bid?: $"))
  bid[bidder_name] = bidder_amount
  bids.append(bid)


def bid_results():
  #who won
  curr_high_bid_amount = 0  # initialize bid
  curr_high_bid_name = ""
  
  for bid_dict in bids:
        for bidder_name, bidder_amount in bid_dict.items():
          if bidder_amount > curr_high_bid_amount:
            curr_high_bid_amount = bidder_amount
            curr_high_bid_name = bidder_name
  print(curr_high_bid_name, curr_high_bid_amount)


print(logo)
submit_bid()

more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")

while more_bidders == "yes":
  clear()
  submit_bid()
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
  
bid_results()
  
