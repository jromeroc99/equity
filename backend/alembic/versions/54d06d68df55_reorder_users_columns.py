"""reorder_users_columns

Revision ID: 54d06d68df55
Revises: 948e74f6cc18
Create Date: 2026-01-04 17:42:22.365385

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54d06d68df55'
down_revision: Union[str, Sequence[str], None] = '948e74f6cc18'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Reordenar columnas: id primero
    op.execute("ALTER TABLE users MODIFY COLUMN id INT NOT NULL AUTO_INCREMENT FIRST")
    op.execute("ALTER TABLE users MODIFY COLUMN username VARCHAR(50) NOT NULL AFTER id")
    op.execute("ALTER TABLE users MODIFY COLUMN email VARCHAR(255) NOT NULL AFTER username")
    op.execute("ALTER TABLE users MODIFY COLUMN name VARCHAR(100) NOT NULL AFTER email")
    op.execute("ALTER TABLE users MODIFY COLUMN apellidos VARCHAR(100) NOT NULL AFTER name")
    op.execute("ALTER TABLE users MODIFY COLUMN hashed_password VARCHAR(255) NOT NULL AFTER apellidos")
    op.execute("ALTER TABLE users MODIFY COLUMN verified TINYINT(1) NOT NULL AFTER hashed_password")
    op.execute("ALTER TABLE users MODIFY COLUMN disabled TINYINT(1) NOT NULL AFTER verified")
    op.execute("ALTER TABLE users MODIFY COLUMN created_at DATETIME NOT NULL AFTER disabled")
    op.execute("ALTER TABLE users MODIFY COLUMN updated_at DATETIME NOT NULL AFTER created_at")


def downgrade() -> None:
    """Downgrade schema."""
    # No es necesario revertir el orden de columnas
    pass
