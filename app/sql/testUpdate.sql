
update suites set data = jsonb_insert(data, %(test)s, %(data)s) where id = %(id)s
