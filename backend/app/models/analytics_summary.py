from datetime import datetime
from sqlalchemy import Float, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class AnalyticsSummary(Base):
    """
    AnalyticsSummary model storing aggregate scores, indicators,
    and business recommendation outputs.
    """
    __tablename__ = "analytics_summaries"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE"), 
        index=True, 
        nullable=False
    )
    csi_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    hype_index: Mapped[float | None] = mapped_column(Float, nullable=True)
    risk_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    trend_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    recommendation: Mapped[str | None] = mapped_column(Text, nullable=True)
    calculated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now(), 
        nullable=False
    )
