
import pyodbc as odbccon
conn = odbccon.connect('Driver={SQL Server};'
                      'Server=DESKTOP-1VDKEN9\SQLEXPRESS;'
                      'Database=bt_interviews;'
                      'Trusted_Connection=yes;')

def getUserEvents():
   data = pd.read_sql('SELECT * FROM bt_interviews.tbl_userEvents', conn)
   return data