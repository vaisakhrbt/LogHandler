import os

class BaseConfig(object):
	debug_mode = True
	logging_mode = True

	host = '0.0.0.0'
	port = 5000
	couchbase_ip = '192.168.244.198:8091'
	couchbase_bucket = 'TestProject'
	couchbase_bucket_for_logs = 'TestProjectLogs'
	couchbase_connection = 'couchbase://'+couchbase_ip+'/'+couchbase_bucket