#!/home/eps91-epixel/.local/share/virtualenvs/python-tutorial-F36CvGBT/bin/python3
import cgi;
import cgitb;
cgitb.enable()
import psycopg2

print("Content-Type: text/html")
print("") #use this double quote print statement to add a blank line in the script

# get form data
form = cgi.FieldStorage()   
id = form.getvalue('emp-id')    
name = form.getvalue('emp-name')
designation = form.getvalue('emp-desig')  
department_id = form.getvalue('emp-dept-id')  


# Add data to database using psycopg2
# Use print() to return response
hostname = 'localhost'
database = 'python'
username = 'postgres'
pwd = 'root@123'
port_id = 5432


try:    

        conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id
        
        )

        cur = conn.cursor()
        insert_script = 'INSERT INTO employees(id,name,designation,department_id) VALUES(%s, %s,%s,%s)'
        insert_value = (id ,name,designation,department_id)

        cur.execute(insert_script, insert_value)

        conn.commit()
except Exception as error:
        print ("weeeee",error)

finally:
        if cur is not None:
                cur.close()
        if conn is not None:
                conn.close()
