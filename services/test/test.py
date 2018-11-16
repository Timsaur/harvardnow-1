import urllib2, urllib
import re
import random

#############################
##    Joke Function     ##
#############################

def getJoke(input):

    try:
        jokes = ["Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.", "Anton, do you think I'm a bad mother?  My name is Paul.", "My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.",
        		  "A ham sandwich walks into a bar and orders a beer, the bartender says 'sorry, we don't serve food here.'"]
        joke = jokes[random.randint(0,len(jokes)-1)]
    except Exception, e:
        print str(e)
        return "Why is six afraid of seven?  Because seven eight nine. .-. "

    return joke

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'To get a joke, use the format \'joke\'.'
    return s

## return proper format to use for getting weather
special = makeSpecial()

def eval(input):
    return getJoke(input)