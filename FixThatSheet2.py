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
Priority = sheet.get_worksheet(2)


PrioList = []
VQueueSchools = []
ClaimList = []



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
        i = i + 1
        if i == 13: break
    #print(VQueueSchools)

# Makes a list of priorities from the Priority sheet
def GatherPrio():
    startCell = Priority.acell('b3')
    PrioList.insert(0, startCell)
    i = 1

    for q in PrioList:
        if q.value == "":
            q.value = "*"
        a = Priority.cell(startCell.row, startCell.col + i)
        PrioList.append(a)
        i = i + 1
        if a.value == "": break
        elif i > 100: break
    FindPrio()


# checks if the school in the VQueue sheet is a priority
def FindPrio():
    for q in VQueueSchools:
        for z in PrioList:
            if z.value == q.value:
                print(q)

                GetClaimList(z.row, z.col, q)
                break
            try:
                VQueueSchools.remove(q)
                print(VQueueSchools)
            except:
                pass


# Gets the relevant info below the school on the priority sheet if its also on the VQueue sheet
def GetClaimList(row, col, VQueueCell):
    startCell = Priority.cell(row,col)
    ClaimList.append(startCell)
    i = 1
    for q in ClaimList:
        a = Priority.cell(startCell.row + i, startCell.col)

        ClaimList.append(a)
        i = i + 1
        if a.value == "": break
    ReplaceCells(VQueueCell)


# Replaces the cells below the school on the VQueue sheet with the claim list from GetClaimList()
def ReplaceCells(startCell):

    print("startcell", startCell)
    i = 0
    for q in ClaimList:
        a = VQueue.cell(startCell.row + i, startCell.col)
        a.value = q.value
        i = i + 1
        #print(a)
        if a.value == "":
            print("end of list")
            break

        if a.value != "*":
            VQueue.update_cell(a.row, a.col, a.value)

    #print(ClaimList)
    d = ClaimList[0]
    if d.value != "*":
        #Priority.update_cell(d.row, d.col, "")
        for c in ClaimList:
            Priority.update_cell(c.row, c.col, "")
    #print(d)
    for v in ClaimList:
        Priority.update_cell(v.row, v.col, "")
    ClaimList.clear()



GetSchoolsVQueue()
# print(VQueueSchools)
GatherPrio()
#print(PrioList)



quit()



















