from routine import print_record
from routine import find_record
from routine import add_record
from routine import delete_record

def print_command_list():
    print("┌{:─^62}┐".format(""))
    print("│{: <62}│".format(" Command list: "))    
    print("│{: <62}│".format(""))    
    print("│{: <62}│".format(" h - show command list."))    
    print("│{: <62}│".format(" a - add record."))    
    print("│{: <62}│".format(" f - find record."))    
    print("│{: <62}│".format(" e - edit record."))    
    print("│{: <62}│".format(" d - delete record."))    
    print("│{: <62}│".format(" s - save database."))    
    print("│{: <62}│".format(" q - quit."))
    print("│{: <62}│".format("")) 
    print("│{: <62}│".format(" Additional commands: "))
    print("│{: <62}│".format("")) 
    print("│{: <62}│".format(" backup - create backup."))     
    print("│{: <62}│".format(" export - export to .csv file."))     
    print("└{:─^62}┘".format(""))  

def wait_for_user_response(commands):
    while True:
        command = input(">> ")
        if command in commands:
            return command

        print("┌{:─^62}┐".format(""))  
        print("│{: <62}│".format(" {} - unvalid command".format(command)))
        print("└{:─^62}┘".format(""))

def execute_search(where):
    print("┌{:─^62}┐".format(""))  
    print("│{: <62}│".format(" Find records."))
    print("│{: <62}│".format(""))
    print("│{: <62}│".format(" Waiting for search request."))
    print("└{:─^62}┘".format(""))
    request = input(">> ")
    record = None
    if len(request.split(",")) != 4:
        print("┌{:─^62}┐".format(""))  
        print("│{: <62}│".format(" Unwalid search request syntax."))
        print("└{:─^62}┘".format(""))
        return
    record = find_record(where, request)
    if len(record) > 0:
        print("┌{:─^62}┐".format(""))  
        print("│{: <62}│".format(" Found records:"))
        print("└{:─^62}┘".format(""))
        print_record(where, record)
    else:
        print("┌{:─^62}┐".format(""))  
        print("│{: <62}│".format(" No records found."))
        print("└{:─^62}┘".format(""))

def execute_add(where):
    print("┌{:─^62}┐".format(""))  
    print("│{: <62}│".format(" Add record."))
    print("│{: <62}│".format(""))
    print("│{: <62}│".format(" Waiting for new record."))
    print("└{:─^62}┘".format(""))
    record = input(">> ")
    if len(record.split(",")) != 4:
        print("┌{:─^62}┐".format(""))  
        print("│{: <62}│".format(" Unwalid new record syntax."))
        print("└{:─^62}┘".format(""))
        return
    flag = add_record(where, record)
    if flag:
        print("┌{:─^62}┐".format(""))  
        print("│{: <62}│".format(" Following record added:"))
        print("└{:─^62}┘".format(""))
    else:
        print("┌{:─^62}┐".format(""))  
        print("│{: <62}│".format(" Record with ip [{}] allready exists:".format(record.split(",")[0])))
        print("└{:─^62}┘".format(""))
   
    print_record(where,  find_record(where, "{},*,*,*".format(record.split(",")[0])))

def execute_del(where):
    print("┌{:─^62}┐".format(""))  
    print("│{: <62}│".format(" Delete records."))
    print("│{: <62}│".format(""))
    print("│{: <62}│".format(" Waiting for search request."))
    print("└{:─^62}┘".format(""))
    request = input(">> ")
    record = None
    if len(request.split(",")) != 4:
        print("┌{:─^62}┐".format(""))  
        print("│{: <62}│".format(" Unwalid search request syntax."))
        print("└{:─^62}┘".format(""))
        return
    record = find_record(where, request)
    if len(record) > 0:
        print("┌{:─^62}┐".format(""))  
        print("│{: <62}│".format(" Found records:"))
        print("└{:─^62}┘".format(""))
        print_record(where, record)
    else:
        print("┌{:─^62}┐".format(""))  
        print("│{: <62}│".format(" No records found."))
        print("└{:─^62}┘".format(""))
        return

    print("┌{:─^62}┐".format(""))  
    print("│{: <62}│".format(" Are you shure you want to delete this records?"))
    print("│{: <62}│".format(" y/n"))
    print("└{:─^62}┘".format(""))

    command = wait_for_user_response(['y','n'])
    if command == 'y':
        delete_record(where, record)
        print("┌{:─^62}┐".format(""))  
        print("│{: <62}│".format(" Records deleted."))
        print("└{:─^62}┘".format(""))

def execute_edit(where):
    print("┌{:─^62}┐".format(""))  
    print("│{: <62}│".format(" Delete records."))
    print("│{: <62}│".format(""))
    print("│{: <62}│".format(" Waiting for search request."))
    print("└{:─^62}┘".format(""))
    request = input(">> ")
    record = None
    if len(request.split(",")) != 4:
        print("┌{:─^62}┐".format(""))  
        print("│{: <62}│".format(" Unwalid search request syntax."))
        print("└{:─^62}┘".format(""))
        return
    record = find_record(where, request)
    if len(record) > 1:
        print("┌{:─^62}┐".format(""))  
        print("│{: <62}│".format(" More than one record founded."))
        print("└{:─^62}┘".format(""))
        print_record(where, record)
        print("┌{:─^62}┐".format(""))  
        print("│{: <62}│".format(" Please, check search request."))
        print("└{:─^62}┘".format(""))
        return
    if len(record) == 0:
        print("┌{:─^62}┐".format(""))  
        print("│{: <62}│".format(" No records founded."))
        print("│{: <62}│".format(""))
        print("│{: <62}│".format(" Please, check search request."))
        print("└{:─^62}┘".format(""))
        return
    print("┌{:─^62}┐".format(""))  
    print("│{: <62}│".format(" Found record:"))
    print("└{:─^62}┘".format(""))
    print_record(where, record)
    print("┌{:─^62}┐".format(""))  
    print("│{: <62}│".format(" Are you shure you want to edit this records?"))
    print("│{: <62}│".format(" y/n"))
    print("└{:─^62}┘".format(""))    

    command = wait_for_user_response(['y','n'])
    if command == 'n':
        return

    existed_split = request.split(",")
    print("┌{:─^62}┐".format(""))  
    print("│{: <62}│".format(" Waiting for edited record."))
    print("│{: <62}│".format(" Fields with * will not be changed."))
    print("└{:─^62}┘".format(""))
    edited = input(">> ")
    edited_split = edited.split(",")
    if len(edited_split) != 4:
        print("┌{:─^62}┐".format(""))  
        print("│{: <62}│".format(" Unwalid edited record syntax."))
        print("└{:─^62}┘".format(""))
        return

    result_split = []
    for index in range(0, len(edited_split)):
        if edited_split[index] == "*":
            result_split.append(existed_split[index])
        else:
            result_split.append(edited_split[index])

    edited = ",".join(result_split)

    print("┌{:─^62}┐".format("")) 
    print("│{: <62}│".format(" Confirm changes?"))
    print("│{: <62}│".format(" y/n"))
    print("└{:─^62}┘".format(""))    

    command = wait_for_user_response(['y','n'])
    if command == 'n':
        return
    
    delete_record(where, record)
    add_record(where, edited)






