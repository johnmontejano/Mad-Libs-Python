from __future__ import print_function # so works on Python 2 and 3 alike
from colors import red, green, blue, yellow
word_list = list()

def libs():
  verb = input("Type in a verb: ")
  word_list.append(verb)

  noun = input("Type in a noun: ")
  word_list.append(noun)

  pronoun = input("Type in a pronoun: ")
  word_list.append(pronoun)

  adjective = input("Type in an adjective: ")
  word_list.append(adjective)


  print(red('verb:red'))
  print(green('noun:green'))
  print(blue('pronoun:blue'))
  print(yellow('adjective:yellow'))


  print("I {} some {} then I've seen {}. I didn't realize it's {}" .format(red(verb), green(noun),blue(pronoun), yellow(adjective)))
  
  inputs = input('Enter R to show results: ')

  if inputs == 'r' or inputs == 'R':
    for list_item in word_list:
      print(list_item)
   
    
libs()
