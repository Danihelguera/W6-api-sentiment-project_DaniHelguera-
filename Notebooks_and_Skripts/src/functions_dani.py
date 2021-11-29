

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
        print(f"Ya existe el usuario: '{string}' y tiene el ID {ID}")
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
        print(f"Ya existe el producto: '{string[:25]}...' y tiene el ID {ID}")
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
    mark          = int(fila["rating"][0])
    texto         = fila["rating_text"][0]
    title         = fila["rating_title"][0]
    date_         = fila["date"][0]
    recommended   = int(fila["recommended"][0])
    ID_p          = insert_product(fila["Product_name"][0] )
    ID_u          = insert_user(fila["username"][0] )

    exists_r,ID_r = check("rating", texto )
            
    if exists_r:
        print(f"Ya existe el rating '{texto[:20]}...' y tiene el ID {ID_r}")
    else:
        engine.execute(f"""
        INSERT INTO ratings (mark, texto, title, date_, recommended, ID_product, ID_user) 
        VALUES ({mark},'{texto}','{title}','{date_}','{recommended}','{ID_p}','{ID_u}');
        """)
        exits_r,ID_r = check("rating", texto )
        print(f"Nuevo rating insertado en BBDD: '{texto[:20]}...' y tiene el ID {ID_r}")
    
    return ID_r
