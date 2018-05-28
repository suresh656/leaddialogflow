from flask import Flask, render_template, jsonify, request
#from werkzeug.wrappers import Request, Response
import re
#import json
#from pprint import pprint

app =Flask(__name__)

#@Request.application
#def application(request):
#    return Response('Hello World!')
#
#
@app.route('/plot/')
def plot():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, output_file, show
    from bokeh.embed import components
    from bokeh.resources import CDN

    start=datetime.datetime(2016,10,1)
    end=datetime.datetime(2017,3,10)

    df=data.DataReader(name="GOOG",data_source="google",start=start,end=end)

    df_bull=df[df.Close>=df.Open]
    df_bear=df[df.Open>df.Close]

    p=figure(x_axis_type='datetime', height=300, width=1000,title='Candlestick Chart',sizing_mode='scale_width')
    #p.grid.grid_line_alpha=0.5
#hi
    hours_12=12*60*60*1000

    p.segment(df.index, df.High, df.index, df.Low, color='black')
    p.rect(x=df_bull.index,y=((df_bull.Open+df_bull.Close)/2),
           width=hours_12,height=abs(df_bull.Close-df_bull.Open),color='#CCFFFF',line_color='black')

    p.rect(x=df_bear.index,y=((df_bear.Open+df_bear.Close)/2),
           width=hours_12,height=abs(df_bear.Open-df_bear.Close),color='#FF3333',line_color='black')

    script1,div1=components(p)
    cdn_js=CDN.js_files[0]
    cdn_css=CDN.css_files[0]
    return render_template("plot.html",
    script1=script1, div1=div1,cdn_css=cdn_css,cdn_js=cdn_js)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/ome/',methods=["GET"])
def geti():
    resp = {"username": "kkk"}
    return jsonify(resp)

@app.route('/ost/',methods=["POST"])
def posti():
    responseId = request.json["responseId"]
    req = request.json
    for header in req:
        if header == "queryResult":
            for item in req[header]:
                if item == "intent":
                    for option in req[header][item]:
                        if option == "displayName":
                            if req[header][item][option] == "askmobile":
                                for itm in req[header]:
                                    if itm == "parameters":
                                        for para in req[header][itm]:
                                            if para == "mobileNumber":
                                                p = re.compile(r'^[6789]\d{9}$',re.I|re.M)
                                                print (req[header][itm][para])
                                                if p.match(str(req[header][itm][para])):
                                                    respo = {"fulfillmentText": "Please enter the OTP received","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {"name": "otp"}}
                                                    return jsonify(respo)
                                                else:
                                                    respo = {"fulfillmentText": "Please enter a valid 10 digit mobile number","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {"name": "mobile"}}
                                                    return jsonify(respo)
                            elif req[header][item][option] == "askmobile - fallback":
                                 respo = {"fulfillmentText": "","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {"name": "mobile"}}
                                 return jsonify(respo)
                            elif req[header][item][option] == "askotp":
                                for itm in req[header]:
                                    if itm == "parameters":
                                        for para in req[header][itm]:
                                            if para == "otp":
                                                p = re.compile(r'^\d{6}$',re.I|re.M)
                                                print (req[header][itm][para])
                                                if p.match(str(req[header][itm][para])):
                                                    respo = {"fulfillmentText": "Otp verified Sucessfully, What are you Looking for?Apply Loan,Track loan status,raise Service request","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {}}
                                                    return jsonify(respo)
                                                else:
                                                    respo = {"fulfillmentText": "Please enter a valid 6 digits OTP sent to your mobile number","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {}}
                                                    return jsonify(respo)
                            elif req[header][item][option] == "askotp - fallback":
                                 respo = {"fulfillmentText": "","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {"name": "otp"}}
                                 return jsonify(respo)
                            elif req[header][item][option] == "applyloan":
                                 respo = {"fulfillmentText": "","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {"name": "fname"}}
                                 return jsonify(respo)
                            elif req[header][item][option] == "applyloan - fname":
                                for itm in req[header]:
                                    if itm == "parameters":
                                        for para in req[header][itm]:
                                            if para == "otp":
                                                p = re.compile(r'^\d{6}$',re.I|re.M)
                                                print (req[header][itm][para])
                                                if p.match(str(req[header][itm][para])):
                                                    respo = {"fulfillmentText": "Otp verified Sucessfully, What are you Looking for?Apply Loan,Track loan status,raise Service request","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {}}
                                                    return jsonify(respo)
                                                else:
                                                    respo = {"fulfillmentText": "Please enter a valid 6 digits OTP sent to your mobile number","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {}}
                                                    return jsonify(respo)
                            elif req[header][item][option] == "applyloan - lname":
                                for itm in req[header]:
                                    if itm == "parameters":
                                        for para in req[header][itm]:
                                            if para == "otp":
                                                p = re.compile(r'^\d{6}$',re.I|re.M)
                                                print (req[header][itm][para])
                                                if p.match(str(req[header][itm][para])):
                                                    respo = {"fulfillmentText": "Otp verified Sucessfully, What are you Looking for?Apply Loan,Track loan status,raise Service request","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {}}
                                                    return jsonify(respo)
                                                else:
                                                    respo = {"fulfillmentText": "Please enter a valid 6 digits OTP sent to your mobile number","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {}}
                                                    return jsonify(respo)
                            elif req[header][item][option] == "applyloan - pincode":
                                for itm in req[header]:
                                    if itm == "parameters":
                                        for para in req[header][itm]:
                                            if para == "otp":
                                                p = re.compile(r'^\d{6}$',re.I|re.M)
                                                print (req[header][itm][para])
                                                if p.match(str(req[header][itm][para])):
                                                    respo = {"fulfillmentText": "Otp verified Sucessfully, What are you Looking for?Apply Loan,Track loan status,raise Service request","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {}}
                                                    return jsonify(respo)
                                                else:
                                                    respo = {"fulfillmentText": "Please enter a valid 6 digits OTP sent to your mobile number","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {}}
                                                    return jsonify(respo)
                            elif req[header][item][option] == "isNewVehicle":
                                 respo = {"fulfillmentText": "Lead creation successful! Lead ID 149875 has been assigned to this SFE,he will contact you further. ","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {}}
                                 return jsonify(respo)
                            respo = {"fulfillmentText": "This is not greeting intent","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {}}
                            return jsonify(respo)
    #session = request.json["session"]
    #querytext = request.json["querytext"]
    #mobilenumber = request.json["mobilenumber"]


@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/policy/')
def policy():
    return render_template("policy.html")

if __name__ == "__main__":
    app.run(debug=True)
    #from werkzeug.serving import run_simple
    #run_simple('localhost', 4000, application)
