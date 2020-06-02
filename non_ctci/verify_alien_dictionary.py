#a problem from leetcode that I saw

def verify_alien_dictionary(self, words: [str], order: str) -> bool:
    alien_order = dict()
    for i, letters in enumerate(order):
        alien_order[letters] = i
        
    def in_order(word_1, word_2):
        for place in range(min(len(word_1), len(word_2))):
            if alien_order[word_1[place]] < alien_order[word_2[place]]:
                return True
            elif alien_order[word_1[place]] > alien_order[word_2[place]]:
                return False
        if len(word_1) > len(word_2):
            return False
        else:
            return True
    for place in range(len(words) - 1):
        if not in_order(words[place], words[place + 1]):
            return False
    return True
    

