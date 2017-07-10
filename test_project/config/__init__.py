import os
test_project_env = os.getenv('ENV_TEST_PROJECT', 'dev').lower()
if test_project_env == 'prod':
	from prod_config import Config
else:
	# dev
	from dev_config import Config


