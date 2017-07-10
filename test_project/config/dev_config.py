from config import BaseConfig

class Config(BaseConfig):
	host = 'localhost'
	port = 5050
	api_url = 'http://localhost:5000/'
	couchbase_bucket_for_logs = 'TestProjectLogsDev'