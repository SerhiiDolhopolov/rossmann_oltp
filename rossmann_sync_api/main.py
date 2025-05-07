import uvicorn
from fastapi import FastAPI

from rossmann_sync_api.api.employees import router as employees_router
from rossmann_sync_api.api.categories import router as categories_router
from rossmann_sync_api.api.products import router as products_router
from rossmann_sync_api.api.shops import router as shops_router


app = FastAPI()
app.include_router(employees_router)
app.include_router(categories_router)
app.include_router(products_router)
app.include_router(shops_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)