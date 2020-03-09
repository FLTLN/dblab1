from dbio import load
from dbio import save
from dbio import export

from ui_routine import print_command_list
from ui_routine import wait_for_user_response
from ui_routine import execute_search
from ui_routine import execute_add
from ui_routine import execute_del
from ui_routine import execute_edit

import os
import argparse

parser = argparse.ArgumentParser(description="Database management system.")

parser.add_argument('-p', '--path', required=True,  type=str, help='Path to .txt file with database.')
parser.add_argument('-n', '--new', required=False, type=bool, default=False, help='Create new database')


args = parser.parse_args()

print("┌{:─^62}┐".format(""))
print("│{: ^62}│".format("Welcome to the database management system."))     
print("└{:─^62}┘".format(""))

print("┌{:─^62}┐".format(""))  
print("│{: <62}│".format(" Input path:"))
print("│{: <62}│".format(" {}".format(args.path)))
print("│{: <62}│".format("")) 
print("│{: <62}│".format(" Checking input path."))  

if not os.path.exists(os.path.dirname(args.path)):
    print("│{: <62}│".format("")) 
    print("│{: <62}│".format(" Directory with file does not exist.")) 
    print("│{: <62}│".format(" Please, check path."))
    print("│{: <62}│".format("")) 
    print("│{: <62}│".format(" Checking input path - failed."))
    print("└{:─^62}┘".format(""))
    exit(1)

if args.new:
    print("│{: <62}│".format(" Checking input path - done."))
    print("│{: <62}│".format("")) 
    print("│{: <62}│".format(" Creating database."))
    try:
        temp = open(args.path, "tw")
        temp.close
    except:
        print("│{: <62}│".format("")) 
        print("│{: <62}│".format(" Something went wrong while creating new database."))
        print("│{: <62}│".format("")) 
        print("│{: <62}│".format(" Creating database - failed."))
        print("└{:─^62}┘".format("")) 
        exit(1)
    print("│{: <62}│".format(" Creating database - done."))
else:
    if not os.path.isfile(args.path):
        print("│{: <62}│".format("")) 
        print("│{: <62}│".format(" Path is not a file.")) 
        print("│{: <62}│".format(" Please, check path.")) 
        print("│{: <62}│".format("")) 
        print("│{: <62}│".format(" Checking input path - failed."))
        print("└{:─^62}┘".format(""))
        exit(1)

    print("│{: <62}│".format(" Checking input path - done."))
print("│{: <62}│".format("")) 
print("│{: <62}│".format(" Opening database."))  

data = None

try:
    data = load(args.path)
except:
    print("│{: <62}│".format("")) 
    print("│{: <62}│".format(" Something went wrong while opening database."))
    print("│{: <62}│".format(" Please, check that .txt file have right format."))
    print("│{: <62}│".format("")) 
    print("│{: <62}│".format(" Opening database - failed."))
    print("└{:─^62}┘".format("")) 
    exit(1)
    
print("│{: <62}│".format(" Opening database - done."))
print("└{:─^62}┘".format(""))

print("┌{:─^62}┐".format(""))
print("│{: ^62}│".format("Database loaded and ready to work."))     
print("└{:─^62}┘".format(""))

print_command_list()

while True:
    print("┌{:─^62}┐".format(""))
    print("│{: <62}│".format(" Waiting for command."))     
    print("└{:─^62}┘".format(""))
    command = wait_for_user_response(['h','f','q','a','d','s','e','backup','export'])
    if command == 'h':
        print_command_list()
    if command == 'f':
        execute_search(data)
    if command == 'a':
        execute_add(data)
    if command == 'd':
        execute_del(data)
    if command == 's':
        print("┌{:─^62}┐".format(""))
        print("│{: <62}│".format(" Saving database."))     
        try:
            save(data, args.path)
            data = load(args.path)
            print("│{: <62}│".format("")) 
            print("│{: <62}│".format(" Database saved."))     
            print("└{:─^62}┘".format(""))
        except:
            print("│{: <62}│".format("")) 
            print("│{: <62}│".format(" Something went wrong when saving database."))     
            print("└{:─^62}┘".format(""))

    if command == 'e':
        execute_edit(data)
    if command == 'q':
        quit(0)

    if command == 'backup':
        print("┌{:─^62}┐".format(""))
        print("│{: <62}│".format(" Creating backup.")) 
        backup_path = os.path.splitext(args.path)[0] + "_backup.txt"
        try:
            save(data, backup_path)
            print("│{: <62}│".format("")) 
            print("│{: <62}│".format(" Backup created."))     
            print("└{:─^62}┘".format(""))
        except:
            print("│{: <62}│".format("")) 
            print("│{: <62}│".format(" Something went wrong when creating backup."))     
            print("└{:─^62}┘".format(""))

    if command == 'export':
        print("┌{:─^62}┐".format(""))
        print("│{: <62}│".format(" Export .csv.")) 
        export_path = os.path.splitext(args.path)[0] + ".csv"
        try:
            export(data, export_path)
            print("│{: <62}│".format("")) 
            print("│{: <62}│".format(" Export done."))     
            print("└{:─^62}┘".format(""))
        except:
            print("│{: <62}│".format("")) 
            print("│{: <62}│".format(" Something went wrong when exporting .csv."))     
            print("└{:─^62}┘".format(""))


     