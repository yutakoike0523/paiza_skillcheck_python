s= list(map(int,input().split()))
N,M,K=s[0],s[1],s[2]
cards = list(range(1, N + 1))
def shuffle_cards(N, M):

    sets = [cards[i:i+M] for i in range(0, N, M)]
    sets.reverse()
    shuffled_cards = [card for set in sets for card in set]

    return shuffled_cards

for i in range(0,K):
    cards=shuffle_cards(N,M)
for x in cards:
    print(x)