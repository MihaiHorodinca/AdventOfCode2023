from enum import IntEnum

fileName = "day7input.txt"
myFile = open(fileName, "r")


class CardRank(IntEnum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


cardValues = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14
}


def get_rank(hand: str):
    frequency = [0] * 15

    for card in hand:
        frequency[cardValues.get(card)] += 1

    if max(frequency) == 5:
        return CardRank.FIVE_OF_A_KIND

    if max(frequency) == 4:
        return CardRank.FOUR_OF_A_KIND

    if 3 in frequency and 2 in frequency:
        return CardRank.FULL_HOUSE

    if 3 in frequency:
        return CardRank.THREE_OF_A_KIND

    noPairs = frequency.count(2)
    if noPairs == 2:
        return CardRank.TWO_PAIR

    if noPairs == 1:
        return CardRank.ONE_PAIR

    return CardRank.HIGH_CARD


def get_rank_with_jokers(hand: str):
    frequency = [0] * 15

    for card in hand:
        frequency[cardValues.get(card)] += 1

    noJokers = frequency[cardValues.get("J")]
    frequency[cardValues.get("J")] = 0

    maxIndex, maxValue = max(enumerate(frequency), key=lambda pair: pair[1])

    if maxValue == 0:
        # all cards are Jokers
        return CardRank.FIVE_OF_A_KIND

    frequency[maxIndex] += noJokers

    if max(frequency) == 5:
        return CardRank.FIVE_OF_A_KIND

    if max(frequency) == 4:
        return CardRank.FOUR_OF_A_KIND

    if 3 in frequency and 2 in frequency:
        return CardRank.FULL_HOUSE

    if 3 in frequency:
        return CardRank.THREE_OF_A_KIND

    noPairs = frequency.count(2)
    if noPairs == 2:
        return CardRank.TWO_PAIR

    if noPairs == 1:
        return CardRank.ONE_PAIR

    return CardRank.HIGH_CARD


class CamelCardHand:
    def __init__(self, hand: str, bid: int):
        self.hand = hand
        self.bid = bid
        self.rank = get_rank_with_jokers(hand)

    def __str__(self):
        return f'Hand {self.hand} of rank {self.rank} with bid {self.bid}'


def sort_hands(hand: CamelCardHand):
    numberedCards = [cardValues.get(card) for card in hand.hand]
    return hand.rank, numberedCards


def solve_a():
    textHands = myFile.readlines()
    hands = []

    for line in textHands:
        hand, bid = line.split()
        hands.append(CamelCardHand(hand, int(bid)))

    print("\n".join([str(hand) for hand in hands]))
    print()

    hands.sort(key=sort_hands)
    print("\n".join([str(hand) for hand in hands]))

    total = 0
    payout = 1
    for hand in hands:
        total += hand.bid * payout
        payout += 1

    print(total)


solve_a()
