from datetime import datetime
from enum import Enum

from database import Base
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship


class TradeType(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
    DIVIDEND = "DIVIDEND"


class Ticker(Base):
    __tablename__: str = "tickers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    symbol: Mapped[str] = mapped_column(String, unique=True, index=True)
    name: Mapped[str | None] = mapped_column(String, nullable=True)
    asset_type: Mapped[str | None] = mapped_column(String, nullable=True)
    is_owned: Mapped[bool] = mapped_column(Boolean, default=False)
    average_buy_price: Mapped[float | None] = mapped_column(default=None)
    quantity: Mapped[float | None] = mapped_column(default=None)

    # Added the cascade rule so transactions are deleted if the ticker is deleted
    transactions: Mapped[list["Transaction"]] = relationship(
        back_populates="ticker", cascade="all, delete-orphan"
    )

    notes: Mapped[list["Note"]] = relationship(
        back_populates="ticker", cascade="all, delete-orphan"
    )


class Transaction(Base):
    __tablename__: str = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    transaction_type: Mapped[TradeType] = mapped_column(default=TradeType.BUY)

    transaction_total_price: Mapped[float | None] = mapped_column(default=None)
    transaction_unit_quantity: Mapped[float | None] = mapped_column(default=None)
    transaction_unit_price: Mapped[float | None] = mapped_column(default=None)
    transaction_date: Mapped[datetime | None] = mapped_column(default=None)

    ticker_id: Mapped[int] = mapped_column(ForeignKey("tickers.id"))
    ticker: Mapped["Ticker"] = relationship(back_populates="transactions")


class Note(Base):
    __tablename__: str = "notes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    content: Mapped[str] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    ticker_id: Mapped[int] = mapped_column(ForeignKey("tickers.id"))
    ticker: Mapped["Ticker"] = relationship(back_populates="notes")
