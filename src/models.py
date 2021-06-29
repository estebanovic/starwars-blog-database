import os
import sys
import json
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    results = Column()

class Vehicles(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    results = Column()

class Starships(Base):
    __tablename__ = 'starships'

    id = Column(Integer, primary_key=True)
    results = Column()

class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    results = Column()

class Species(Base):
    __tablename__ = 'species'

    id = Column(Integer, primary_key=True)
    results = Column()
    
class ReadList(Base):
    __tablename__ = 'read_list'

    id = Column(Integer, primary_key=True)
    results = Column()

class Info(Base):
    __tablename__ = 'info'

    id = Column(Integer, primary_key=True)
    results = Column()

class Store(Base):
    __tablename__ = 'store'

    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey('people.id'))
    People = relationship(People)
    starships_id = Column(Integer, ForeignKey('starships.id'))
    Starships = relationship(Starships)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    Planets = relationship(Planets)
    species_id = Column(Integer, ForeignKey('species.id'))
    Species = relationship(Species)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    Vehicles = relationship(Vehicles)
    read_list_id = Column(Integer, ForeignKey('read_list.id'))
    ReadList = relationship(ReadList)
    info_id = Column(Integer, ForeignKey('info.id'))
    Info = relationship(Info)

class Actions(Base):
    __tablename__ = 'actions'

    id = Column(Integer, primary_key=True)
    get_people = Column()
    get_plantes = Column()
    get_vehicles = Column()
    get_species = Column()
    get_starships = Column()
    set_readlist = Column()
    remove_reatlist = Column()
    get_info = Column()
    clear = Column()

class Flux(Base):
    __tablename__ = 'flux'

    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey('store.id'))
    Store = relationship(Store)
    actions_id = Column(Integer, ForeignKey('actions.id'))
    Actions = relationship(Actions)


class AppContext(Base):
    __tablename__ = 'app_context'

    id = Column(Integer, primary_key=True)
    flux_id = Column(Integer, ForeignKey('flux.id'))
    Flux = relationship(Flux)


class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    app_context_id = Column(Integer, ForeignKey('app_context.id'))
    AppContext = relationship(AppContext)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')