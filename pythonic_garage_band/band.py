from abc import ABC,abstractmethod



class Musician:
    """
    Musician Class
    """
    def __init__(self,name,instrument='',solo=''):
        self.name = name
        self.instrment = instrument
        self.solo = solo

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo


class Guitarist(Musician):
    """
   Guitarist Class
    """
    def __str__(self):
        
        return f"My name is {self.name} and I play guitar"

        
    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    def get_instrument(self):
        return 'guitar'
    def play_solo(self):

       return "face melting guitar solo"




class Drummer(Musician):
    """
    Drummer Class
    """
    def __str__(self):
        return f"My name is {self.name} and I play drums"


    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"


    def get_instrument(self):
        return "drums"



    def play_solo(self):

        
       return "rattle boom crash"





class Bassist(Musician):
    """
    Bassist Class
    """
    def __init__(self,name):
        self.name = name
        self.instrument = 'bass'
        self.solo = "bom bom buh bom" 

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


       
class Band:
    instances=[]
    def __init__(self,name:str,members=[]):
        self.name=name
        self.members=members
        Band.instances.append(self)



    def play_solos(self):
        players = []
        for i in self.members:

            players.append(i.play_solo())
            
        return players

        
    @classmethod
    def to_list(cls):
        return cls.instances
