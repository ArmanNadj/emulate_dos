from bots import BotDispatcher
import os

if __name__ == "__main__":
    whichSite = input("Which site to ping: ")
    while os.system("ping -c 1 " + whichSite) != 0:
        whichSite = input("\nUnable to reach host. Enter valid host name: ")
    print("\nSuccesfully found host...\n")
    
    howManyBots = 1
    correctBotAmount = False
    while not correctBotAmount:
        try:
            howManyBots = int(input("How many bots to deploy (> 0): "))
            if howManyBots <= 0:
                continue
        except Exception as e:
            continue
        correctBotAmount = True
        
    print("\n------------- BEGIN ---------------\n")
    distcenter: BotDispatcher = BotDispatcher(whichSite, howManyBots)
    distcenter.distribute()
    distcenter.evaluate()
    print("\n------------- END ---------------\n")
        