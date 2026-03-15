from datetime import datetime

from database import Base
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Ticker(Base):
    __tablename__: str = "tickers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    symbol: Mapped[str] = mapped_column(String, unique=True, index=True)
    name: Mapped[str | None] = mapped_column(String, nullable=True)
    asset_type: Mapped[str | None] = mapped_column(String, nullable=True)
    is_owned: Mapped[bool] = mapped_column(Boolean, default=False)

    # Using standard 'list' instead of typing.List
    notes: Mapped[list["Note"]] = relationship(
        back_populates="ticker", cascade="all, delete-orphan"
    )


class Note(Base):
    __tablename__: str = "notes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    content: Mapped[str] = mapped_column(Text)

    # Using func.now() lets the database handle the UTC timestamp safely
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    ticker_id: Mapped[int] = mapped_column(ForeignKey("tickers.id"))
    ticker: Mapped["Ticker"] = relationship(back_populates="notes")
