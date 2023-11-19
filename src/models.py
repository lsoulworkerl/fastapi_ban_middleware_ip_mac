from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, mapped_column


Base = declarative_base()


class UserIP(Base):
    __tablename__ = "user_ip"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(20), nullable=False)


class UserCookie(Base):
    __tablename__ = "user_cookie"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cookie = Column(String(20), nullable=False)


class VoteIP(Base):
    __tablename__ = "vote_ip"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vote = Column(Boolean)
    user_ip_id = mapped_column(ForeignKey("user_ip.id"), unique=True)

    user_ip = relationship('UserIP', back_populates='vote_ip')


class VoteCookie(Base):
    __tablename__ = "vote_cookie"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vote = Column(Boolean)
    user_cookie_id = mapped_column(ForeignKey("user_cookie.id"), unique=True)

    user_cookie = relationship('UserCookie', back_populates='vote_cookie')


class VoteCookieIP(Base):
    __tablename__ = "vote_cookie_ip"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vote = Column(Boolean)
    user_ip_id = mapped_column(ForeignKey("user_ip.id"), unique=True)
    user_cookie_id = mapped_column(ForeignKey("user_cookie.id"), unique=True)

    user_ip = relationship('UserIP', back_populates='vote_ip')
    user_cookie = relationship('UserCookie', back_populates='vote_cookie')


UserIP.votes_ip = relationship('VoteIP', back_populates='user_ip')
UserIP.votes = relationship('VoteCookieIP', back_populates='user_ip')
UserCookie.votes_cookie = relationship('VoteIP', back_populates='user_cookie')
UserCookie.votes = relationship('VoteCookieIP', back_populates='user_cookie')
