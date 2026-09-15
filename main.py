from fastapi import FastAPI

from dtos import ProductDTO

app = FastAPI()
from mockData import products


@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/products")
def get_products():
    return products

## Path Params

@app.get("/product/{product_id}")
def get_product(product_id: int):

    ## if product avilable with id ,return produvt, else retiurn error massage


    product = None
    for product in products:
        if product.get("id")== product_id:
            return product

    return {"error": "Product not found"}


## Query Params

@app.get("/greet")
def greet_user(name:str, age:int):
    return {
        "greet": f"Hello {name},what is your age?{age}"
    } 




## different type of HTTPS methods

@app.post("/create_product")
def create_product(product_data: ProductDTO):
    
    product_data = product_data.model_dump()
    ##print(product_data)
    products.append(product_data)






@app.put("/update_product/{product_id}")

def update_product(product_data: ProductDTO,product_id:int):
    for index, product in enumerate(products):
        # print(oneProduct)
        if product.get("id")== product_id:
         products[index] = product_data
         return{"status": "Product updated successfully...", "product": product_data}
    
    return {"error": "Product not found"}













## pydantic = it is used to validate data and create DTOs (Data Transfer Objects) for request and response models. It helps ensure that the data being sent and received adheres to the expected structure and types.







##POSTMAN


##How to call defferent type of HTTP methods - GET, POST, PUT, DELETE



##how to validate data. - DTOS.(Data Transfer Objects)
