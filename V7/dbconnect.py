#!/usr/bin/python

import mysql.connector as sql
from mysql.connector import Error

config = {
	"user": "root",
#	"password": "root",
#	"password": "checkout",
#	"host": "192.168.1.11",
	"unix_socket": "/tmp/mysql.sock",
	"database": "pong",
	"raise_on_warnings": True,
}


def pull():
    try:
        db = sql.connect(**config)
        if db.is_connected():
            print("Connection successful!")
                    
            cursor = db.cursor()
            query = "SELECT pOneName, pTwoName, pOneScore, pTwoScore, winner, gameDate \
            FROM matches ORDER BY gameDate ASC LIMIT 5;"
            cursor.execute(query)
            rows = cursor.fetchall()

            return rows
        
    except Error as e:
        print (e)
        
    finally:
        db.close()
        print("Connection closed!")

def push(pOneName, pTwoName, pOneScore, pTwoScore, winner, gameDate):
    try:
        db = sql.connect(**config)
        if db.is_connected():
            print("Connection successful!")
            
            cursor = db.cursor()
            print "sql: ", pOneName, pTwoName, pOneScore, pTwoScore, winner, gameDate
            query = "INSERT INTO matches (pOneName, pTwoName, pOneScore, pTwoScore, winner, gameDate) \
                VALUES('%s', '%s', %d, %d, %d, '%s');" % (pOneName, pTwoName, pOneScore, pTwoScore, winner, gameDate)

            cursor.execute(query)

    except Error as e:
        print (e)

    finally:
        db.close()
        print("Connection closed!")



#if __name__ == "__main__":
#	connect()

#cursor = db.cursor()

#query = ("SELECT * FROM scores "
#	"ORDER BY playerScore")

#cursor.execute(query)
