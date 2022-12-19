import sqlite3

con = sqlite3.connect("database")
cur = con.cursor()

def get_sources():
    res = cur.execute("SELECT * FROM Sources")
    return res.fetchall()

def get_users(sources):
    t = (sources,)
    res = cur.execute("SELECT * FROM Users WHERE Sources = ?", t)
    return res.fetchall()

def check_progress(tmp_rooms,source,user):
    rooms=[]
    for room in tmp_rooms:
        t = (source,user,room['id'],)
        res = cur.execute("SELECT count(*) FROM Progress WHERE Sources = ? AND UserId = ? AND roomId = ?",t)
        if res.fetchone() ==(0,):
            cur.execute("INSERT INTO Progress(Sources,UserId,roomId) VALUES(?,?,?)",t)
            con.commit()
            rooms.append(room)
    return rooms