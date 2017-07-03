import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('OAuthInfo.json', scope)
gs = gspread.authorize(credentials)

# opens the Virtual Shipping Queue
sheet = gs.open_by_url('https://docs.google.com/spreadsheets/d/1LBzBtBcJQQNEVc3zoMS3ArPWQmedydDwF562iq7mMMY/edit#gid=0')

# opens the different worksheets
VQueue = sheet.get_worksheet(0)
Key = sheet.get_worksheet(1)
Priority = sheet.get_worksheet(2)

SchoolList = []
PrioList = []
ClaimList = []
ReplacedCells = []
#makes a list of every school on teh VQueue sheet
def MakeSchoolList():
    startCell = VQueue.acell('b7')
    c = 0
    r = 0
    i = 0
    while i < 33:
        SchoolList.append(VQueue.cell(startCell.row + r, startCell.col + c))
        i = i + 1
        c = c + 1
        if c == 12:
            r = r + 28
            c = 0


def MakePrioList():
    r = 3
    c = 2
    while c < 50:
        a = Priority.cell(r, c)
        if a.value == "": break
        PrioList.append(a)
        c = c + 1
    print(PrioList)

#
def CheckForMatch():
    for o in PrioList:
        for a in SchoolList:
            if a == "":break
            if o.value == a.value:
                print("found a match", a, " & ", o)
                d = SchoolList.index(a)
                SchoolList.pop(d)
                print("schoolList index = ", d)
                ReplaceMatch(o, a)
                break



def ReplaceMatch(priocell, vqcell):
    GetClaimList(priocell)
    i = 0

    for c in ClaimList:
        a = VQueue.cell(vqcell.row + i, vqcell.col)
        a.value = c.value
        i = i + 1
        ReplacedCells.append(a)
    VQueue.update_cells(ReplacedCells)
    for c in ClaimList:
        c.value = ""
    Priority.update_cells(ClaimList)
    ClaimList.clear()

def GetClaimList(priocell):
    i = 0
    while i < 21:
        a = Priority.cell(priocell.row + i, priocell.col)
        if a.value =="": break
        ClaimList.append(a)
        i = i + 1
    #print("ClaimLIst", ClaimList)
MakeSchoolList()
MakePrioList()
CheckForMatch()
