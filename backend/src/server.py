from fastapi import APIRouter, FastAPI

from api.cargo import cargo_router
from api.purchase import purchases_router
from api.review import reviews_router
from api.search import search_router
from api.user import users_router


def init_routes(app_: FastAPI):
    api_router = APIRouter()
    api_router.include_router(users_router, prefix='/users')
    api_router.include_router(search_router, prefix='/search')
    api_router.include_router(purchases_router, prefix='/purchases')
    api_router.include_router(reviews_router, prefix='/reviews')
    api_router.include_router(cargo_router, prefix='/cargo')
    app_.include_router(api_router)


def setup_middlewares(app_: FastAPI):
    pass


def setup_events(app_: FastAPI):
    pass


def init_cache(app_: FastAPI):
    pass


def create_app() -> FastAPI:
    app = FastAPI()
    init_routes(app)
    setup_events(app)
    setup_middlewares(app)
    return app


app = create_app()
