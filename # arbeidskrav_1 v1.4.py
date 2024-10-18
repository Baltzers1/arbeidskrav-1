# arbeidskrav_1  v.1
# author Magnus Baltzersen PY1010-1 24H
# written in VS code

 
while True:                                                                         #Bruker While funksjonen for å kun ha gyldige tall i inputen
    try:
        print("Tast inn hvor mange km du kjører i året: (kun heletall)")
        km_kjort = int(input())                                                     #Valgte input() som int for å gjøre det litt vanskeligere for meg seg 
        
        # Totalkost el.bil
        fors_el         = 5000              # kr/år     forsikring         
        drivstoff_el    = 0.2               # kWh/km    drivstoff       
        strompris       = 2.00              # kr/kWh    pris kWh    
        bom_el          = 0.1               # kr/km     bomavgift

        # Totalkost co2 bil
        fors_co2         = 7500              # kr/år     forsikring  
        drivstoff_co2    = 1.0               # kWh/km    drivstoff       
        bom_co2          = 0.3               # kr/km     bomavgift

        # Kostnad felles for begge
        avgift           =  8.38 * 365       # kr/år     trafikkforsikringsavgift

        # Beregning av årlige kostnader for elbil
        drivstoffkost_el     = km_kjort * drivstoff_el * strompris
        bomkost_el           = km_kjort * bom_el 
        total_el             = fors_el + avgift + drivstoffkost_el + bomkost_el

        # Beregning av årlige kostnader for CO2-bil
        drivstoffkost_co2   = km_kjort * drivstoff_co2 
        bomkost_co2         = km_kjort * bom_co2  
        total_co2           = fors_el + avgift + drivstoffkost_el + bomkost_co2
        1
        # Kostnadsdifferanse
        kostdiff = total_co2 - total_el

        # Presentasjon av resultatene
        print("Årlige kostnader for elbil:", round(total_el), "kr")                  # Brukt funksjonen round() til null desimaler siden input er satt til int, hele tall
        print("Årlige kostnader for bensinbil:", round(total_co2), "kr")             
        print("Årlig kostnadsdifferanse:", round(kostdiff), "kr")
        break  

    except ValueError: 
        print("Ugyldig input! Vennligst skriv inn et gyldig heltall.")
        print("")                                                                    # Ønsket en linje mellom teksten over og teksten som kommer etter.


