import mysql.connector

#Connect to mysql database
mydb = mysql.connector.connect(
  host="localhost",
  user="bpittman",
  passwd="",
  database="afniboard"
)

mycursor = mydb.cursor()

#mysql select to identify unapproved messages
mycursor.execute("Select author, subject from phorum_messages where status = -1 and (author != 'rick reynolds') and (author != 'Daniel Glen') and (author != 'ptaylor') and (author != 'gangc') and (author != 'GANG') and (author !='cooldesert') and (author != 'Doughboys') and (author != 'sondosayyash') and (author != 'Ddickstein') and (author != 'roopchansinghv') and (author != 'paul.hamilton') and (author != 'st') and (author != 'Galit') and (author != 'nstuart') and (author != 'kkinder5') and (author != 's.meliss') and (author != 'patrick.rollo@uth.tmc.edu') and (author != 'Ilaria') and (author != 'shanaadise') and (author != 'Larry Barsalou') and (author != 'lhopkins') and (author != 'dingzhihu') and (author != 'carolin31') and (author != 'cibuthomas') and (author != 'RS Yuan') and (author != 'Matthew_2') and (author != 'Phil Burton') and (author != 'EXP.2086') and (author != 'AFNIbeginner') and (author != 'bebe') and (author != 'jkeidel') and (author != 'Kirk') and (author != 'ysagon')") 

myresult = mycursor.fetchall()

for x in myresult:
    print(x, mycursor.rowcount)



 
