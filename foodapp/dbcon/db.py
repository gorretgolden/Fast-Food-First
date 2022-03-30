import psycopg2 #pip install psycopg2 
import psycopg2.extras

DB_HOST = "localhost"
DB_NAME = "restaurantdb"
DB_USER = "postgres"
DB_PASSWORD = "#golden@" 
 
# Open a cursor to perform database operations 

conn = psycopg2.connect( host= DB_HOST,database= DB_NAME,user= DB_USER,password= DB_PASSWORD)
# cur = conn.cursor(psycopg2.extras.DictCursor)