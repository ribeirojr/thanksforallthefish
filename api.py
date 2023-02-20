from flask import Flask
from data import insertThanks, GetAllThanks

app = Flask(__name__)

insertThanks('test', 'thanks mate')

@app.route("/")
def GetAllThanksFromDb():
	result = "<ul>"
	for thanks in get_all_thanks():
		result += "<li>" + thanks.message + "</li>"
	result += "</ul>"
	return result

@app.route("/insert", methods=['POST'])
def Insert():
	InsertThanks(request.email, request.message)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
