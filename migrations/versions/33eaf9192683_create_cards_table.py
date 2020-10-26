from alembic import op
import sqlalchemy as sa

revision = '33eaf9192683'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
      'cards',
      sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
      sqlalchemy.Column("title", sqlalchemy.String),
      sqlalchemy.Column("type", sqlalchemy.String),
      sqlalchemy.Column("position", sqlalchemy.Integer),
      sqlalchemy.Column("created_at", sqlalchemy.DateTime),
      sqlalchemy.Column("updated_at", sqlalchemy.DateTime),
    )

def downgrade():
    op.drop_table('cards')
