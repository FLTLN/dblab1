def add_ref(indexes, index, ref):
    if ref not in indexes:
        indexes[ref] = []
        indexes[ref].append(index)
    else:
        indexes[ref].append(index)


def load(path):
    ip_index   = {}
    usr_index  = {}
    hash_index = {}
    perm_index = {}
    ctr = 0
    data = []
    all_indexes = []
    with open(path, "r") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.split(",")
            tmp = []
            for item in line:
                tmp.append(item)
            data.append(tmp)
            ip_index[tmp[0]] = [ctr]
            add_ref(usr_index, ctr, tmp[1])
            add_ref(hash_index, ctr, tmp[2])
            add_ref(perm_index, ctr, tmp[3])
            all_indexes.append(ctr)
            ctr += 1

    return (data, ip_index, usr_index, hash_index, perm_index, all_indexes)

def save(what, path):
    data = what[0]
    with open(path, "w") as file:
        for record in data:
            if not record == None: 
                file.write("{},{},{},{}\n".format(record[0],record[1],record[2],record[3]))

def export(what, path):
    data = what[0]
    with open(path, "w") as file:
        for record in data:
            if not record == None: 
                file.write("{};{};{};{}\n".format(record[0],record[1],record[2],record[3]))
