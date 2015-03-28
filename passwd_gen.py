import string
import random


# TODO Remember with Phenetic alpha
# TODO Create unittests
# TODO write with pgp key

class Password():
    
    length = 8
    letters = True
    mixedcase = True
    numbers = False
    punctuation = False

    phenetic_alpha = {"A":"Alpha","B":"Bravo","C":"Charlie","D":"Delta","E":"Echo","F":"Foxtrot","G":"Golf","H":"Hotel","I":"India",
                      "J":"Juliet","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec",
                      "R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"X-ray","Y":"Yankee",
                      "Z":"Zulu"}

    def __init__(self,length=8,letters=True,mixedcase=True,numbers=False,punctuation=False):
        self.length = length
        self.letters = letters
        self.mixedcase = mixedcase
        self.numbers = numbers
        self.punctuation = punctuation 

    def create_password(self,length=None,repeat=True):
        
        if not length:
            length = self.length

        char_selection=""
        if self.letters == True:
            if self.mixedcase == True:
                char_selection += string.ascii_letters
            else:
                char_selection += string.ascii_lowercase

        if self.numbers == True:
            char_selection += string.digits
        
        if self.punctuation == True:
            char_selection += string.punctuation
    
        
        if not repeat:
            key = ""
            while(len(key)!=length):
                # issue what is not possible?
                # trying to produce a string with char we have if the len required
                # exceeds the number of chars available
                key += random.choice(char_selection)
                key = "".join(set(key))
        else:
            key = ''
            for i in range(length):
                key += random.choice(char_selection)

        return key

    # the password could be in the class
    def remember_password(self,password):
        remember = ""
        for i,v in enumerate(password):

            if v.upper() in self.phenetic_alpha.keys():
                remember += self.phenetic_alpha[v.upper()] +" "
            else:
                remember +=v + " "

        
        return remember
        

if __name__ == "__main__":
    p = Password(length=8,letters=True,mixedcase=True,numbers=True,punctuation=False)

    password = p.create_password(repeat=False)
    print password
    print p.remember_password(password)
