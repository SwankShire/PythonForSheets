import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('OAuthInfo.json', scope)
gs = gspread.authorize(credentials)

# opens the Virtual Shipping Queue
sheet = gs.open_by_url('https://docs.google.com/spreadsheets/d/1LBzBtBcJQQNEVc3zoMS3ArPWQmedydDwF562iq7mMMY/edit#gid=0')

# opens the different worksheetss
VQueue = sheet.get_worksheet(0)
SchoolList = sheet.get_worksheet(1)
Monday = sheet.get_worksheet(2)
PrioList = []
VQueueSchools = []
# Gathers a list of schools on the VQueue sheet
def GetSchoolsVQueue():
    startCell = VQueue.acell('b7')
    VQueueSchools.insert(0, startCell)
    i = 1
    for q in VQueueSchools:
        if q.value == "":
            q.value = "*"
        a = VQueue.cell(startCell.row, startCell.col + i)

        VQueueSchools.append(a)
        i = i+1
        if i == 13: break

def GatherPrio():
    startCell = Monday.acell('b3')
    PrioList.insert(0, startCell)
    i = 1

    for q in PrioList:
        if q.value == "":
            q.value = "*"
        a = Monday.cell(startCell.row, startCell.col + i)
        PrioList.append(a)
        i = i + 1
        if a.value == "": break
        elif i > 100: break

def FindPrio():

    for q in VQueueSchools:
        print(q)

        if q.value in PrioList:
            print("IT WORKS")
        #print(q)



GetSchoolsVQueue()
# print(VQueueSchools)
#GatherPrio()
#print(PrioList)
FindPrio()




















