"""Typing test implementation"""

from msilib import type_binary
from utils import count, lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k): #paragraphs is a list
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    if len(paragraphs)<k + 1:
        return ''
    if k == 0:
        n=0
        for s in paragraphs:
            if select(s):
                return str(s)
                n =1
        return ''
    else:
        if select(paragraphs[0]):
            return choose(paragraphs[1:],select, k-1)
        else:
            return choose(paragraphs[1:],select , k)
    # END PROBLEM 1


def about(topic):#topic is a list
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select(paragraph): #paragragh is an element
        fixed_para= split(lower(remove_punctuation(paragraph) ))
        for s in topic:
            if s in fixed_para:
                return True
        return False
    return select
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    count, i =0,0
    if len(typed_words) == 0:
        return 0.0
    else:
        while i <min(len(typed_words),len(reference_words)):
            if typed_words[i] == reference_words[i]:
                count +=1
            i +=1
        return count / len(typed_words) *100
        
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed)/elapsed * 12
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    else:
        i, best_valid = 1, valid_words[0]
        diff =diff_function(user_word, valid_words[0],limit)
        while i< len(valid_words):
            if diff_function(user_word,valid_words[i],limit)< diff:
                diff = diff_function(user_word,valid_words[i],limit)
                best_valid = valid_words[i]

            i += 1
        if diff <= limit:
            return best_valid
        else:
            return user_word

    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    if limit < 0:
        return 1
    if min(len(start),len(goal))== 0:
        if limit -(len(start)+len(goal))<0:
            return 1 +len(start)+len(goal)
        return len(start) + len(goal)
    else:
        if start[0]!=goal[0]:
            count =1
        else:
            count =0
        return count + shifty_shifts(start[1:],goal[1:],limit - count)
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    if limit < 0:
        return 1
    elif len(start)== 0 or len(goal) == 0: # Fill in the condition
        # BEGIN
        # END
        add_count = len(start)+len(goal)
        # if limit < add_count:
        #     return 1 + add_count
        return add_count


    else:
        add_diff = 1 + pawssible_patches(start , goal[1:],limit - 1)
        remove_diff = 1 + pawssible_patches(start[1:],goal, limit -1) 
        is_sub = 1
        if start[0] == goal[0]:
            is_sub = 0
        substitute_diff = is_sub + pawssible_patches(start[1:],goal[1:],limit -is_sub)
        # BEGIN
        "*** YOUR CODE HERE ***"
        return min(add_diff, remove_diff, substitute_diff)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    weight = [0.7, 0.3]
    diff_fuc_list = [pawssible_patches, shifty_shifts]
    i = 0 
    w_diff = 0 
    while i<2:
        w_diff = weight[i]*diff_fuc_list[i](start, goal, limit)
        i +=1
    return min(limit + 1, w_diff)

###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    i = 0
    while i < min(len(prompt),len(typed)) and typed[i] == prompt[i]:
        i += 1
    progress = (i) /len(prompt)
    will_send = {"id" : user_id,'progress': progress  }
    send(will_send)
    return progress
        

    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    times =[]   
    for lis in times_per_player:
        i = 0
        while i<len(lis) - 1:
            lis[i] = lis[i+1] - lis[i]
            i += 1
        lis_remove_last = lis[:len(lis)-1]
        times.append(lis_remove_last)
    return game(words, times)

    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = len(all_times(game))  # contains an *index* for each player
    word_indices = len(all_words(game))    # contains an *index* for each word
    # BEGIN PROBLEM 10  
    all_time = all_times(game )
    final_ls=[[] for i in range(player_indices)]
    k = 0
    while k <word_indices:
        fast_play = 0
        j = 1
        while j<player_indices:
            if all_time[j][k]< all_time[fast_play][k]:
                fast_play =j
            j += 1
        final_ls[fast_play].append(word_at(game,k))
        k +=1
    return final_ls


    "*** YOUR CODE HERE ***"
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
