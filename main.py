from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
    
dataRestaurants = [
    {
        "id": 1, 
        "nama_warung": "Warung Makan Mahal", 
        "deskripsi": "Warung menjual makanan tidak murah", 
        "kategori": "Warung", 
        "lokasi" : 110.1234
    }, 
    {
        "id": 2, 
        "nama_warung": "Restoran Tidak Murah", 
        "deskripsi": "Restoran menyediakan pangan", 
        "kategori": "Restoran", 
        "lokasi" : 140.02138
    }       
]

    

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/restaurants")
def read_restaurants():
    # print(json.dump(datasql))
    return dataRestaurants
    
@app.get("/foods")
def read_foods():
    return {"get all data foods"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}