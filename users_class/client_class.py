from users_class.users_class import User;
     
class Client (User):
    
    __list_of_products=[];
    __is_admin= False;
    
    
    def __init__(self, card_number, contact_number, is_premium , id_client,*args ,**kwards): ## *args y **kwards para pasaje con clave valor explicito ejemplo name= "leo"
      super().__init__(*args,**kwards);
      self.__card_number=card_number;
      self.__contact_number= contact_number;
      self.__is_premium= is_premium;
      self.__id_client=id_client;
       
    def __str__(self):
      client_data_string= f"numero de tarjeta: {self.__card_number}, id de cliente : {self.__id_client}."
      
      return client_data_string;
    
    def get_card_number(self):
      return self.__card_number;
    
    def set_card_number(self, number):
      self.__card_number= number;
      
    def get_phone(self):
      return self.__contact_number;
    
    def set_phone(self, number):
      self.__contact_number=number;
      
    def get_is_premium(self):
      return self.__is_premium;
    
    def set_is_premium(self):
      self.__is_premium = not self.__is_premium;
      
    def get_id_client(self):
      return self.__id_client;
    
    def add_products(self, product):
      self.__list_of_products.append(product);
    
    def clear_list_products(self):
      self.__list_of_products= [];
    
    def get_list_of_products(self):
      return self.__list_of_products;

