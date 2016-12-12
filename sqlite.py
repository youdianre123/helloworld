import sqlite3
import Crawl
import uuid
path = "/media/youdianre/project/com/Python/sqlite-tool/"
conn = sqlite3.connect(path + "dict.db")
#sql = "create table if not exists tb_dict(id char(32) primary key, name char(30) not null, ph_am char(100), content char(1024), list_index int(3), type int(1), create_time timestamp, update_time timestamp)"

id = uuid.uuid1()
sql = "insert into tb_dict(id, name, ph_am, content, list_index, type) values('%s', '%s',  \"%s\", '%s', '%s', '%s')"



fileName = ["testA/wordlist" + ("0"+str(i), str(i))[i >= 10] + ".txt" for i in range(1, 50)]
count = 0
#fileName = ["testA/wordlist50.txt"]
for i in fileName:
    with open(i, 'r') as file:
        for line in file.readlines():
            count = count + 1
            list = line.split(";")
            if len(list) == 1:
                print list
                break
            name = list[0].split("[")

            content = list[1:]
            content[-1] = content[-1].strip()
            insert = sql % (uuid.uuid1(), name[0], "\[" + name[1], "".join(content), i[-6:-4], '0')
            conn.execute(insert)

conn.commit()
conn.close()
print count
