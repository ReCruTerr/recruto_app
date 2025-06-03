from fastapi import FastAPI 

app = FastAPI() 

@app.get('/main') 
async def main_page(name:str = 'Recruto', message:str = 'Давай дружить'): 
    return {"message": f"Hello {name}! {message}"}

