"""empty message

Revision ID: eabe90912128
Revises: 
Create Date: 2021-08-16 11:22:11.215031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eabe90912128'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pytorchjob',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('namespace', sa.String(length=100), nullable=True),
    sa.Column('create_time', sa.String(length=100), nullable=True),
    sa.Column('status', sa.String(length=100), nullable=True),
    sa.Column('annotations', sa.Text(), nullable=True),
    sa.Column('labels', sa.Text(), nullable=True),
    sa.Column('spec', sa.Text(length=65536), nullable=True),
    sa.Column('status_more', sa.Text(length=65536), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('info_json', sa.Text(), nullable=True),
    sa.Column('add_row_time', sa.DateTime(), nullable=True),
    sa.Column('foreign_key', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tfjob',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('namespace', sa.String(length=100), nullable=True),
    sa.Column('create_time', sa.String(length=100), nullable=True),
    sa.Column('status', sa.String(length=100), nullable=True),
    sa.Column('annotations', sa.Text(), nullable=True),
    sa.Column('labels', sa.Text(), nullable=True),
    sa.Column('spec', sa.Text(length=65536), nullable=True),
    sa.Column('status_more', sa.Text(length=65536), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('info_json', sa.Text(), nullable=True),
    sa.Column('add_row_time', sa.DateTime(), nullable=True),
    sa.Column('foreign_key', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workflow',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('namespace', sa.String(length=100), nullable=True),
    sa.Column('create_time', sa.String(length=100), nullable=True),
    sa.Column('status', sa.String(length=100), nullable=True),
    sa.Column('annotations', sa.Text(), nullable=True),
    sa.Column('labels', sa.Text(), nullable=True),
    sa.Column('spec', sa.Text(length=65536), nullable=True),
    sa.Column('status_more', sa.Text(length=65536), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('info_json', sa.Text(), nullable=True),
    sa.Column('add_row_time', sa.DateTime(), nullable=True),
    sa.Column('foreign_key', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('xgbjob',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('namespace', sa.String(length=100), nullable=True),
    sa.Column('create_time', sa.String(length=100), nullable=True),
    sa.Column('status', sa.String(length=100), nullable=True),
    sa.Column('annotations', sa.Text(), nullable=True),
    sa.Column('labels', sa.Text(), nullable=True),
    sa.Column('spec', sa.Text(length=65536), nullable=True),
    sa.Column('status_more', sa.Text(length=65536), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('info_json', sa.Text(), nullable=True),
    sa.Column('add_row_time', sa.DateTime(), nullable=True),
    sa.Column('foreign_key', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('action', sa.String(length=512), nullable=True),
    sa.Column('method', sa.String(length=50), nullable=True),
    sa.Column('path', sa.String(length=200), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('json', sa.Text(), nullable=True),
    sa.Column('dttm', sa.DateTime(), nullable=True),
    sa.Column('duration_ms', sa.Integer(), nullable=True),
    sa.Column('referrer', sa.String(length=1024), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['ab_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('changed_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('describe', sa.Text(), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.Column('expand', sa.Text(length=65536), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('repository',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('changed_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('server', sa.String(length=100), nullable=False),
    sa.Column('user', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('hubsecret', sa.String(length=100), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user_attribute',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('changed_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['ab_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('images',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('changed_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('describe', sa.Text(), nullable=True),
    sa.Column('repository_id', sa.Integer(), nullable=True),
    sa.Column('entrypoint', sa.String(length=200), nullable=True),
    sa.Column('dockerfile', sa.Text(), nullable=True),
    sa.Column('gitpath', sa.String(length=200), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['repository_id'], ['repository.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nni',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('changed_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_type', sa.Enum('Job'), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('namespace', sa.String(length=200), nullable=False),
    sa.Column('describe', sa.Text(), nullable=True),
    sa.Column('parallel_trial_count', sa.Integer(), nullable=True),
    sa.Column('maxExecDuration', sa.Integer(), nullable=True),
    sa.Column('max_trial_count', sa.Integer(), nullable=True),
    sa.Column('max_failed_trial_count', sa.Integer(), nullable=True),
    sa.Column('objective_type', sa.Enum('maximize', 'minimize'), nullable=False),
    sa.Column('objective_goal', sa.Float(), nullable=False),
    sa.Column('objective_metric_name', sa.String(length=200), nullable=False),
    sa.Column('objective_additional_metric_names', sa.String(length=200), nullable=True),
    sa.Column('algorithm_name', sa.String(length=200), nullable=False),
    sa.Column('algorithm_setting', sa.Text(), nullable=True),
    sa.Column('parameters', sa.Text(), nullable=True),
    sa.Column('job_json', sa.Text(), nullable=True),
    sa.Column('trial_spec', sa.Text(), nullable=True),
    sa.Column('working_dir', sa.String(length=200), nullable=True),
    sa.Column('volume_mount', sa.String(length=100), nullable=True),
    sa.Column('node_selector', sa.String(length=100), nullable=True),
    sa.Column('image_pull_policy', sa.Enum('Always', 'IfNotPresent'), nullable=False),
    sa.Column('resource_memory', sa.String(length=100), nullable=True),
    sa.Column('resource_cpu', sa.String(length=100), nullable=True),
    sa.Column('resource_gpu', sa.String(length=100), nullable=True),
    sa.Column('experiment', sa.Text(), nullable=True),
    sa.Column('alert_status', sa.String(length=100), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('notebook',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('changed_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('describe', sa.Text(), nullable=True),
    sa.Column('namespace', sa.String(length=200), nullable=True),
    sa.Column('images', sa.String(length=200), nullable=True),
    sa.Column('ide_type', sa.String(length=200), nullable=True),
    sa.Column('working_dir', sa.String(length=200), nullable=True),
    sa.Column('volume_mount', sa.String(length=400), nullable=True),
    sa.Column('node_selector', sa.String(length=200), nullable=True),
    sa.Column('image_pull_policy', sa.Enum('Always', 'IfNotPresent'), nullable=True),
    sa.Column('resource_memory', sa.String(length=100), nullable=True),
    sa.Column('resource_cpu', sa.String(length=100), nullable=True),
    sa.Column('resource_gpu', sa.String(length=100), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('pipeline',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('changed_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('describe', sa.String(length=200), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('dag_json', sa.Text(), nullable=False),
    sa.Column('namespace', sa.String(length=100), nullable=True),
    sa.Column('global_env', sa.String(length=500), nullable=True),
    sa.Column('schedule_type', sa.Enum('once', 'crontab'), nullable=False),
    sa.Column('cron_time', sa.String(length=100), nullable=True),
    sa.Column('pipeline_file', sa.Text(length=65536), nullable=True),
    sa.Column('pipeline_argo_id', sa.String(length=100), nullable=True),
    sa.Column('version_id', sa.String(length=100), nullable=True),
    sa.Column('run_id', sa.String(length=100), nullable=True),
    sa.Column('node_selector', sa.String(length=100), nullable=True),
    sa.Column('image_pull_policy', sa.Enum('Always', 'IfNotPresent'), nullable=False),
    sa.Column('parallelism', sa.Integer(), nullable=False),
    sa.Column('alert_status', sa.String(length=100), nullable=True),
    sa.Column('alert_user', sa.String(length=300), nullable=True),
    sa.Column('expand', sa.Text(length=65536), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('project_user',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('changed_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('role', sa.Enum('dev', 'ops', 'creator'), nullable=False),
    sa.Column('created_by_fk', sa.Integer(), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['ab_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('project_id', 'user_id')
    )
    op.create_table('service',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('changed_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('label', sa.String(length=100), nullable=False),
    sa.Column('images', sa.String(length=200), nullable=False),
    sa.Column('working_dir', sa.String(length=100), nullable=True),
    sa.Column('command', sa.String(length=1000), nullable=True),
    sa.Column('args', sa.Text(), nullable=True),
    sa.Column('env', sa.Text(), nullable=True),
    sa.Column('volume_mount', sa.String(length=200), nullable=True),
    sa.Column('node_selector', sa.String(length=100), nullable=True),
    sa.Column('min_replicas', sa.Integer(), nullable=True),
    sa.Column('max_replicas', sa.Integer(), nullable=True),
    sa.Column('ports', sa.String(length=100), nullable=True),
    sa.Column('resource_memory', sa.String(length=100), nullable=True),
    sa.Column('resource_cpu', sa.String(length=100), nullable=True),
    sa.Column('resource_gpu', sa.String(length=100), nullable=True),
    sa.Column('deploy_time', sa.String(length=100), nullable=False),
    sa.Column('host', sa.String(length=200), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('job_template',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('changed_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('version', sa.Enum('Release', 'Alpha'), nullable=False),
    sa.Column('images_id', sa.Integer(), nullable=True),
    sa.Column('hostAliases', sa.Text(), nullable=True),
    sa.Column('describe', sa.Text(), nullable=True),
    sa.Column('workdir', sa.String(length=400), nullable=True),
    sa.Column('entrypoint', sa.String(length=200), nullable=True),
    sa.Column('args', sa.Text(), nullable=True),
    sa.Column('env', sa.Text(), nullable=True),
    sa.Column('volume_mount', sa.String(length=400), nullable=True),
    sa.Column('privileged', sa.Boolean(), nullable=True),
    sa.Column('accounts', sa.String(length=100), nullable=True),
    sa.Column('demo', sa.Text(), nullable=True),
    sa.Column('expand', sa.Text(length=65536), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['images_id'], ['images.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('kfservice',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('changed_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('label', sa.String(length=100), nullable=False),
    sa.Column('service_type', sa.Enum('predictor', 'transformer', 'explainer'), nullable=False),
    sa.Column('default_service_id', sa.Integer(), nullable=True),
    sa.Column('canary_service_id', sa.Integer(), nullable=True),
    sa.Column('canary_traffic_percent', sa.Integer(), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['canary_service_id'], ['service.id'], ),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['default_service_id'], ['service.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('run',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pipeline_id', sa.Integer(), nullable=True),
    sa.Column('pipeline_file', sa.Text(length=65536), nullable=True),
    sa.Column('pipeline_argo_id', sa.String(length=100), nullable=True),
    sa.Column('version_id', sa.String(length=100), nullable=True),
    sa.Column('experiment_id', sa.String(length=100), nullable=True),
    sa.Column('run_id', sa.String(length=100), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['pipeline_id'], ['pipeline.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('task',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('changed_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('label', sa.String(length=100), nullable=False),
    sa.Column('job_template_id', sa.Integer(), nullable=True),
    sa.Column('pipeline_id', sa.Integer(), nullable=True),
    sa.Column('working_dir', sa.String(length=1000), nullable=True),
    sa.Column('command', sa.String(length=1000), nullable=True),
    sa.Column('overwrite_entrypoint', sa.Boolean(), nullable=True),
    sa.Column('args', sa.Text(), nullable=True),
    sa.Column('volume_mount', sa.String(length=200), nullable=True),
    sa.Column('node_selector', sa.String(length=100), nullable=True),
    sa.Column('resource_memory', sa.String(length=100), nullable=True),
    sa.Column('resource_cpu', sa.String(length=100), nullable=True),
    sa.Column('resource_gpu', sa.String(length=100), nullable=True),
    sa.Column('timeout', sa.Integer(), nullable=False),
    sa.Column('retry', sa.Integer(), nullable=False),
    sa.Column('outputs', sa.Text(), nullable=True),
    sa.Column('monitoring', sa.Text(), nullable=True),
    sa.Column('expand', sa.Text(length=65536), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['job_template_id'], ['job_template.id'], ),
    sa.ForeignKeyConstraint(['pipeline_id'], ['pipeline.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    op.drop_table('run')
    op.drop_table('kfservice')
    op.drop_table('job_template')
    op.drop_table('service')
    op.drop_table('project_user')
    op.drop_table('pipeline')
    op.drop_table('notebook')
    op.drop_table('nni')
    op.drop_table('images')
    op.drop_table('user_attribute')
    op.drop_table('repository')
    op.drop_table('project')
    op.drop_table('logs')
    op.drop_table('xgbjob')
    op.drop_table('workflow')
    op.drop_table('tfjob')
    op.drop_table('pytorchjob')
    # ### end Alembic commands ###
