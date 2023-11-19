from fastapi import APIRouter

from controllers import voting_router


def get_apps_router():
    router = APIRouter()
    router.include_router(voting_router)
    return router
