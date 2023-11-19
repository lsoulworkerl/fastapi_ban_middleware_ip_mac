from fastapi import APIRouter, Request, HTTPException
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from dtos import VoteDTO
from repositories import (
    vote_ip_repository,
    vote_cookie_repository,
    vote_cookie_ip_repository,
    user_ip_repository,
    user_cookie_repository,
)
from exceptions import AlreadyExistError


voting_router = APIRouter(prefix='/voting', tags=["Voting"])


@voting_router.post("/vote_ip", status_code=HTTP_200_OK)
async def vote_ip(dto: VoteDTO, request: Request):
    user_ip = request.scope.get('client')[0]

    user_ip_id = user_ip_repository.get_user_id_by_ip(ip=user_ip)

    try:
        vote_ip_repository.create_vote_ip(vote=dto.vote, user_ip_id=user_ip_id)
    except AlreadyExistError:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="You already voted",
        )


@voting_router.post("/vote_cookie", status_code=HTTP_200_OK)
async def vote_cookie(dto: VoteDTO, request: Request):
    user_cookie = request.cookies.get("evercookie")

    user_cookie_id = user_cookie_repository.get_user_id_by_cookie(
        cookie=user_cookie,
    )

    try:
        vote_cookie_repository.create_vote_cookie(
            vote=dto.vote,
            user_cookie_id=user_cookie_id,
        )
    except AlreadyExistError:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="You already voted",
        )


@voting_router.post("/vote_cookie_ip", status_code=HTTP_200_OK)
async def vote_cookie_ip(dto: VoteDTO, request: Request):
    user_ip = request.scope.get('client')[0]
    user_cookie = request.cookies.get("evercookie")

    user_ip_id = user_ip_repository.get_user_id_by_ip(
        ip=user_ip,
    )
    user_cookie_id = user_cookie_repository.get_user_id_by_cookie(
        cookie=user_cookie,
    )

    try:
        vote_cookie_ip_repository.create_vote_cookie_ip(
            vote=dto.vote,
            user_ip_id=user_ip_id,
            user_cookie_id=user_cookie_id,
        )
    except AlreadyExistError:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="You already voted",
        )
