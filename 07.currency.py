#We just got home from a fun trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:
#🇨🇴 Colombian pesos
#🇵🇪 Peruvian soles
#🇧🇷 Brazilian reais
#Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

pe=int(input("What do you have left in pesos? "))
co=int(input("What do you have left in soles? "))
br=int(input("What do you have left in reais? "))
usd=pe*0.050 + co*0.27 + br*0.175
print(usd)
