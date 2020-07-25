# make sure to edit below details
#	Google Project -> Enter Your google Cloud Project ID
#	dataset -> Dataset for Google Cloud Big Query
#	table -> Table for Google Cloud Big Query from above selected Dataset


from google.cloud import bigquery
client = bigquery.Client()
 
query = """ SELECT * FROM `<Google Project>.<dataset>.<table>` """
results = client.query(query)

print('ID | Name | Address') # Enter Columns (I have assumed 3 Columns ID, Name and Address)
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
for row in results:
    ID = row['ID']
    Name = row['Name']
    Address = row['Address']
    print(f'{ID} | {Name} | {Address}')

