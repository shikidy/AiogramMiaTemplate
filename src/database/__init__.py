from .base import session, Base, engine

Base.metadata.create_all(engine)