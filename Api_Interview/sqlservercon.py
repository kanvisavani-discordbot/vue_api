import pyodbc as odbccon
conn = odbccon.connect('Driver={SQL Server};'
                      'Server=DESKTOP-1VDKEN9\SQLEXPRESS;'
                      'Database=bt_interviews;'
                      'Trusted_Connection=yes;')

#cursor = conn.cursor()
#cursor.execute('SELECT * FROM bt_interviews.dbo.tbl_userEvents')

#for row in cursor:
#    print(row)
def getUserEvents()->list:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM bt_interviews.dbo.tbl_userEvents')
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        print(type(results.append(dict(zip(columns, row)))))
    return results

print(getUserEvents())