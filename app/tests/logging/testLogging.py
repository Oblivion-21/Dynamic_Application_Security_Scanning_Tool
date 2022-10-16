#Check to see if logs are exposed on URL path. To do this we want to  >????
#Check URL first 
#Make dictionary of popular logs (log.log, enginx.log poop.log, php.log, wordpress.log)
#Check if it is accessible via URL
from re import I
import requests
import testManager

logList = [
    "log.log",
    "logs/access.log",
    "access.log",
    "nginx-access.log",
    "sslparams.log",
    "access.log",
    "/var/log/apache2/error.log",
    "/var/log/nginx/error.log",
    "debug.log",
    "kinsta-cache-perf.log",
    "logs/php-deprecation-warnings.log",
    "custom.log",
    "logs/laravel.log",
    "/var/log/ruby.log",
    "log/#{Rails.env}.log",
    "rails.logger",
    "/var/log/letsencrypt/letsencrypt.log",
    "letsencrypt.log",
    "mysql.log",
    "/var/log/mysql/mysql.log",
    "mysql_error.log",
    "mysql-slow.log",
    "/var/log/mysql/mysql-slow-query.log",
    "postgresql.log",
    "/var/log/redis_6379.log",
    "redis_6379.log",
    "mongod.log",
    "/var/log/mongodb/mongod.log",
    "es.log",
    "es.logs"
]

 
#Setup main fuction taking in url as an argument
async def testLogging(ws, session, testConfig, url, useDatabase):
    try:
        if "://" not in url:
            url = f"https://{url}/"
        requests.get(url) 

        for logFile in logList:
            appendedUrl = f"{url}{logFile}"
            res = requests.get(appendedUrl)
            if res.status_code > 199 and res.status_code < 300:
                return await testManager.sendMessage(ws, {"message": "FAILED"}, url, True, "testLogging", useDatabase)

        return await testManager.sendMessage(ws, {"message": "PASSED"}, url, True, "testLogging", useDatabase)

    except Exception as e: 
        return await testManager.sendMessage(ws, {"message": f"INVALID - {e}"}, url, True, "testLogging", useDatabase)
