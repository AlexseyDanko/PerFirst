class Animals:
    def __init__(self,name,family="living creatures",number_of_limbs=4,food="maybe meat,fish,seafood and another",speed_of_movement="from 1 to 110 km/h"):
        self.speed_of_movement=speed_of_movement
        self.name=name
        self.family=family
        self.number_of_limbs=number_of_limbs
        self.food=food
        self.skills_people=" body skills of people no limits"
        self.max_speed_people = "  40 km/h  "
        self.max_speed_dog = "  60 km/h  "
        self.max_speed_cat = "  15 km/h  "
        self.Mspeed_animals="  from 5 to 110 km/h  "
        self.skill_dog = "  Playning, jump and run  "
        self.skill_cat = "  clever  "
        self.feature_of_the_body_cat = "flexibility"
        self.top_speed_Cheetach = 100
        self.top_speed_Tiger = 60
        self.top_speed_Lion = 55
        self.life_expectancy_Cheetach = "  from 10 to 20 years  "
        self.life_expectancy_Tiger = "  from 10 to 15 years  "
        self.life_expectancy_Lion = "  from 7 to 15 years  "

    def description(self):
        print(" Hello this " + self.name +" "+ self.family + " likes to eat " + self.food + " has " + str(self.number_of_limbs) + " paws " + " speed of movement " + str(self.speed_of_movement) + " km/h ")
    def top_speed(self):
        if self.name == "Cheetach":
            print(self.name + " Max speed " + str(self.top_speed_Cheetach))
        elif self.name == "Tiger":
            print(self.name + " Max speed " + str(self.top_speed_Tiger))
        else:
            print(self.name + " Max speed " + str(self.top_speed_Lion))
    def life_expectancy(self):
        if self.name == "Cheetach":
            print(self.name + " Life Expectancy " + str(self.life_expectancy_Cheetach))
        elif self.name == "Tiger":
            print(self.name + " Life Expectancy " + str(self.life_expectancy_Tiger))
        else:
            print(self.name + " Life Expectancy " + str(self.life_expectancy_Lion))

    def skills_cat(self):
        print(self.name +" "+ self.skill_cat + " and " + self.feature_of_the_body_cat)
    def skills_dog(self):
        print(self.name+" "+ self.skill_dog)
    def skills_peoples(self):
        print(self.name+ " "+self.skills_people)

class Cat(Animals):
    def __init__(self,name,family="living creatures",number_of_limbs=4,food="maybe meat,fish,seafood and another",speed_of_movement="from 1 to 110 km/h"):
        super().__init__(name,family,number_of_limbs,food,speed_of_movement)
        self.hobby="sharpen claws"
    def MSpeed_cat(self):
        print(self.name + "  Maximum speed " + str(self.max_speed_cat))
    def description(self):
        print(" Hello this " + self.name +" "+ self.family+"  family" + " likes to eat " + self.food + " has " + str(self.number_of_limbs) +"  paws")
    def skills_cat(self):
        print(self.name +" "+ self.skill_cat +"Like play with ball")

    def runing(self):
        print(self.name+" " + "Like run")
    def jumping(self):
        print(self.name+" " + "Like jump")

class Dog(Animals):
    def __init__(self,name,family="living creatures",number_of_limbs=4,food="maybe meat,fish,seafood and another",speed_of_movement="from 1 to 110 km/h"):
        super().__init__(name,family,number_of_limbs,food,speed_of_movement)
        self.hobby="gnawing slippers"
    def description(self):
        print(" Hello this " + self.name +" "+ self.family+"  family" + " likes to eat " + self.food)
    def MSpeed_dog(self):
        print(self.name + "  Maximum speed " + str(self.max_speed_dog))
    def skills_dog(self):
        print(self.name+ "  has a powerful charm")

    def playning(self):
        print(self.name +" "+"Like play with ball")

    def goodfriends(self):
        print(self.name +" "+ "Best friend for people")

class People(Animals):
    def __init__(self,name,family="living creatures",number_of_limbs=4,food="maybe meat,fish,seafood and another",speed_of_movement="from 1 to 110 km/h"):
        super().__init__(name,family,number_of_limbs,food,speed_of_movement)
        self.__hobby="music,racing and another"
    def description(self):
        print(" Hello this " + self.name +" "+ self.family+"  family")
    def skills_peoples(self):
        print(self.name+ "  first Homo sapiens")

    def MSpeed_people(self):
        print(self.name + "  Maximum speed " + str(self.max_speed_people))

    def Iq(self):
        print(self.name +" "+"Homo sapiens")

    def emotional(self):
        print(self.name +" "+" Very emotional animal")