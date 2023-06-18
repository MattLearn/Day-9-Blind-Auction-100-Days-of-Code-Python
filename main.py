from replit import clear
#HINT: You can call clear() to clear the output in the console.
bids = {}
print("welcome to auction")
betting = True
largest_bidder = ''

while(betting == True):
  name = input("Enter your name: ")
  bid = int(input("how much are you willing to bid on the item: $"))
  bids[name] = bid
  largest_bidder = name
  if input("is there anyone else who wants to bid (Y or N): ").lower() == 'n':
    betting = False
  clear()

if len(bids) > 1:
  for bidders in bids:
    if bids[bidders] > bids[largest_bidder]:
      largest_bidder = ''+(bidders)
print(f"The winner is {largest_bidder} with a bid of ${bids[largest_bidder]}.")