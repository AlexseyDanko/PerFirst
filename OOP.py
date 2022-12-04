class Person:
    def __init__(self, surname, name, age, height, weight):
        self.surname = surname
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def hello(self):
        print(" Привет " +  self.surname  + "  "+  self.name   + " Ваш возраст "+ str(self.age) + " года " + " Ваш рост " + str(self.height) + " см " + " Ваш вес  " + str(self.weight) + " кг ")
    def hello_child(self):
        print(" Привет " + self.surname + "  " + self.name + " Ваш возраст " + str(self.age) + " лет " + " Ваш рост " + str(self.height) + " см " + " Ваш вес  " + str(self.weight) + " кг ")
    def hello_babies(self):
        print(" Привет " + self.surname + "  " + self.name + " Ваш возраст " + str(self.age) + " год " + " Ваш рост " + str(self.height) + " см " + " Ваш вес  " + str(self.weight) + " кг ")
    # def married(self):


class Animals:
    def __init__(self,name,sex,family,food,paws,speed):
        self.sex=sex
        self.max_speed_people=40
        self.max_speed_dog=60
        self.max_speed_cat= 15
        self.skill_dog="Playning, jump and run"
        self.skill_cat="clever"
        self.feature_of_the_body_cat="flexibility"
        self.name = name
        self.family = family
        self.food = food
        self.paws = paws
        self.speed = speed
        self.top_speed_Cheetach = 100
        self.top_speed_Tiger = 60
        self.top_speed_Lion = 55
        self.life_expectancy_Cheetach = "from 10 to 20 years"
        self.life_expectancy_Tiger = "from 10 to 15 years"
        self.life_expectancy_Lion = "from 7 to 15 years"




    def description(self):
        print(" Hello this " + self.name +" "+ self.family + " likes to eat " + self.food + " has " + str(self.paws) + " paws " + " speed of movement " + str(self.speed) + " km/h ")
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

    def _skills_cat(self):
        print(self.name +" "+ self.skill_cat + " and " + self.feature_of_the_body_cat)
    def _skills_dog(self):
        print(self.name+" "+ self.skill_dog)

class Cat(Animals):
    def __init__(self,name,sex,family,food,paws,speed):
        super().__init__(name,sex,family,food,paws,speed)
        self.__hobby="sharpen claws"
    def __MSpeed_cat(self):
        print(self.name + "  Maximum speed " + str(self.max_speed_cat))

    def runing(self):
        print(self.name+" " + "Like run")
    def jumping(self):
        print(self.name+" " + "Like jump")

class Dog(Animals):
    def __init__(self,name,sex,family,food,paws,speed):
        super().__init__(name,sex,family,food,paws,speed)
        self.__hobby="gnawing slippers"
    def __MSpeed_dog(self):
        print(self.name + "  Maximum speed " + str(self.max_speed_dog))

    def playning(self):
        print(self.name +" "+"Like play with ball")

    def goodfriends(self):
        print(self.name +" "+ "Best friend for people")

class People(Animals):
    def __init__(self,name,sex,family,food,paws,speed):
        super().__init__(name,sex,family,food,paws,speed)
        self.__hobby="music,racing and another"

    def __MSpeed_people(self):
        print(self.name + "  Maximum speed " + str(self.max_speed_people))

    def Iq(self):
        print(self.name +" "+"Homo sapiens")

    def emotional(self):
        print(self.name +" "+" Very emotional animal")


