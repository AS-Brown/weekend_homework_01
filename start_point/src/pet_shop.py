# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(list_petshop):
    return list_petshop["name"]

def get_total_cash(list_petshop):
    return list_petshop["admin"]["total_cash"]

def add_or_remove_cash(list_petshop, num_one): 
    list_petshop["admin"]["total_cash"] += num_one

def get_pets_sold(list_petshop):
    return list_petshop["admin"]["pets_sold"]

def increase_pets_sold(list_petshop, num_one):
    list_petshop["admin"]["pets_sold"] += num_one

def get_stock_count(list_petshop):
    return len(list_petshop["pets"])

def get_pets_by_breed(list_petshop, breed):
    pets = []
    for animal in list_petshop["pets"]:
        if animal["breed"] == breed:
            pets.append(animal)
    return pets

def find_pet_by_name(list_petshop, animal_name):
    for animal in list_petshop["pets"]:
        if animal["name"] == animal_name:
            return animal
        
def remove_pet_by_name(list_petshop, animal_name):
            list_petshop["pets"].remove(find_pet_by_name(list_petshop, animal_name))
            
def add_pet_to_stock(list_petshop, list_new_animal):
    list_petshop["pets"].append(list_new_animal)

def get_customer_cash(list_customers):
    return list_customers["cash"]

def remove_customer_cash(list_customers, price):
    list_customers["cash"] -= price

def get_customer_pet_count(list_customers):
    return len(list_customers["pets"])

def add_pet_to_customer(list_customers, list_new_pet):
    list_customers["pets"].append(list_new_pet)

def customer_can_afford_pet(list_customers, list_new_pet):
    if list_customers["cash"] >= list_new_pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(list_petshop, list_new_pet, list_customer):
    if list_new_pet != None and customer_can_afford_pet(list_customer, list_new_pet) == True:
        add_pet_to_customer(list_customer, list_new_pet)
        increase_pets_sold(list_petshop, get_customer_pet_count(list_customer))
        remove_customer_cash(list_customer, list_new_pet["price"])
        add_or_remove_cash(list_petshop, list_new_pet["price"])
        remove_pet_by_name(list_petshop, list_new_pet["name"])
    else:
        pass


