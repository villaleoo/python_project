import json

def run_form ():
    finish_registration= 'si';
    cancel_registration='cancelar';
    #si se quisiera mostrar todos los usuarios que se crearon con exito al finalizar el programa, deberia crar un diccionario aqui y agregar cada nuevo usuario a este en la linea 24. al salir del while printear este diccionario que contiene cada nuevo usuario creado. o con load json
    while(finish_registration == 'si'):
        registration_form= True; #esto se utiliza para que el usuario pueda cancelar el registro cuando lo desee y se presume verdadero por estar activamente 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000registrandose
        try:
            new_user={
                'nombre': input("Ingrese nombre de usuario: ").strip().lower(),
                'email': input("Ingrese mail de registro: ").strip().lower(),
                'contrasenia':input("Ingrese contrasenia: ").strip().lower(),
            }
            
            while((verification_empty_dictionary(new_user) != False) and registration_form): # Esto se ejecuta mientras la funcion que verifica que no haya campos vacios arroje algo distinto a falso y la variable que indica las ganas del usuario de continuar logueandose continue en verdadero
                verification_dictionary= verification_empty_dictionary(new_user); #almacena el valor del campo vacio
    
                new_user[f'{verification_dictionary}'] = input(f'Por favor re-ingrese su {verification_dictionary} o introduzca {cancel_registration} para salir: ').strip().lower() #printea que reingrese cada campo que encuentra vacio o introduzca cancelar para salir
                
                if(new_user[f'{verification_dictionary}'] == cancel_registration): #si se introduce cancelar en algun campo vacio, indica que el usuario no quiere continuar logueandose, por lo que la variable creada para ello pasa a falso
                    registration_form=False;

            while((email_not_include_symbol(new_user['email'])) and registration_form): #esto se ejecuta si es verdadero que el email no contiene @ y terminacion .com Y si el usuario continua con las ganas de loguearse en true
                new_user['email']=input(f"Por favor ingrese un email valido(con @ y terminacion .com) o introduzca {cancel_registration} para salir: ").strip().lower(); 
                
                if(new_user['email'] == cancel_registration): #se ejecuta si el usuario no verifica el mail y quiere cancelar el logueo 
                   registration_form = False
                
        except:
            print("Dato/s ingresado/s incorrectamente.")
        else:
            if(registration_form): #si el usuario logro completar los campos y verificar el mail, continuó con las ganas de registrarse en true y llego al final del programa donde se guarda el usuario en la BBDD
                with open('./data/users_database.json', 'a') as create_user: #toma el usuario creado correctamente y lo agrega(apenda('a'),no sobreescribe) a la BBDD
                    json.dump(new_user, create_user, indent=4)
                    
                print(f"\n\t¡Usuario creado con exito!\n");
                print_dictionary_users(new_user); #muestra por pantalla el usuario creado
                     
        finish_registration=input(f"Desea crear otro usuario? Ingrese {finish_registration} para continuar: ").strip().lower()
        if(finish_registration != 'si'):  
            print("Gracias por visitarnos.")
            
            
            
def verification_empty_dictionary(dictionary): #verifica si hay campos vacios en un diccionario de usuarios. si encuentra un campo vacio, retorna la key del campo, si no, retorna false
    input_is_empty= False;  
    for key in dictionary:
        if (dictionary[key] == ''):
            input_is_empty=key;
    return input_is_empty;
            
            
def print_dictionary_users(dictionary):   #muestra por pantalla los datos de un usuario con estilo.
    for item, value in dictionary.items():
        if(item == 'nombre'):
            print(f"{item} usuario: {value}") 
        else:
            print(f"{item}: {value}")
            
        
def email_not_include_symbol(mail_of_user): #retorna TRUE si efectivamente el email NO contiene @ y .com ; FALSE si los contiene
    not_contains_symbol=True; #se presume que el email NO contiene simbolo @ y terminacion .com, hasta que el while encuentre lo contrario.
    lenght_email=len(mail_of_user);
    
    while((not_contains_symbol) and (lenght_email > 0)): #se sale de este loop cuando [se encuentra una arroba Y hay terminacion .com]->(esto haria not_cotains_symbol FALSE) Ó cuando se recorran todos los caracteres del email sin exito de encontrar arroba(@)
        list_email= list(mail_of_user);
        for value,first_condition in enumerate(list_email):
            if(first_condition == '@'): #recorre la lista hecha con el mail del usuario y si encuentra un arroba, procede a verificar si encuentra un punto '.'
                for second_condition in list_email[value:-2]: #recorre desde donde encuentra un arroba hasta 3 caracteres antes de terminar el mail,asegurando que luego del punto haya por lo menos 2 caracteres (ejemplo terminaciones .es) incrementando value se podria maximizar la distancia entre donde encuentra el @ y donde deberia haber un punto.
                    if(second_condition == '.'):
                        not_contains_symbol= False; #solo si "encuentra la terminacion .com" cambia el valor de la variable not_contains_symbol, sino el mail NO verifica como valido 
                        
            lenght_email-= 1;  
               
    return not_contains_symbol 


run_form()
    
        

