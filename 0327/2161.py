from collections import deque

N= int(input())
cards = deque(range(1,N+1))
discarded=[]

while len(cards)>1:
    discarded.append(cards.popleft())
    cards.append(cards.popleft())

print(*discarded, cards[0])