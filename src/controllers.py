from fastapi import APIRouter
from starlette.status import HTTP_200_OK

from dtos import TestDTO


voting_router = APIRouter(prefix='/voting', tags=["Voting"])


@voting_router.post("/", status_code=HTTP_200_OK)
async def test(dto: TestDTO):
    print(dto.test)
