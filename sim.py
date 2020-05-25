import random
import math
bank = 5000000 #equal to 500USD
#initbet = 1 #Equal to .00000001 BTC
chance = 49.5 #set percentage chance of win
multi = 2 # set multiplier

def rolldice(maxnum):
    num1 = random.randint(0, maxnum)
    return num1

def start(bank):
    rollperc = (100 - chance) * 10000
    a = 20
    highbet = 0
    highbank = 0
    bet = round(bank // 10 ** (int(math.log(bank, 10)) - 1 + 1) / 2)
    initbet = bet
    sidewallet = 0
    totalbets = 0
    jcount = 0

    while(bank != 0):
        a=a-1

        if(bank > 99999999999): #Move amount to side wallet
            print("Moving to side waller")
            sidewallet = sidewallet + 1000000
            bank = bank - 1000000

        if (bet > 99999999999): #Adjust to return bet to starting value
            bet = initbet
            #quit() #uncomment to kill bot if bet is too high

        if (bank < 0): #Stop loss
            quit()

        rolled = rolldice(1000000) #call rolldice function
        print("You bet: ", bet, "You roll: ", rolled)
        bank = bank - bet #remove bet from bank
        totalbets = totalbets + 1 #calculate total bets

        if(bet > highbet): #calculate highest bet
            highbet = bet

        if(bank > highbank): #calculate highest bank value
            highbank = bank

        if (rolled >= rollperc):
            print("#########WIN!#########")
            jackpot = rolled%100000
            if(jackpot == 77777):
                print("JACKPOT!!!!")
                bank = bank + 11
                jcount = jcount + 1
            else:
                bank = bet * multi + bank  # calculate bank after winning
                print("Winnings: ", bet * multi - bet)

            print("Total in bank: ", bank)
            print("Total bets made: ", totalbets)
            print("Highest bet so far is: ", highbet)
            print("Highest bank so far is: ", highbank)
            print("Side wallet total: ", sidewallet)
            print("Jackpots hit: ", jcount)
            print("######################\n")
            if(random.randint(0,10) == 5):
                bet = 50 #adjust random increments, set to zero for none
            else:
                #bet = initbet
                bet = round(bank // 10 ** (int(math.log(bank, 10)) - 1 + 1) / 2)
        else:
            print("#########LOSE#########")

            bet = bet * 2 #Incease bet by 2

            print("Total in bank: ", bank)
            print("Total bets made: ", totalbets)
            print("Highest bet so far is: ", highbet)
            print("Highest bank so far is: ", highbank)
            print("Side wallet total: ", sidewallet)
            print("Jackpots hit: ", jcount)
            print("######################\n")

            if(bet > bank):
                print("#########Your Broke#########")
                exit()


start(bank)
