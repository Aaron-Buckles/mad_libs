import os
import re

tags = {'<n>': 'noun',
        '<a>': 'adjective',
        '<v>': 'verb',
        '<nat>': 'nationality',
        '<per>': 'person',
        '<pn>': 'plural noun',
        '<num>': 'number',
        '<pshape>': 'plural shape',
        '<food>': 'food',
        '<g>': 'game',
        '<ing>': "verb ending in 'ing'",
        '<plant>': 'plant',
        '<body>': 'part of the body',
        '<place>': 'a place',
        '<name>': 'name',
        '<shout>': 'something to shout',
        '<feel>': 'feeling'}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_available_stories():
    clear_screen()
    available_stories = []

    files = os.listdir('stories')
    for file in files:
        if ".txt" in file:
            available_stories.append(file[:-4].capitalize())

    for story_name in available_stories:
        print(story_name)


def choose_story():
    show_available_stories()
    while True:
        story_name = input("Choose a story: ").lower()
        try:
            f = open("stories\{}.txt".format(story_name), "r")
        except FileNotFoundError:
            print("{} does not exist. Try again.".format(story_name))
            
        else:
            story = f.read()
            f.close()
            clear_screen()
            return story, story_name


def parse_story(story):
    blanks = re.findall(r"<\w+>", story)

    for blank in blanks:
        user_input = input("{}: ".format(tags[blank].capitalize())).strip()
        story = story.replace(blank, user_input, 1)

    return story


while True:
    story, story_name = choose_story()
    story = parse_story(story)

    clear_screen()

    print(story_name.capitalize())
    print(story)

    play_again = input("Do you want to play again? [y/N] ")
    if play_again.lower() == 'n':
        break
