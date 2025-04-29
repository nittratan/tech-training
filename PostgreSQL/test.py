import psycopg2

DATABASE_URL = 'postgresql://aidepostgres_user:TsTcQCRkuZipgwUvSWX3PaOaV4dW9RYt@dpg-d073poqli9vc73etucq0-a.oregon-postgres.render.com/aidepostgres'

conn = psycopg2.connect(DATABASE_URL)
#Replace user and password with your Postgres username and password, host and #port with the values in your database URL, and database_name with the name of #your database.


cur = conn.cursor()

cur.execute("SELECT 1;")
test_result = cur.fetchone()

# Check if the connection is successful by printing the result of the test query
if test_result:
    print("✅ Connection successful! Test query result:", test_result[0])
else:
    print("❌ Connection failed.")

# Example of fetching data from a table (optional)
# Replace 'mytable' with the actual table name you want to query

PGPASSWORD=5Wk4xT3nGM4liaqQlpcwheVX9Pyeg5le psql -h dpg-d07mo3hr0fns738nmumg-a.oregon-postgres.render.com -U test_db_gagt_user test_db_gagt