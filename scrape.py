from bs4 import BeautifulSoup
import csv

with open('contracts.html', 'r') as html_file:
	content = html_file.read()
	header_row = []


# pull headers from table
    
	soup = BeautifulSoup(content, 'lxml')
	headers = soup.find_all('thead')
	for heads in headers:
		headers = heads.find_all('th')
	
	str_cells = str(headers)
	headers = BeautifulSoup(str_cells, "lxml").get_text()
	header_row.append(headers)
	#print(headers)
    
# pull player names from table

	table = soup.find_all('tbody')
	data_rows = []
	for rows in table:
		table_rows = rows.find_all('tr', class_="sortable")
		for cells in table_rows:
			data = cells.find_all('td')
			str_cells = str(data)
			players = BeautifulSoup(str_cells, "lxml").get_text()
			players = players.split()
			
			data_rows.append(players)



	#print(data_rows) #this prints out all the data from the table as a list for every player



with open("capleague.csv", "w") as f:
	writer = csv.writer(f)
	writer.writerow(header_row)
	writer.writerows(data_rows)




			

				









