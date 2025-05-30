from flask import Flask
from flask import render_template
import random

app = Flask(__name__)


headlinks = list()
headlinks.append(("https://www.google.com","Google"))
headlinks.append(("https://www.digitalocean.com","Digital Ocean"))

navlinks = dict()
navlinks['Compute'] = list()
navlinks['Compute'].append(("https://gemini.google.com/","Gemini AI"))


@app.route("/now")
def hello_world():
    return render_template("index.html")


@app.route("/")
def CreateTemplate():

    navlinks = dict()
    navlinks['Compute'] = list()
    navlinks['Storage'] = list()
    navlinks['Storage'].append(("/App/anfs_vol","ANFS Volume"))
    navlinks['Compute'].append(("/App/tf_vm","Virtual Machine"))
    return render_template("gen.html", headlinks=headlinks, navlinks=navlinks)



def get_random_quote(quotes_list):
    """
    Selects a random quote from the given list.

    Args:
        quotes_list: A list of strings, where each string is a quote.

    Returns:
        A randomly selected quote as a string.
    """
    if not quotes_list:
        return "The treasure chest of quotes is empty!"
    return random.choice(quotes_list)

@app.route("/fortune")
def fortune():
    
    quotes = [
        "The best way to predict the future is to invent it.",
        "Life is what happens when you're busy making other plans.",
        "Not all those who wander are lost.",
        "To be or not to be, that is the question; whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune...",
        "The only way to do great work is to love what you do.",
        "I have not failed. I've just found 10,000 ways that won't work.",
        "A day without sunshine is like, you know, night.",
        "It's hard to be a diamond in a rhinestone world.",
        "If you tell the truth, you don't have to remember anything.",
        "I'm on a seafood diet. I see food and I eat it.",
        "The early bird might get the worm, but the second mouse gets the cheese.",
        "I think, therefore I am. I think?",
        "Never trust a computer you can’t throw out a window.",
        "A computer once beat me at chess, but it was no match for me at kickboxing.",
        "The difference between stupidity and genius is that genius has its limits.",
        "Why do they call it rush hour when nothing moves?",
        "If at first you don't succeed, then skydiving definitely isn't for you.",
        "My software never has bugs. It just develops random features.",
        "The journey of a thousand miles begins with a single step... and a really good pair of shoes.",
        "I'm not superstitious, but I am a little stitious.",
        "Always borrow money from a pessimist. He won’t expect it back.",
        "If you think nobody cares if you’re alive, try missing a couple of car payments.",
        "Artificial intelligence is no match for natural stupidity.",
        "A clear conscience is usually the sign of a bad memory.",
        "Never put off till tomorrow what you can do the day after tomorrow just as well.",
        "The universe is a grand book, but it's written in a language we can't read without a good search engine.",
        "Happiness is just a biscuit away. Or maybe two.",
        "If you want to shine like the sun, first burn like the sun. (Or just use a really bright flashlight).",
        "Common sense is like deodorant. The people who need it most never use it.",
        "I told my wife she was drawing her eyebrows too high. She seemed surprised.",
        "Why is 'abbreviation' such a long word?",
        "The best things in life are free. The second best are very expensive.",
        "If life gives you lemons, make lemonade. Then find someone whose life has given them vodka and have a party.",
        "It's not a bug, it's an undocumented feature!",
        "Programming is like sex: one mistake and you have to support it for the rest of your life.",
        "There are 10 types of people in the world: those who understand binary, and those who don't.",
        "I would love to change the world, but they won't give me the source code.",
        "Computers are good at following instructions, but not at reading your mind.",
        "The road to success is always under construction.",
        "My therapist told me the way to achieve true inner peace is to finish what I start. So far I’ve finished two bags of M&Ms and a chocolate cake. I feel better already."
    ]

    # Get a random quote
    fortune_cookie = get_random_quote(quotes)

    return render_template("gen.html", headlinks=headlinks, navlinks=navlinks, fortune=fortune_cookie)
