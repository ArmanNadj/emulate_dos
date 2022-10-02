import os
import threading
import time
from enum import Enum

#status of Bot
class STATUS(Enum):
    SUCCESS = 1
    FAILURE = 2
 
#Bot class that will run the ping on it's own thread       
class Bot:
 
    id: int
    response: int
    hostToAttack: str
    status: STATUS
    
    def __init__(self, id, hostToAttack):
        self.id = id
        self.hostToAttack = hostToAttack

    def ping(self):
        self.response = os.system("ping -c 1 " + self.hostToAttack)
        self.status = self.eval_response()
        
    def eval_response(self) -> STATUS:
        if self.response == 0:
            print('Ping succeeded from bot #' + str(self.id))
            return STATUS.SUCCESS
        else:
            print('Ping failed from bot #' + str(self.id))
            return STATUS.FAILURE
            

# Dispatches bots to perform their operation
class BotDispatcher:
    hostname: str # who we are pinging
    amountOfBots: int # how many times we are pinging
    bots = []
    successfulBots = []
    failedBots = []
    
    def __init__(self, hostname, amountOfBots):
        self.hostname = hostname
        self.amountOfBots = amountOfBots
        
    def distribute(self):
        for i in range(self.amountOfBots):
            tempBot = Bot(i + 1, self.hostname)
            self.bots.append(tempBot)
            threading.Thread(target=tempBot.ping(), name=str(tempBot.id))
            time.sleep(1)
            
    def evaluate(self):
        self.successfulBots = [x for x in self.bots if x.status == STATUS.SUCCESS]
        self.failedBots = [x for x in self.bots if x.status == STATUS.FAILURE]
        
        print("\n------- Successful Bots -------\n")
        if len(self.successfulBots) > 0:
            for i in self.successfulBots:
                print("Bot ID #" + str(i.id))
        else:
            print("No successful bots...")
        
        
        print("\n------- Failed Bots -------\n")  
        if len(self.failedBots) > 0: 
            for i in self.failedBots:
                print("Bot ID #" + str(i.id))
        else:
            print("No failed bots....")