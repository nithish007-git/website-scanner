from flask import Flask,render_template,request
import requests
import json

global site1
app=Flask(__name__)
@app.route('/')
def temp():
    return render_template('index.html')


@app.route('/',methods=["Post"])
def get():
    site1 = request.form.get("say")
    print("hello")
    api_key = "9ef46010808934b1ddcd789dedb639b1403c3db8a15b3dd8e7ee099f7f9c96ba"
    url = "https://www.virustotal.com/vtapi/v2/url/report"

    headers = {
        "accept": "application/json",
        "content-type": "multipart/form-data"
    }
    params = {"apikey": api_key, "resource":site1 }
    response = requests.get(url, params=params)
    response_json = json.loads(response.content)
    a=response_json["positives"]
    b=int(a)
    return render_template('result.html', positives=b)






if __name__ ==  "__main__":
    app.run(debug=True)