import fastapi
from .DB import engine, Base
from . import model
from .auth import login 
from fastapi.middleware.cors import CORSMiddleware


app = fastapi.FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create all tables
model.Base.metadata.create_all(bind=engine)



app.include_router(login.router)



# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="[IP_ADDRESS]", port=8000)