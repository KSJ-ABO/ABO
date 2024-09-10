import 

def check_cache():
  conn = pymysql.connect(host = 'localhost', 'user=root', password = '', 'db = 'myhome', charset = 'utf8')  
  cur = conn.cursor() 
  data = cur.execute("SELECT * FROM cache WHERE typo_name = %s", (input,)) 
  if data == null:
    return 0;
  else:
    return data;
    

def insert_cache(typo_name, accuracy, name):
  conn = pymysql.connect(host = 'localhost', 'user=root', password = '', 'db = 'myhome', charset = 'utf8')
  typo_name = sys.argv[1]
  accuracy = float(sys.argv[2])
  name = sys.argv[3]
  
  try:
    cur.execute(“"INSERT INTO cache VALUES (typo_name, accuracy, name)")
    conn.commit()
  finally:
    conn.close()
    return 1;
