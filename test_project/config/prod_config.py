from config import BaseConfig

class Config(BaseConfig):
	host = '192.168.244.207'
	port = 5001
	api_url = 'http://192.168.244.207:5000/'
	couchbase_bucket_for_logs = 'TestProjectLogsProd'