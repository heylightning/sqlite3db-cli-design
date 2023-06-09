import sqlite3

print('''
Welcome to a CLI (Command Line Interface) to interact with the database.
Version 1.0.0
''')

conn = sqlite3.connect('experiX.db')
cursor = conn.cursor()

while(True):
    try:
        query = str(input("\nheylighting/sqlite3db-cli-design (experiX)\n$>>> "))

        while(query[len(query)-1] != ';'):
            queryTemp = str(input(">>> "))
            query = query + " " + queryTemp

        if(query == 'exit;' or query == 'exit ;'):
            print('Bye!'); exit()
        
        cursor.execute(query)
        print("Query Executed Successfully!\nWarnings: 0 Errors: 0\n")

        if(cursor.description != None):
            column_headers = []

            for iterating in range(len(cursor.description)):
                column_headers.append(cursor.description[iterating][0])

            for running in cursor.fetchall():
                decimal = 0
                for k in range(len(column_headers)):
                    print(f'{column_headers[decimal]}: {running[decimal]}\t', end='')
                    decimal+=1
                print('')
      
    except Exception as err:
        print(f'\n {err} \n')
            
conn.commit()
conn.close()