import random
from art import *
import json
def main():
    tprint("RANDOM  TWEET  GENERATOR", font='small')

    filename = 'source.json'
    with open(filename, 'r') as file:
        data = json.load(file)
        starts = data['starts']
        middles = data['middles']
        qualifiers = data['qualifiers']
        finishes = data['finishes']

    tweet_maker(starts, middles, qualifiers, finishes)
def tweet_maker(starts, middles, qualifiers, finishes):
    rand_starts = random.choice(starts)
    rand_middles = random.choice(middles)
    rand_qualifiers = random.choice(qualifiers)
    rand_finishes = random.choice(finishes)


    print(rand_starts + " " + rand_middles + " " + rand_qualifiers + " " + rand_finishes)

if __name__ == '__main__':
    main()