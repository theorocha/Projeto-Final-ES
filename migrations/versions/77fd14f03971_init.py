"""init

Revision ID: 77fd14f03971
Revises: aa2df5d39569
Create Date: 2023-07-07 20:50:43.257665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77fd14f03971'
down_revision = 'aa2df5d39569'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questao_exames', sa.Column('exame_id', sa.Integer(), nullable=False))
    op.drop_constraint(None, 'questao_exames', type_='foreignkey')
    op.create_foreign_key(None, 'questao_exames', 'exames', ['exame_id'], ['id'])
    op.create_foreign_key(None, 'questao_exames', 'questoes', ['questao_id'], ['id'])
    op.drop_column('questao_exames', 'exame')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questao_exames', sa.Column('exame', sa.INTEGER(), nullable=False))
    op.drop_constraint(None, 'questao_exames', type_='foreignkey')
    op.drop_constraint(None, 'questao_exames', type_='foreignkey')
    op.create_foreign_key(None, 'questao_exames', 'exames', ['exame'], ['id'])
    op.drop_column('questao_exames', 'exame_id')
    # ### end Alembic commands ###
