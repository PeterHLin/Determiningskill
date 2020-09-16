import valorant

print("Welcome to :", valorant.name + "!")
print("ranks you can select: ", valorant.ranks)
print("tiers you can select: ", valorant.tier)
player_name = input("To determine how good you are, please enter your game name: ")
player_rank = input("please put in your rank! (it is case sensitive so please type in the given available ranks in the given fomat: ")
player_tier = input("please put in your tier in number: ")

if int(player_tier) == 3:
    print("Dear " + player_name + ", you are ranked " + player_rank
    + " and our bot says that " + valorant.ratings[1] + " in your elo!")
if int(player_tier) == 2:
    print("Dear" + player_name + ", you are ranked " + player_rank
    + " and our bot says that " + valorant.ratings[2] + " in your elo!")
if int(player_tier) == 1:
    print("Dear " + player_name + ", you are ranked " + player_rank
    + " and our bot says that " + valorant.ratings[0] + " in your elo!")

