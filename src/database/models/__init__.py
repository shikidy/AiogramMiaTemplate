from __future__ import annotations

import enum
from datetime import datetime
from typing import List, Set

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Identity, DateTime, Double, Enum
from sqlalchemy.orm import relationship, Mapped

from src.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

