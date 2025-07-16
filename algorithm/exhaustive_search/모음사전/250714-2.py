"""
다른 사람이 푼 풀이
"""

dictionary = []
def make_dictionary(word:str)->None:
    global dictionary

    if len(word) == 6:
        return

    dictionary.append(word)

    for alphabet in ['A', 'E', 'I', 'O', 'U']:
        make_dictionary(word + alphabet)

def solution(word:str)->int:
    global dictionary

    make_dictionary("")
    dictionary.sort()
    return dictionary.index(word)
