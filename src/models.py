import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

favorite_planets = Table('favorite_planets',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('planet_id', Integer, ForeignKey('planet.id'), primary_key=True)
)

favorite_characters = Table('favorite_characters',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('character_id', Integer, ForeignKey('character.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    favorite_planets = relationship('Planet', secondary=favorite_planets, backref='favorited_by_users')
    favorite_characters = relationship('Character', secondary=favorite_characters, backref='favorited_by_users')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

