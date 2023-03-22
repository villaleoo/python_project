from data_clients.funcs_form.validation_functions import *;
from data_clients.funcs_form.clients_database_functions import append_users_database;
from users_class.client_class import Client;

def execute_form(URL_BBDD):
    print(URL_BBDD)
    registration_form= True; #esto se utiliza para que el usuario pueda cancelar el registro cuando lo desee y se presume verdadero por estar activamente registrandose
    cancel_registration='cancelar';
    opt_selecc=-1
    options_menu= ["ver datos", "cambiar contrasenia", "salir"]
    
   
       
    try:
        new_user={
            'tarjeta': int(input("ingrese su numero de tarjeta: ").strip()),
            'telefono':int(input('ingrese su numero telefonico: ').strip()),
            'premium': False,
            'id': 28, #numero random
            'nombre': input("Ingrese nombre de usuario: ").strip().lower(),
            'email': input("Ingrese mail de registro: ").strip().lower(),
            'contrasenia':input("Ingrese contrasenia: ").strip().lower(),
        };
        
        while((verification_empty_dictionary(new_user) != False) and registration_form): # Esto se ejecuta mientras la funcion que verifica que no haya campos vacios arroje algo distinto a falso y la variable que indica las ganas del usuario de continuar logueandose continue en verdadero
            verification_dictionary= verification_empty_dictionary(new_user); #almacena el valor del campo vacio
    
            new_user[f'{verification_dictionary}'] = input(f'Por favor re-ingrese su {verification_dictionary} o introduzca {cancel_registration} para salir: ').strip().lower(); #printea que reingrese cada campo que encuentra vacio o introduzca cancelar para salir
            
            if(new_user[f'{verification_dictionary}'] == cancel_registration): #si se introduce cancelar en algun campo vacio, indica que el usuario no quiere continuar logueandose, por lo que la variable creada para ello pasa a falso
                registration_form=False;
        while((email_not_include_symbol(new_user['email'])) and registration_form): #esto se ejecuta si es verdadero que el email NO contiene @ y terminacion .com Y si el usuario continua con las ganas de loguearse en true
            new_user['email']=input(f"Por favor ingrese un email valido(con @ y terminacion .com) o introduzca {cancel_registration} para salir: ").strip().lower(); 
            
            if(new_user['email'] == cancel_registration): #se ejecuta si el usuario no verifica el mail y quiere cancelar el logueo 
               registration_form = False;
                
    except:
        print("Dato/s ingresado/s incorrectamente.");
    else:
        if(registration_form): #si el usuario logro completar los campos y verificar el mail, continuó con las ganas de registrarse en true y llego al final del programa donde se guarda el usuario en la BBDD
            append_users_database(URL_BBDD, new_user)
            print(f"\n\t¡Usuario creado con exito!\n");
            print_dictionary_users(new_user); #muestra por pantalla el usuario creado
            new_client= Client(new_user['tarjeta'], new_user['telefono'], new_user['premium'], new_user['id'], new_user['nombre'], new_user['email'], new_user['contrasenia'])
            
            while((opt_selecc < 0) or (opt_selecc >= len(options_menu)) and (opt_selecc != options_menu[-1])):
                print_menu_client(options_menu)
                opt_selecc= int(input("Ingrese la opearacion que desea realizar: "))
            if(opt_selecc == 0):
                print(new_client);
            if(opt_selecc == 1):
                new_client.set_password(input("ingrese nueva contrasenia"))
                print(f"su nueva contrasenia es: {new_client.get_password()}")
    
 
 
 
    
def print_menu_client(options_menu):
    
    for i, value in enumerate(options_menu):
        print(f'{i}.{value}.') 
    
            
                     
 
    
            