# euromunten Jordy Kruijer

# invoer vragen voor munten
EenCent = int(input())
TweeCent = int(input())
VijfCent = int(input())
TienCent = int(input())
TwintigCent = int(input())
VijftigCent = int(input())
EenEuro = int(input())
TweeEuro = int(input())

# Berekenen aantal munten
TotaleAantal = EenCent + TweeCent + VijfCent + TienCent + TwintigCent + VijftigCent + EenEuro + TweeEuro  #Aantallen bij elkaar

# berekenen waarde munten
TotaleWaarde = (EenCent * 0.01) + (TweeCent * 0.02) + (VijfCent * 0.05) + (TienCent * 0.10) + (TwintigCent * 0.20) + (VijftigCent * 0.50) + (EenEuro * 1.0) + (TweeEuro * 2.0)  #aantal keer de waarde

# genereren uitvoer
print(TotaleAantal)
print(TotaleWaarde)