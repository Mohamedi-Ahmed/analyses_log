def read_files(filename) :
    
    txt = []
    f = open(filename, "r")
    txt = f.read().splitlines()
    f.close()
    return txt

def create_file(data, filename) :
    with open(filename, "w") as f:
        for row in data :
            f.write(row+"\n")
    return

def create_file_from_dict(data, filename) :
    with open(filename, "w") as f:
        f.write("Username : number_of_connexions_with_suspicious_ip\n\n")
        for row in data.items() :
            f.write(str(row[0]) + " : " + str(row[1]) + "\n")
    return

def retrieve_users(data) :
    
    users = []
    for entry in data :
        users.append(entry.split(";")[1])
    return users

def get_user_from_connexion_hours(data) :
    
    dict_hackers = {}
    
    for entry in data :
        date = entry.split(";")[-1]
        full_hour = date.split(" ")[-1]
        hour = full_hour.split(":")[0]
        if int(hour) < 8 or int(hour) > 19 :
            dict_hackers[entry.split(";")[1]] = entry.split(";")[0]    
    return dict_hackers

def get_suspect_from_data(data_connexions, list_ip) :
    
    dict_suspect = dict()
    for user in data_connexions :
        user_ip =  user.split(";")[0]
        if user_ip in list_ip :
            user_name =  user.split(";")[1]
            if user_name in dict_suspect.keys() :
                dict_suspect[user_name] += 1
            else :
                dict_suspect[user_name] = 1
    return dict_suspect

namefile = "connexion.log"
pathfile = "./"

full_filepath = pathfile + namefile

myConnexions = read_files(full_filepath)
#print(myConnexions[1].split(";"))
myUsers = retrieve_users(myConnexions)
#create_file(myUsers,"./utilisateurs.txt")
myHackers = get_user_from_connexion_hours(myConnexions)
print(myHackers)

myDangerousIps = read_files("./warning.txt")
print(myDangerousIps)

mySuspects = get_suspect_from_data(myConnexions, myDangerousIps)
#print(mySuspects)
#create_file_from_dict(mySuspects, "./suspect.txt")

