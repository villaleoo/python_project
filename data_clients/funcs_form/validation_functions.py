def verification_empty_dictionary(dictionary): #verifica si hay campos vacios en un diccionario de usuario. si encuentra un campo vacio, retorna la key del campo, si no, retorna false
    input_is_empty= False;  
    for key in dictionary:
        if (dictionary[key] == ''):
            input_is_empty=key;
    return input_is_empty;
            
            
def print_dictionary_users(dictionary):   #muestra por pantalla los datos de un usuario con estilo.
    for item, value in dictionary.items():
        if(item == 'nombre'):
            print(f"{item} usuario: {value}"); 
        else:
            print(f"{item}: {value}");
            
        
def email_not_include_symbol(mail_of_user): #esta funcion retorna TRUE si el email no contiene o contiene mas de una @ o si el mail no contiene la terminacion .com/.es ; retorna FALSE si cumple con las condiciones de @ y .com
    not_contains_symbol=True; #se presume que el email NO contiene simbolo @ y terminacion .com hasta que supere las verificaciones
    list_email=(mail_of_user);
    quantity_chars_after_point= 4;
    
    if(quantity_symbols_of_email(mail_of_user) == 1):
        for value,second_condition_validate in enumerate(list_email):
            if(second_condition_validate == '.'): #cuando encuentra un punto en el email, busca verificar si luego de él hay 0 arrobas y si el punto se encuentra a 4 caracteres del final de la longitud del email
                if((quantity_symbols_of_email(mail_of_user[value:]) == 0) and ((len(mail_of_user) - value ) <= quantity_chars_after_point)): #esta condicion obliga al usuario a incluir un mail el cual no haya arrobas luego de que haya un . al final del email con hasta 3 caracteres luego del '.'
                    not_contains_symbol = False;
          
    return not_contains_symbol;


def quantity_symbols_of_email(user_email): #esta funcion recorre el mail del usuario y retorna la cantidad de @ que encuentra (deberia haber solo 1)
    quantity_symbols = 0;
    list_email= list(user_email);
    
    for first_conditon_validate in list_email[1:]:
        if(first_conditon_validate == '@'):
            quantity_symbols+=1;
            
    return quantity_symbols;
