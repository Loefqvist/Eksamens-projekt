import random
#Importerer den indbyggede random-pakke i Python
#som bruges senere i koden til at blande bogstaverne i ord.


with open('input.txt', 'r', encoding='utf8') as input_file:
#Åbner filen input.txt til læsning ('r') og bruger 
#'utf8'-kodning for at sikre korrekt indlæsning af Unicode-tegn. 
#Denne fil gemmer inputtet til programmet.

#(encoding er fordi vi vil bruge en bestemt ascii )
   

    with open('output.txt', 'w', encoding='utf8') as output_file:
    #Åbner filen output.txt til skrivning ('w') og bruger 
    #'utf8'-kodning til at sikre korrekt skrivning af Unicode-tegn. 
    #Denne fil gemmer outputtet fra programmet.

      
        for line in input_file:
        #går over hver linje i inputfilen.


            words = line.split()
            #Opdeler hver linje i ord ved hjælp af split()-metoden
            #og gemmer disse ord i en liste words.


            for word in words:
            #Går over hvert ord i words-listen.


                
                if len(word) <= 2:
                    output_file.write(word + ' ')
                    continue
                #Hvis længden af ordet er mindre end eller lig med 2, 
                #skrives ordet uændret til outputfilen og
                #fortsætter til næste iteration (linje eller stykke) 
                #af for-løkken ved hjælp af continue.


                
                middle_letters = list(word[1:-1]) 
                random.shuffle(middle_letters) 
                scrambled_word = word[0] + ''.join(middle_letters) + word[-1]
                #Hvis længden af ordet er større end 2, 
                #gemmes midterste bogstaver af ordet 
                #(dvs. alle bogstaverne bortset fra det første og det sidste bogstav) i en liste middle_letters. 
                #random.shuffle()-metoden bruges derefter til at blande bogstaverne i middle_letters-listen.
                #De blandede bogstaver bruges derefter til at danne det "scramblede" ord, scrambled_word, 
                #som har det samme første og sidste bogstav som det oprindelige ord, men med blandede midterste bogstaver.


                output_file.write(scrambled_word + ' ')
                #Det scramblede ord skrives til outputfilen, efterfulgt af et mellemrum.

            output_file.write('\n')
            #Efter hver linje i inputfilen skrives en linjeskift i outputfilen for at adskille ordene fra forskellige linjer.
            #backslash n er et tegn for at skrive ny linje