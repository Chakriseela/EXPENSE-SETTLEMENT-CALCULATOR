from fastapi import FastAPI
from routes.auth_routes import router as auth_router
from routes.users_expense_details_routes import router as expense_router


app = FastAPI()
print(auth_router)
print(expense_router)

app.include_router(auth_router)

app.include_router(expense_router)