import requests
import csv
import sys
def IPisTor(ip,timestamp):
    url = "http://metrics.torproject.org/exonerator.html?ip={ip}&timestamp={timestamp}&lang=en".format(ip = ip,timestamp = timestamp)
    response = requests.get(url)
    response = response.text
    response = response[8530:8560]
    index = response.find('Result is')
    response_text = response[index:index+18]

    if response_text == "Result is positive":
        return True
    elif response_text == "Result is negative":
        return False
    else:
        return "No result found"

# Opens file, puts each line in separate list
file = open(sys.argv[1], "r")
csv_reader = csv.reader(file,delimiter='\t')
next(csv_reader)
csv_reader = list(csv_reader)

# loops through list of IP addresses/timestamps and feeds them into IPisTor, returning true or false
for list in csv_reader:
    ip = list[1]
    timestamp = list[2]
    res = IPisTor(ip,timestamp)