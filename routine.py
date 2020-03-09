def print_col(col):
    if not col == None: 
        print("├{:─^15}┼{:─^20}┼{:─^20}┼{:─^4}┤".format("","","",""))
        print("│{:<15}│{:<20}│{:<20}│{:<4}│".format(col[0],col[1],col[2],col[3]))

def print_record(where, indexes):
    print("┌{:─^15}┬{:─^20}┬{:─^20}┬{:─^4}┐".format("","","",""))
    print("│{:<15}│{:<20}│{:<20}│{:<4}│".format("ip","user","hash","perm",))
    for index in indexes:
        print_col(where[0][index])
    print("└{:─^15}┴{:─^20}┴{:─^20}┴{:─^4}┘".format("","","",""))

def find_record(where, what):
    what = what.split(",")
    ip    = where[-1]
    name  = where[-1]
    hashh = where[-1]
    perm  = where[-1]

    if not(what[0] == "*"):
        if (what[0] in where[1]):
            ip = where[1][what[0]]
        else: 
            return []

    if not(what[1] == "*"): 
        if (what[1] in where[2]):
            name = where[2][what[1]]
        else: 
            return [] 

    if not(what[2] == "*"):
        if (what[2] in where[3]):
            hashh = where[3][what[2]]
        else: 
            return []

    if not(what[3] == "*"):
        if (what[3] in where[4]):
            perm = where[4][what[3]]
        else: 
            return []

    result = list(set(ip) & set(name) & set(hashh) & set(perm))

    return result

def add_ref(indexes, index, ref):
    if ref not in indexes:
        indexes[ref] = []
        indexes[ref].append(index)
    else:
        indexes[ref].append(index)

def add_record(where, record):

    record = record.split(",")
    if not find_record(where, "{},*,*,*".format(record[0])) == []:
        if not where[0][find_record(where, "{},*,*,*".format(record[0]))[0]] == None:
            return False
    try:
        ctr = where[-1][-1] + 1
    except:
        ctr = 0
    where[-1].append(ctr)

    where[0].append(record)

    where[1][record[0]] = [ctr]
    add_ref(where[2], ctr, record[1])
    add_ref(where[3], ctr, record[2])
    add_ref(where[4], ctr, record[3])

    return True

def delete_record(where, indexes):
    for index in indexes:
        where[0][index] = None
        