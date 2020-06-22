import sqlite3
from controlclass import controlclass

conn = sqlite3.connect('sqlite:///Sox.db')
c = conn.cursor()


def insert_control(control):
    with conn:
        c.execute("INSERT INTO TestControl VALUES (:section, :cycle, :process, :control, :tester, :Reviewer, :Status, "
                  ":Effect, :Due, :Category)",
                  {'section': control.section, 'cycle': control.cycle, 'process': control.process, 'process': control.control, 'process': control.control3})
