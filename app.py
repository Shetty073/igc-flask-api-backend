from flask import Flask, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def getmembers():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("gcreds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("igc_members").sheet1
    data = sheet.get_all_records()
    return data


def gettotalmem():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("gcreds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("igc_members").sheet1
    data = sheet.get_all_records()
    numofmem = len(data)
    return numofmem


app = Flask(__name__)


@app.route('/members', methods=['GET', 'POST'])
def members():
    return jsonify(getmembers())


@app.route('/totalmembers', methods=['GET', 'POST'])
def totalmembers():
    return jsonify(gettotalmem())


if __name__ == "__main__":
    app.run()
