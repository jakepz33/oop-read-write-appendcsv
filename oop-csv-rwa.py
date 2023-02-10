#Altering 2...
import csv

#with block *** creates the csv file
with open("transaction_records.csv", "w") as file: 
  writer = csv.writer(file, lineterminator = '\n')

  #write the header row
  header= ["ID", "Name", "Status", "Due date", "Amount"]
  writer.writerow(header)



print("Welcome to transaction tracker!")
#action = input("What would you like to perform (import/statistics)? ")
listid = []
count = 0
numtrans = 0
repeat = True
uploaded_file = 0
pending = 0
statsidref = []

#KEEP THE CODE GOING
while repeat:
  count = 0
  action = input("What would you like to perform (import/statistics)? ")
# Asking to import a csv file
  if action.lower() == "import":
    new_file = input("Which file would you like to import? ")
    #READ FILE AND STORE AS LISTS
    try:
      with open(new_file, 'r') as f1:
        reader = csv.reader(f1)
        for line in reader: 
          rows = line #STORE LINES AS ROWS
          if line[0] not in listid: #ITERATE AT 0 INDEX
            #APPEND TO CSV
            with open('transaction_records.csv', 'a') as f1:
              writer = csv.writer(f1, lineterminator = '\n')
              idnum = line[0] #APPEND TO LIST OF IDs IN USE
              count = count+1 #COUNT THE NUMBER OF TRANSACTIONS ADDED
              numtrans = numtrans+1 #COUNT NUMBER OF TOTAL TRANSACTIONS
              listid.append(idnum)
              writer.writerow(rows) #WRITE DATA TO CSV
          else:
            print('Data for ID: ', line[0], 'already in transaction records') #IF ID IN USE PRINT THIS
        print(f'{count} transactions loaded')

      uploaded_file += 1
    #SHOW ERROR IF NO FILE EXISTS
    except FileNotFoundError:
      print("That file doesnt exist")

  #STATISTICS
  elif action.lower() == "statistics":
    if uploaded_file <= 0: #USE TO TRACK IF FILE IS LOADED
      print("Sorry, no transaction data was loaded yet. Please try again.")
    else:
      with open('transaction_records.csv', 'r') as file:
        reader = csv.reader(file) #LAYOUT DATA AS LISTS
        for line in reader:
          row = line

          statsid = line[0]
          #statsidref.append(statsid)
          if statsid not in statsidref: #so we dont add to pending everytime its ran
            statsidref.append(statsid)

            if row[2] == 'PENDING': #GET ROW INDEX
              trans_pending = row[4]
              new_int = int(trans_pending) #MAKE INTO INT
              pending = pending + new_int
              '''pending.append(new_int)
              add = sum(pending)'''
            

        print(f'Number of lifetime transactions: {numtrans}')
        print(f'Total dollar amount pending: {pending}')
  else:
    print("Please choose between import or statistics")

  decision = input("Would you like to run further analysis? (yes/no)? ")

  if decision.lower() != 'no' and decision.lower() != 'yes':
    print('Please enter yes or no')
  elif decision.lower() == 'yes':
    repeat = True
  else:
    repeat = False


print("thank you")
print('new line')

