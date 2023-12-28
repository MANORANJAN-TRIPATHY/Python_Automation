from flask import Flask, render_template
import pyodbc
from watchdog.events import EVENT_TYPE_OPENED

app = Flask(__name__)

# Replace these placeholders with your actual SQL Server credentials
server_name = 'LAPTOP-PO1MV019\\SQLEXPRESS'
database_name = 'AdventureWorks2019'

# Establish a connection using Windows Authentication
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    f'SERVER={server_name};'
    f'DATABASE={database_name};'
    'Trusted_Connection=yes;'
)

# Create a cursor
cursor = conn.cursor()

# Define a route to display table data on a webpage
@app.route('/')
def index():
    # Example: Execute a query to fetch data from a table
    cursor.execute("SELECT * FROM Sales.Customer")
    
    # Fetch all rows
    rows = cursor.fetchall()
     
    #rows = cursor.execute("select * from Sales.Customer")

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Render the template with the fetched data
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(debug= False)
