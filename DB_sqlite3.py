#coding = utf-8
import json
import sqlite3
import os


class sqlite3_test():
    
    def __init__(self):
        self.conn=sqlite3.connect("securitydog.db")
    
    def initial_tables(self):
        c=self.conn.cursor()
        self.createStarTable(c)
        self.createVideoTable(c)

    def createVideoTable(self,c):
        c.execute('''
            create TABLE VIDEO
            ( id CHAR(50) primary key NOT NULL,
              name TEXT NOT NULL,
              director CHAR(50),
              starId
              size INT NOT NULL,
              videoPath TEXT,
              coverPath TEXT,
              thumbnailPath TEXT, 
              isDownloaded INT,
              isWatched INT,
              mosaic INT,  
              area INT,
              series TEXT,
              tag TEXT

            );
        ''')
        #mosaic 0无，1普，2薄
        #area 0亚，1欧，2其他
        self.conn.commit()
        return True
    def createStarTable(self,c):
        c.execute('''
            create TABLE STAR
            ( id CHAR(50) primary key NOT NULL,
              userName CHAR(50) NOT NULL,
              orgName CHAR(50),
              birthday TEXT,
              body_B INTEGER,
              body_W INTEGER,
              body_H INTEGER,
              introduction TEXT
            );
        ''')
        self.conn.commit()
        return True

    def doExecute(self,sqlstr):

        c=self.conn.cursor()
        try:
            ret=c.execute(sqlstr)
            self.conn.commit()
            print(ret)
            for row in ret:
                print(row)
        except Exception as e:
            print("error",e)

    
if __name__ == '__main__':
    sd=sqlite3_test()
    while(True):
        sqlstr=input("input the sqlstr:\n")
        if sqlstr=="exit":
            sd.conn.close()
            break
        elif sqlstr=="init":
            sd.initial_tables()#初始化sqlite数据库表
        else:
            sd.doExecute(sqlstr)
    exit(0)
