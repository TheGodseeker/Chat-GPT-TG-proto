import fastapi

from src.settings.const import BASE_URL

app = fastapi.FastAPI()
appv1 = fastapi.FastAPI()

# appv1.include_router(router_recommendation)
# appv1.include_router(router_neuralmodel)

app.mount(BASE_URL, appv1)
