import random

def get_word_points(word):
    word_letters = list(word)
    total_word_points = 0
    one_point_list = ['E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U']
    two_point_list = ['D', 'G']
    three_point_list = ['B', 'C','M','P']
    four_point_list = ['F', 'H', 'V', 'W', 'Y']
    five_point_list = ['K']
    eight_point_list = ['J', 'X']
    ten_point_list = ['Q', 'Z']


    for letter in word_letters:
        if letter in one_point_list:
            total_word_points += 1
        elif letter in two_point_list:
            total_word_points += 2
        elif letter in three_point_list:
            total_word_points += 3
        elif letter in four_point_list:
            total_word_points += 4
        elif letter in five_point_list:
            total_word_points += 5
        elif letter in eight_point_list:
            total_word_points += 8
        elif letter in ten_point_list:
            total_word_points += 10

    return total_word_points

def create_bag():
    bag = []
    for i in range (0,12):
        bag.append('E')

    for i in range(0,9):
        bag.append('A')
        bag.append('I')

    for i in range(0,8):
        bag.append('O')

    for i in range(0,6):
        bag.append('N')
        bag.append('R')
        bag.append('T')

    for i in range(0,4):
        bag.append('L')
        bag.append('S')
        bag.append('U')
        bag.append('D')

    for i in range(0,3):
        bag.append('G')

    for i in range(0,2):
        bag.append('B')
        bag.append('C')
        bag.append('M')
        bag.append('P')
        bag.append('F')
        bag.append('H')
        bag.append('V')
        bag.append('W')
        bag.append('Y')

    for i in range(0,1):
        bag.append('K')
        bag.append('J')
        bag.append('X')
        bag.append('Q')
        bag.append('Z')
    
    return bag

def get_player_hand():
    bag = create_bag()
    random.shuffle(bag)
    player_rack = [bag.pop(0),bag.pop(0),bag.pop(0),bag.pop(0),bag.pop(0),bag.pop(0),bag.pop(0)]

    return player_rack

def find_valid_word():
    letters = get_player_hand()
    dictionary = open("dictionary.txt")

    possible_words = []
    confirmed_words = []

    for possible_word in possible_words:
        if possible_word in dictionary.read():
            confirmed_words.append(possible_word)
