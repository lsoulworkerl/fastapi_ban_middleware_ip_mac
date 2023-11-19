from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class UserIP(Base):
    __tablename__ = "user_ip"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(20), nullable=False, unique=True)


class UserCookie(Base):
    __tablename__ = "user_cookie"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cookie = Column(String(20), nullable=False, unique=True)


class VoteIP(Base):
    __tablename__ = "vote_ip"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vote = Column(Boolean)
    user_ip_id = Column(ForeignKey("user_ip.id"), unique=True)

    user_ip = relationship('UserIP', back_populates='votes_ip')


class VoteCookie(Base):
    __tablename__ = "vote_cookie"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vote = Column(Boolean)
    user_cookie_id = Column(ForeignKey("user_cookie.id"), unique=True)

    user_cookie = relationship('UserCookie', back_populates='votes_cookie')


class VoteCookieIP(Base):
    __tablename__ = "vote_cookie_ip"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vote = Column(Boolean)
    user_ip_id = Column(ForeignKey("user_ip.id"), unique=True)
    user_cookie_id = Column(ForeignKey("user_cookie.id"), unique=True)

    user_ip = relationship('UserIP', back_populates='user_votes')
    user_cookie = relationship('UserCookie', back_populates='votes')


UserIP.votes_ip = relationship(
    'VoteIP',
    back_populates='user_ip',
)
UserIP.user_votes = relationship(
    'VoteCookieIP',
    back_populates='user_ip',
)
UserCookie.votes_cookie = relationship(
    'VoteCookie',
    back_populates='user_cookie',
)
UserCookie.votes = relationship(
    'VoteCookieIP',
    back_populates='user_cookie',
)
