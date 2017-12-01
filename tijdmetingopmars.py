# tijdmeting op mars Jordy Kruijer S1096853

# invoer sol (sol)
Sol = int(input("Geef het aantal sol in: "))

# omrekenen Sol omzetten in seconden
SolOmrekenenFormule = 35.244 + (39 * 60) + (24 * 60 * 60)
SolInSeconde = Sol * SolOmrekenenFormule

# aarddag in seconden
AardDagInSeconden = (24 * 60 * 60)
AardUurInSeconden = (60 * 60)
AardMinInSeconden = 60

# omrekenen resultaat naar dagen, uren, minuten, seconden
AardDagen = SolInSeconde / AardDagInSeconden    #hier bereken ik hoeveel dagen hier in zitten
RestNaDag = SolInSeconde % AardDagInSeconden    #hier bereken ik de rest waarmee ik verder kan rekenen
AardUren = RestNaDag / AardUurInSeconden        #hier bereken ik de uren
RestNaUur = RestNaDag % AardUurInSeconden       #hier bereken ik de rest
AardMin = RestNaUur / AardMinInSeconden         #hier bereken ik de minuten
RestNaMin = RestNaUur % AardMinInSeconden       #hier bereken ik de rest, dit zijn de seconden

# uitvoer in aardtijd in natuurlijke getallen(uitvoer)
print(Sol, "soldagen = ", int(AardDagen), "dagen, ", int(AardUren), "Uren, ",
      int(AardMin), "Minuten en", int(RestNaMin), "Seconden") #int wordt gebruikt om de waardes te veranderen in int's

#print(Sol, "soldagen = ", AardDagen, "dagen, ", AardUren, "Uren, ",
#      AardMin, "Minuten, ", RestNaMin, "Seconde") #dit is een controle lijn, om afrondingen te controleren
