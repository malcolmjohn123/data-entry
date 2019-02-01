from Tkinter import *
import ttk
import sqlite3

class GUI:

    db_name = "info.db"

    def __init__(self, myGui):
        self.myGui = myGui
        self.myGui.title("Info")
        self.myGui.geometry("500x500+100+100")
        
        self.tree = ttk.Treeview(self.myGui, height=100)
        
        self.tree["columns"] = ('1','2','3','4','5')
        self.tree.column('1', width=100, anchor='w')
        self.tree.column('2', width=150, anchor='w')
        self.tree.column('3', width=150, anchor='w')
        self.tree.column('4', width=150, anchor='w')
        self.tree.column('5', width=150, anchor='w')
        
        self.tree.heading('1', text="Time")
        self.tree.heading('2', text="Generator Voltage")
        self.tree.heading('3', text="Generator Current")
        self.tree.heading('4', text="Motor Voltage")
        self.tree.heading('5', text="Motor Speed")

        self.tree.pack()

        ttk.Label(self.myGui,text='Dates').place(x=200,y=10)
        ttk.Button(self.myGui,text='clear', command=self.remove_all).place(x=0,y=30)
        self.create_date_Button()

    def run_query(self, query):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query)
            conn.commit()
        return query_result

    def create_date_Button(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        self.x = cursor.fetchall()
        c=0
        for i in self.x:
            ttk.Button(self.myGui,text=str(i[0]), command=lambda:self.viewing_records(str(i[0]))).place(x=200,y=30+c)
            c+=30

    def viewing_records(self, table_name):
        query = "SELECT * FROM " + table_name 
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 0, text = str(row[0]), values = (row[1],row[2],row[3],row[4],row[5]))

    def remove_all(self):
        x = self.tree.get_children()
        for child in x:
            self.tree.delete(child)

if __name__ == '__main__':
    myGui = Tk()
    gui = GUI(myGui)
    myGui.mainloop()
    
