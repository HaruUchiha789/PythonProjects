# Module with few madlib functions

class madlibs():
    def __init__(self):
        self.yourname= input("yourname:")
        self.rival=input("rival: ")
        self.middleschool=input("middleschool: ")
        self.dreamschool=input("dreamschool: ")
        self.favauthor=input("favauthor: ")
        self.nickname=input("nickname: ")
        self.yourcrush=input("yourcrush: ")
        self.relationship= input("anyrelationship: ")
        self.club=input("schoolclub: ")
        self.bodypart=input("bodypart: ")
        self.mysticcreature=input("mysticcreature: ")
        self.enemyname=input("enemyname: ")


    def sport(self):
        madlib=f"""A chance event triggered {self.yourname}'s love for volleyball. 
        His club had no members, but somehow persevered and finally made it into its very first and 
        final regular match of {self.middleschool}, where it was steamrolled by {self.rival}, 
        a superstar player known as "King of the Court." Vowing revenge, 
        {self.yourname} applied to the {self.dreamschool} volleyball club... 
        only to come face-to-face with his hated rival, {self.rival}! 
        A tale of hot-blooded youth and volleyball from the pen of {self.favauthor}!! """
        print(madlib)

    def romance(self):
        madlib=f"""{self.yourname} is completely misunderstood by her classmates. 
        Her timid and sweet demeanor is often mistaken for malicious behavior. 
        This is due to her resemblance to the ghost girl from "The Ring", 
        which has led her peers to give her the nickname {self.nickname}. 
        Longing to make friends and live a normal life, she is naturally drawn to {self.yourcrush}, 
        the most popular guy in class, whose "100% refreshing" personality earns him great admiration from {self.yourname}. 
        So when {self.yourcrush} starts talking to her, maybe there is hope for the friendships {self.yourname} has always longed for. 
        Maybe...there is even a little hope for some {self.relationship} in her future. """
        print(madlib)


    def action(self):
        madlib=f"""{self.yourname}, a kind-hearted teenager, joins his school's {self.club} Club for fun,
         but discovers that its members are actual sorcerers who can manipulate the energy between beings for their own use. 
         He hears about a cursed object - the {self.bodypart} of {self.enemyname}, a {self.mysticcreature} - and its being targeted by other cursed beings. 
         He eats the finger to protect his friends, and ends up becoming {self.enemyname}'s host. 
         However, {self.yourname} discovers that he has inherited magic and is able to control this power without interference from {self.enemyname}. 
         He joins the {self.dreamschool} Magic Technical College to consumes all of {self.enemyname}'s {self.bodypart}, 
         which will enable a full exorcism to take place that will free him. """
        print(madlib)

