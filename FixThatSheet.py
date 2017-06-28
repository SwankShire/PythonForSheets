import gspread
from oauth2client.service_account import ServiceAccountCredentials

# autorizes stuff
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('OAuthInfo.json', scope)
gs = gspread.authorize(credentials)

# opens the Virtual Shipping Queue
sheet = gs.open_by_url('https://docs.google.com/spreadsheets/d/1LBzBtBcJQQNEVc3zoMS3ArPWQmedydDwF562iq7mMMY/edit#gid=0')

# opens the different worksheetss
VQueue = sheet.get_worksheet(0)
SchoolList = sheet.get_worksheet(1)
Monday = sheet.get_worksheet(2)

# pulls the list of schools from the key worksheet
Schools = SchoolList.range('B1:B300')

# gathers priority from monday sheet
MdayPrio = Monday.range('B3:AA3')
# test cell REMEMBER TO DELETE THIS WHEN DONE
testcell = VQueue.acell('b7')

# goes through everything in the B3 row on the Monday sheet
for stuff in MdayPrio:
    # checks if the cell is empty
    if stuff.value != "":
        # gathers everything below the name of the school.
        # first 2 cells are for date and ship ID, next 20 are for the claim #'s

        cellList = [Monday.cell(stuff.row+1, stuff.col), Monday.cell(stuff.row+2, stuff.col),
                    Monday.cell(stuff.row+3, stuff.col), Monday.cell(stuff.row+4, stuff.col),
                    Monday.cell(stuff.row+5, stuff.col),
                    Monday.cell(stuff.row+6, stuff.col), Monday.cell(stuff.row+7, stuff.col),
                    Monday.cell(stuff.row+8, stuff.col), Monday.cell(stuff.row+9, stuff.col),
                    Monday.cell(stuff.row+10, stuff.col), Monday.cell(stuff.row+12, stuff.col),
                    Monday.cell(stuff.row+13, stuff.col), Monday.cell(stuff.row+14, stuff.col),
                    Monday.cell(stuff.row+15, stuff.col), Monday.cell(stuff.row+16, stuff.col),
                    Monday.cell(stuff.row+17, stuff.col), Monday.cell(stuff.row+18, stuff.col),
                    Monday.cell(stuff.row+19, stuff.col), Monday.cell(stuff.row+20, stuff.col),
                    Monday.cell(stuff.row+21, stuff.col), Monday.cell(stuff.row+22, stuff.col)]
        print(cellList)
        if stuff.value == testcell.value:


            grabRange = []


            VQueue.update_cells(grabRange)
            print(grabRange)












