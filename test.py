import csv
import sys, traceback
import mwreverts.api
import mwapi


# Opens file, puts each line in separate list
file = open("quarry-30104-untitled-run294482.tsv", "r")
csv_reader = csv.reader(file)

# Skips first line
next(csv_reader)

# Converts each id to integer, inserts each id in rev_ids list
rev_ids = []
for line in csv_reader:
    id =int(line[0])
    # print(id)
    rev_ids.append(id)


session = mwapi.Session("https://en.wikipedia.org", user_agent="Research")
reverts = []
for revid in rev_ids[20:40]:
    reverting, reverted, reverted_to = mwreverts.api.check(session, revid)
    # if reverted != None:
    #     user_id= reverted[0]
    # else:
    #     user_id = None

    print(revid,'\nReverting:',reverting,'\nreverted:',reverted,'\nreverted_to:',reverted_to,"\n\n",)