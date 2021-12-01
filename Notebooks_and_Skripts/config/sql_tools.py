from config.configuration import engine
import pandas as pd

def users_list():
    """Esta función es para hacer una query a la BBDD en SQL que nos devuelve todos los usarios registrados
    Returns:
        [list]: [usuarios registrados]
    """
    query = list(engine.execute("SELECT username FROM amazon_rating.user_names;"))
    lista =  [{"user": element[0]} for element in query]
    return lista


def products_list():
    """Esta función es para hacer una query a la BBDD en SQL que nos devuelve todos los productos registrados
    Returns:
        [list]: [productos registrados]
    """
    query = list(engine.execute("SELECT productname FROM amazon_rating.product_names;"))
    lista =  [{"product": element[0]} for element in query]
    return lista

def ratings_by_user(user):
    """Esta función es para hacer una query a la BBDD en SQL que nos devuelve todos los ratings hechos por el usuario "user"
    Returns:
        [list]: [lista de diccionarios, cada elemento es un rating hecho por el usuario "user"]
    """
    _,ID_user = check("username",user)
    query = list(engine.execute(f"SELECT * FROM amazon_rating.ratings WHERE ID_user = {ID_user};"))
    lista = [  {"rating"       : element["mark"]              , 
                "rating_text"  : element["texto"]             ,
                "rating_title" : element["title"]             ,
                "date"         : element["date_"]             ,
                "recommended"  : bool(element["recommended"]) ,
                "username"     : user                         
                }     for element in query ]
    return lista

def ratings_by_product(product) :
    """Esta función es para hacer una query a la BBDD en SQL que nos devuelve todos los ratings de un producto "product"
    Returns:
        [list]: [lista de diccionarios, cada elemento es un rating del producto "product"]
    """
    _,ID_product = check("product",product)
    query = list(engine.execute(f"SELECT * FROM amazon_rating.ratings WHERE ID_product = {ID_product};"))
    lista = [  {"rating"       : element["mark"]              , 
                "rating_text"  : element["texto"]             ,
                "rating_title" : element["title"]             ,
                "recommended"  : bool(element["recommended"]) ,
                "Product_name" : product                      
                }       for element in query ]
    return lista


def check(que,string):
    """
    Función parametrizada que comprueba en cada tabla si existe el user, producto o rating.
    Si existe, devuelve una lista con True y el ID dentro de la tabla
    Si no exite, devuelve una lista con False y None.
    """
    if que == "username":
        query = list(engine.execute(f"SELECT username FROM user_names WHERE username = '{string}'"))
        if len(query) > 0:
            return [True,list(engine.execute(f"SELECT ID FROM user_names WHERE username ='{string}';"))[0][0]]
        else:
            return [False,None]
        
    elif que == "product":
        query = list(engine.execute(f"SELECT productname FROM product_names WHERE productname = '{string}'"))
        if len(query) > 0:
            return [True,list(engine.execute(f"SELECT ID FROM product_names WHERE productname = '{string}'"))[0][0]]
        else:
            return [False,None]
        
    elif que == "rating":
        query = list(engine.execute(f"SELECT texto FROM ratings WHERE texto = '{string}'"))
        if len(query) > 0:
            return [True,list(engine.execute(f"SELECT ID FROM ratings WHERE texto = '{string}'"))[0][0]]
        else:
            return [False,None]
        
def insert_user(string):
    """    
    Primero se comprueba si ya existe el usuario.
    Si no existe se introduce.
    En ambos casos la función informa por pantalla de lo que hace y devuelve el ID del usuario
    """
    exists,ID = check("username", string)
    if exists:
        #print(f"Ya existe el usuario: '{string}' y tiene el ID {ID}")
        pass
    else:
        engine.execute(f"INSERT INTO user_names (username) VALUES ('{string}');")
        exists,ID = check("username", string)
        print(f"Nuevo usuario insertado en BBDD: '{string}' y se le ha asignado el ID {ID}")
    
    return ID

def insert_product(string):
    """
    Primero comprobamos si ya existe el producto.
    Si no existe se introduce.
    En ambos casos la función informa por pantalla de lo que hace y devuelve el ID del producto
    """
    exists,ID = check("product", string)
    if exists:
        #print(f"Ya existe el producto: '{string[:25]}...' y tiene el ID {ID}")
        pass
    else:
        engine.execute(f"INSERT INTO product_names (productname) VALUES ('{string}');")
        exists,ID = check("product", string)
        print(f"Nuevo producto insertado en BBDD: '{string[:25]}...' y se le ha asignado el ID {ID}")
    
    return ID

def insert_rating(fila):
    """
    Esta función mete los comentarios que se le pasan fila por fila de un dataframe en la BBDD SQL.
    Primero llama a la función insert_user con el username del rating incluido en la "fila"
    Segungo llama a la función insert_product con el product del rating incluido en la "fila"
    Tercero comprueba si existe el rating en dicha tabla
        Si ya existe, informa por pantalla y la función devuelve el ID del rating en BBDD de SQL
        Si no existe, lo introduce, informa por pantalla y devuelve el ID del rating en BBDD de SQL
    """
    mark          = int(fila["rating"])
    texto         = fila["rating_text"]
    title         = fila["rating_title"]
    date_         = fila["date"]
    recommended   = int(fila["recommended"])
    ID_p          = insert_product(fila["Product_name"])
    ID_u          = insert_user(fila["username"])

    exists_r,ID_r = check("rating", texto )
            
    if exists_r:
        #print(f"Ya existe el rating '{texto[:20]}...' y tiene el ID {ID_r}")
        pass
    else:
        engine.execute(f"""
        INSERT INTO ratings (mark, texto, title, date_, recommended, ID_product, ID_user) 
        VALUES ({mark},'{texto}','{title}','{date_}','{recommended}','{ID_p}','{ID_u}');
        """)
        exits_r,ID_r = check("rating", texto )
        #print(f"Nuevo rating insertado en BBDD: '{texto[:20]}...' y tiene el ID {ID_r}")
    
    return ID_r
