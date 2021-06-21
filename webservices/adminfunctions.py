from webservices.models import *
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID_input = '1EUm9MJju7oJ9vylwpPRw25dxXyK1BtqkxI7zBpcWegY'


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result_input = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                            range="Anjan!A1:D59").execute()
values_input = result_input.get('values', [])

print("============",values_input)

GSheetData.objects.create(sheet_id = SAMPLE_SPREADSHEET_ID_input, excel_data=values_input)

if not values_input and not values_expansion:
    print('No data found.')