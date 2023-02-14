#!/bin/python3

from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny',
    'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty',
    'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    dictionary_file = open(dictionary_file)
    text = dictionary_file.read().split('\n')
    stack = []
    q = deque()
    stack.append(start_word)
    q.append(stack)

    if start_word == end_word:
        return stack
    while len(q) != 0:
        stack = q.popleft()
        for w in list(text):
            if _adjacent(w, stack[-1]):
                if w == end_word:
                    stack.append(w)
                    return stack
                stack2 = copy.copy(stack)
                stack2.append(w)
                q.append(stack2)
                text.remove(w)
    return None


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    if len(word1) == len(word2):
        difference = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                difference += 1
        if difference <= 1:
            return True
        else:
            return False


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''

    verify = 0
    if not ladder:
        verify = False
    if len(ladder) == 1:
        verify = True
    for i in range(len(ladder) - 1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
        else:
            verify = True
    return verify
