import sqlite3
import time

def create_table(date):
    conn = sqlite3.connect("info.db")
    cursor = conn.cursor()
    cmd = "CREATE TABLE IF NOT EXISTS " + date + "(ID int primary key,\
                                     time time,\
                                     GeneratorVoltage double,\
                                     GeneratorCurrent double,\
                                     MotorVoltage double,\
                                     MotorSpeed double);"
    cursor.execute(cmd)
    conn.commit()
    conn.close()
    
def insert_update(*args):
    date = str(args[6])
    conn = sqlite3.connect("info.db")
    cmd = "SELECT * FROM " + date +" WHERE ID=" + str(args[0])
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if(isRecordExist == 1):
        cmd1 = "UPDATE " + date + " SET time="+str(args[1])+"WHERE ID="+str(args[0])+';'
        cmd2 = "UPDATE " + date + " SET GeneratorVoltage="+str(args[2])+"WHERE ID="+str(args[0])+';'
        cmd3 = "UPDATE " + date + " SET GeneratorCurrent="+str(args[3])+"WHERE ID="+str(args[0])+';'
        cmd4 = "UPDATE " + date + " SET MotorVoltage="+str(args[4])+"WHERE ID="+str(args[0])+';'
        cmd5 = "UPDATE " + date + " SET MotorSpeed="+str(args[5])+"WHERE ID="+str(args[0])+';'
        cursor.execute(cmd1)
        cursor.execute(cmd2)
        cursor.execute(cmd3)
        cursor.execute(cmd4)
        cursor.execute(cmd5)
        conn.commit()
        conn.close()
    else:
        cmd="INSERT INTO "+ date +"(ID,time,GeneratorVoltage,GeneratorCurrent,MotorVoltage,MotorSpeed) Values("+str(args[0])+','+str(args[1])+','+str(args[2])+','+str(args[3])+','+str(args[4])+','+str(args[5])+');'
        cursor.execute(cmd)
        conn.commit()
        conn.close()
        
d1  = "Feb42018"
d2 =  "Feb52018"
create_table(d1)
create_table(d2)

ID = 1
time = '55'
GeneratorVoltage = 50
GeneratorCurrent = 3.5
MotorVoltage = 70
MotorSpeed = 5
insert_update(ID,time,GeneratorVoltage,GeneratorCurrent,MotorVoltage,MotorSpeed,d1)
insert_update(ID,time,GeneratorVoltage,GeneratorCurrent,MotorVoltage,MotorSpeed,d2)

