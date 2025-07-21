```python
from fastapi import FastAPI

  

app = FastAPI()


books = [

    {'title': 'Book One', 'author': 'Author One', 'year': 2021},

    {'title': 'Book Two', 'author': 'Author Two', 'year': 2020},

    {'title': 'Book Three', 'author':'Author three' , 'year': 2020},

    {'title': 'Book four', 'author':'Author four' , 'year': 2020},

    {'title': 'Book five', 'author':'Author five' , 'year': 2020},

    {'title': 'Book six', 'author':'Author six' , 'year': 2020}

]

  

@app.get("/name_endpoint")

async def first_api():

    return {"message": "Home Page"}

  

@app.get("/books")

async def get_books():

    return  books
    
```



command to run FastAPI app:

```powershell
uvicorn books:app
```
where books -- is the name of the python file
	app -- is the name of the fastAPI instance



==How is fast API different from Django or Flask?

===WSGI Vs. ASGI what is the diffference?

==FASTAPI testing?

FastAPI works with only python 3.6+

==how to use middleware in FAST API?

its a wrapper function used to take care of the operations to be done before the request is processed and after the request has been processed and before it is sent to the user.


==Middleware operations are synchronous or Asynchronous?

==CORS Middleware error?

==Benefits of using Pydentic?

allows serialization and deserialization of requests

==Co-routines in python?

==what are background tasks?



