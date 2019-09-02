from __future__ import print_function  # so works on Python 2 and 3 alike
from colors import red, green, blue, yellow


def libs():
    word_list = list()

    verb = input("Type in a verb: ")
    word_list.append(verb)

    noun = input("Type in a noun: ")
    word_list.append(noun)

    pronoun = input("Type in a pronoun: ")
    word_list.append(pronoun)

    adjective = input("Type in an adjective: ")
    word_list.append(adjective)

    print("I ate some {} then I went to {} I didn't realize I ate {} I didn't realize I ate {} of them. I like playing the".format(
        red(verb), green(noun), blue(pronoun), yellow(adjective)))

    print('Your results:')
    print(word_list)


libs()
