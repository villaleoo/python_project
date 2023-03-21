import json;

def append_users_database(URL, new_user):
    with open(URL, 'a') as create_user: #toma el usuario creado correctamente y lo agrega(apenda('a'),no sobreescribe) a la BBDD
        json.dump(new_user, create_user, indent=4);

def get_users_database():
    print("sarasa")