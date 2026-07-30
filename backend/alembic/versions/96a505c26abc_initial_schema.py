"""Initial schema

Revision ID: 96a505c26abc
Revises: 
Create Date: 2026-07-30 11:38:15.105786

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96a505c26abc'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Create products table
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('category', sa.String(length=100), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_products_name'), 'products', ['name'], unique=False)
    op.create_index(op.f('ix_products_category'), 'products', ['category'], unique=False)

    # 2. Create customers table
    op.create_table(
        'customers',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('hashed_password', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_customers_email'), 'customers', ['email'], unique=True)

    # 3. Create customer_reviews table
    op.create_table(
        'customer_reviews',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('review_text', sa.Text(), nullable=False),
        sa.Column('rating', sa.Integer(), nullable=False),
        sa.Column('sentiment_score', sa.Float(), nullable=True),
        sa.Column('sentiment_label', sa.String(length=50), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_customer_reviews_product_id'), 'customer_reviews', ['product_id'], unique=False)

    # 4. Create reddit_posts table
    op.create_table(
        'reddit_posts',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('post_id', sa.String(length=50), nullable=False),
        sa.Column('subreddit', sa.String(length=100), nullable=False),
        sa.Column('title', sa.String(length=500), nullable=False),
        sa.Column('selftext', sa.Text(), nullable=True),
        sa.Column('url', sa.String(length=1024), nullable=True),
        sa.Column('score', sa.Integer(), server_default='0', nullable=False),
        sa.Column('sentiment_score', sa.Float(), nullable=True),
        sa.Column('sentiment_label', sa.String(length=50), nullable=True),
        sa.Column('model_used', sa.String(length=100), nullable=True),
        sa.Column('fetched_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reddit_posts_post_id'), 'reddit_posts', ['post_id'], unique=True)
    op.create_index(op.f('ix_reddit_posts_subreddit'), 'reddit_posts', ['subreddit'], unique=False)

    # 5. Create analytics_summaries table
    op.create_table(
        'analytics_summaries',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('csi_score', sa.Float(), nullable=True),
        sa.Column('hype_index', sa.Float(), nullable=True),
        sa.Column('risk_score', sa.Float(), nullable=True),
        sa.Column('trend_score', sa.Float(), nullable=True),
        sa.Column('recommendation', sa.Text(), nullable=True),
        sa.Column('calculated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_analytics_summaries_product_id'), 'analytics_summaries', ['product_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_analytics_summaries_product_id'), table_name='analytics_summaries')
    op.drop_table('analytics_summaries')
    op.drop_index(op.f('ix_reddit_posts_subreddit'), table_name='reddit_posts')
    op.drop_index(op.f('ix_reddit_posts_post_id'), table_name='reddit_posts')
    op.drop_table('reddit_posts')
    op.drop_index(op.f('ix_customer_reviews_product_id'), table_name='customer_reviews')
    op.drop_table('customer_reviews')
    op.drop_index(op.f('ix_customers_email'), table_name='customers')
    op.drop_table('customers')
    op.drop_index(op.f('ix_products_category'), table_name='products')
    op.drop_index(op.f('ix_products_name'), table_name='products')
    op.drop_table('products')

