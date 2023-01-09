# In[] Funzione Extend 
list = [1,2,3,4,5]  # Funzione che funziona soltanto con le liste

list2 = [6,7]

list.extend(list2)      # Aggiunge una lista ad un altra lista 
list.extend([8,9,10])

print(list)


# In[] Aperura di un file in un altra Directory (cartella)

a = "/Users/matteo/Documents/GitHub/Calcolatori/Lecture 8/Lecture8.py"
                            #! Metodo per aprire un file in una directory diversa da quella in cui si sta lavorando
f = open(a)                 # Apertura file in modalita di lettura (Default)

for line in f:              # Esempio: programma che stampa tutte le righe del file
    print(line)

f.close()                   # E'importante chiudere i file aperti per risparmiare memoria

# In[] Modalità di aperura di un file 
open('Employees.txt')        #! Non serve dichiarare tutto il percorso sei il file si trova nella stessa cartella in cui si sta lavorando

open('Employees.txt', 'r')   # Apertura file in modalita di lettura (Metodo non standard)
open('Employees.txt', 'w')   # Apertura file in modalita di scrittura (Permette di modificare il file)
open('Employees.txt', 'r+')  # Apertura file in modalita di lettura e scrittura 
open('Employees.txt', 'a')   # Apertura file in modalita append (Si possono aggiungere solo informazion alla fine)


# In[] Modalita Lettura
employee_file = open('Employees.txt', 'r') 

print(employee_file.readable())   # Funzione che ci dirà se il file è legibile o no (risultato buleano)
                                  # In questo caso è True, perche il file è in modalita Read (r)

print(employee_file.read())       # Stamapa tutto il file

print(employee_file.readline())   # Stamapa la prima linea
print(employee_file.readline())   # Stamapa la seconda linea
print(employee_file.readline())   # Stamapa la terza linea

print(employee_file.readlines())      # Stampa una lista contenente tutte le linee del file
print(employee_file.readlines()[3])   # Stapa soltanto la linea specificata nel index

for employee in employee_file.readlines():  # Ciclo for per stampare tutte le righe 
    print(employee)

employee_file.close

# In[] Modalita Append
employee_file = open('Employees.txt', 'a')

employee_file.write("Toby - human Resources")      # Testo aggiunto alla fine del file 
employee_file.write("\nKelly - Customer Service")  # \n è fondamentale, senza tutti testi verrebbero scritti sulla stessa riga

employee_file.close()

# In[] Modalita Write Override
employee_file = open('Employees.txt', 'w')

employee_file.write("Toby - human Resources")   # Write override tutto il testo, cancellando tutto quello che cera prima

employee_file.close()

# In[] Modalita Write Nuovo File
employee_file = open('Employees_new.txt', 'w')  # Se il file citato non esiste nella directory in cui si lavora
                                                # Ne verrà creato uno
employee_file.write("This is a new file")

employee_file.close()

# In[] Extend di una lista 