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
        # gathers everything below the name of the school and puts it in a list #forloopsforever
        # first 2 cells are for date and ship ID, next 20 are for the claim #'s
        cList = [testcell]
        c = 1
        for i in cList:

            a = Monday.cell(stuff.row + c, stuff.col)
            cList.append(a)
            print(c)
            print(cList)
            c = c + 1
            if c == 23: break

        print(cList)
        if stuff.value == testcell.value:

            grabRange = [testcell]
            g = 1
            for z in grabRange:
                l = VQueue.cell(testcell.row + g, testcell.col)
                grabRange.append(l)
                g = g + 1
                if g == 23: break


            VQueue.update_cells(grabRange)
            print(grabRange)












