N,M = map(int,input().split())
card_list= list(map(int, input().split()))

for card1 in card_list[:]:
        print(card1)
        for card2 in card_list[:-1]