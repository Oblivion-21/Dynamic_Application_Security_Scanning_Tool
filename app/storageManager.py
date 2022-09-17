from itertools import chain

import psycopg2
import psycopg2.extras

connectArgs = {
    "dbname": "dast",
    "user": "dastuser",
    "password": "password",
    "host": "127.0.0.1",
    "port": 5432
}


def databaseExec(filePath, sqlArgs=None):
    with psycopg2.connect(**connectArgs) as con:
        with con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            with open(filePath, "r") as sqlFile:
                sql = sqlFile.read()
                cur.execute(sql, sqlArgs)
                if not cur.description:
                    return
                return cur.fetchall()


def setup():
    try:
        databaseExec("sql/setup.sql")
        return True
    except Exception as e:
        print(f"Exception occur while trying to setup database: {e}")
        return False


def insert(suiteID, url, data):
    databaseExec("sql/insert.sql", {"id": suiteID, "url": url, "data": data})


def update(suiteID, data):
    databaseExec("sql/update.sql", {"id": suiteID, "data": data})


def testUpdate(suiteID, test, data):
    databaseExec("sql/testUpdate.sql", {"id": suiteID, "test": f"{{{test}}}", "data": data})


def show(limit=20):
    res = databaseExec("sql/show.sql", {"limit": limit})
    return list(chain(*res))


def currentIdentity():
    res = databaseExec("sql/currentIdentity.sql")
    return res[0][0]
