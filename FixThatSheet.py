import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']


credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/nathan/Programming/OAuthInfo.json', scope)

gs = gspread.authorize(credentials)

#opens the Virtual Shipping Queue
sheet = gs.open_by_url('https://docs.google.com/spreadsheets/d/1LBzBtBcJQQNEVc3zoMS3ArPWQmedydDwF562iq7mMMY/edit#gid=0')

#opens the different worksheetss
VQueue = sheet.get_worksheet(0)
SchoolList = sheet.get_worksheet(1)
Monday = sheet.get_worksheet(2)

#pulls the list of schools from the key worksheet
Schools = SchoolList.range('B1:B300')

print('list of schools')
print(Schools)

for i in Schools:
    try:
        b = Monday.find(schools)
        print(b)

    except:
        print('error')
        print(i)







