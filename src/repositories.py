from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from session import sync_db_session
from models import UserIP, UserCookie, VoteIP, VoteCookie, VoteCookieIP
from exceptions import AlreadyExistError


class UserIPRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user_ip(self, ip: str):
        new_user_ip = UserIP(ip=ip)
        self.session.add(new_user_ip)
        self.session.commit()

    def get_user_id_by_ip(self, ip: str):
        user_ip_record = self.session.query(UserIP).filter_by(ip=ip).first()
        return user_ip_record.id if user_ip_record else None


class UserCookieRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user_cookie(self, cookie: str):
        new_user_cookie = UserCookie(cookie=cookie)
        self.session.add(new_user_cookie)
        self.session.commit()

    def get_user_id_by_cookie(self, cookie: str):
        user_cookie_record = self.session.query(
            UserCookie,
        ).filter_by(
            cookie=cookie,
        ).first()
        return user_cookie_record.id if user_cookie_record else None


class VoteIPRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_vote_ip(self, vote: bool, user_ip_id: int):
        try:
            new_vote_ip = VoteIP(vote=vote, user_ip_id=user_ip_id)
            self.session.add(new_vote_ip)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise AlreadyExistError("VoteIP already exist")


class VoteCookieRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_vote_ip(self, vote: bool, user_cookie_id: int):
        try:
            new_vote_ip = VoteCookie(vote=vote, user_ip_id=user_cookie_id)
            self.session.add(new_vote_ip)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise AlreadyExistError("VoteCookie already exist")


class VoteCookieIPRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_vote_ip(self, vote: bool, user_ip_id: int, user_cookie_id: int):
        try:
            new_vote_ip = VoteCookieIP(
                vote=vote,
                user_ip_id=user_ip_id,
                user_cookie_id=user_cookie_id,
            )
            self.session.add(new_vote_ip)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise AlreadyExistError("VoteCookieIP already exist")


vote_ip_repository = VoteIPRepository(
    sync_db_session.get_session()
)
vote_cookie_repository = VoteCookieRepository(
    sync_db_session.get_session()
)
vote_cookie_ip_repository = VoteCookieIPRepository(
    sync_db_session.get_session()
)

user_ip_repository = UserIPRepository(
    sync_db_session.get_session()
)
user_cookie_repository = UserCookieRepository(
    sync_db_session.get_session()
)
