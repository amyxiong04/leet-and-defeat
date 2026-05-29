class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = {}

        for card in hand:
            if card not in freq:
                freq[card] = 0
            freq[card] += 1

        for card in sorted(freq.keys()):
            if freq[card] > 0:
                need = freq[card]  # however many copies of card remain, we need to start that many groups from card

                for x in range(card, card + groupSize): # loop through the cards needed for the straight
                    if x not in freq or freq[x] < need:
                        return False
                    freq[x] -= need

        return True