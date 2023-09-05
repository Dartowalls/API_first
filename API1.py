# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Goodbye World >:)"}

#()

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def root():
#   return "This is the main endpoint of this API"

# @app.get("/names/{name}")
# def read_name(name):
#   return {"name":name,"message":f"Hello, my name is {name}"}

# @app.get("/items/{id}")
# def read_items(id):
#   return {"id":id}

#()


# from fastapi import FastAPI

# app = FastAPI()

# df = {
#     1: {"name": "Hana", "age": 10},
#     2: {"name": "Rifdah", "age": 18}
# }

# @app.get('/data')
# def read_data():
#     return df

# @app.put("/items/{item_id}")
# def update_item(item_id: int, update_data: dict):
#     df[item_id].update(update_data)
#     return {"message": f"Item with ID {item_id} has been updated successfully."}


# from fastapi import FastAPI

# app = FastAPI()

# data = []

# @app.get('/')
# def cart():
#     if len(data)==0:
#         return "There are no items in your cart"
#     else:
#         return data

# @app.post('/input_data/')
# def add_cart(added_item:dict):
#     id = len(data) + 1
#     added_item['id'] = id
#     data.append(added_item)
#     return added_item

# from fastapi import FastAPI

# app = FastAPI()

# df = {
#     1: {"name": "Hana", "age": 10},
#     2: {"name": "Rifdah", "age": 18},
#     3: {"name": "Sakinah", "age": 27}
# }

# @app.get('/data')
# def read_data():
#     return df

# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     df.pop(item_id)
#     return {"message": f"Item with ID {item_id} has been deleted successfully."}

from fastapi import FastAPI, HTTPException, Header

app = FastAPI()

API_KEY = "phase0h8"

data = {"name":"shopping cart",
        "columns":["prod_name","price","num_items"],
        "items":{}}

@app.get("/")
def root():
    return {"message":"Welcome to Toko H8 Shopping Cart! There are some features that you can explore",
            "menu":{1:"See shopping cart (/data)",
                    2:"Add item (/add) - You may need request",
                    3:"Edit shopping cart (/edit/id)",
                    4:"Delete item from shopping cart (/del/id)"}}

@app.get("/cart")
def show():
    return data

@app.post("/add")
def add_item(added_item:dict, api_key: str = Header(None)):
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key. You are not allowed to add data!")
    else:
        id = len(data["items"].keys())+1
        data["items"][id] = added_item
        return f"Item successfully added into your cart with ID {id}"

@app.put("/edit/{id}")
def update_cart(id:int,updated_cart:dict, api_key: str = Header(None)):
    if id not in data['items'].keys():
        raise HTTPException(status_code=404, detail=f"Item with ID {id} not found")
    else:
        if api_key is None or api_key != API_KEY:
            raise HTTPException(status_code=401, detail="Invalid API Key. You are not allowed to edit data!")
        else:
            data["items"][id].update(updated_cart)
            return {"message": f"Item with ID {id} has been updated successfully."}

@app.delete("/del/{id}")
def remove_row(id:int, api_key: str = Header(None)):
    if id not in data['items'].keys():
        raise HTTPException(status_code=404, detail=f"Item with ID {id} not found")
    else:
        if api_key is None or api_key != API_KEY:
            raise HTTPException(status_code=401, detail="Invalid API Key. You are not allowed to delete data!")
        else:
            data["items"].pop(id)
            return {"message": f"Item with ID {id} has been deleted successfully."}