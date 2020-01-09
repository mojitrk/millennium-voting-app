from flask import Flask, render_template, request, url_for, redirect
from flask import flash
import csv

#flask_app_declaration
adminApp = Flask(__name__, static_folder = 'static', template_folder='templates')
adminApp.config['SECRET_KEY']= 'sdfvbukjfn738uif78g2ne8ivb78er'

#external_file_declarations
baseFile = 'data/valid_db.csv'
cacheFile = 'data/cache_db.csv'

@adminApp.route('/')
def rootDash():
    return redirect(url_for('simpleDashData'))

@adminApp.route('/simple-post-info')
def postInfo():
    with open('data/voteagg_db.csv') as csvR:
        csvReader=csv.reader(csvR)
        i=0
        for row in csvReader:
            if row==[]: continue
            i+=1
            if i==1:
                SPL_B_0 = 'nikhil'
                SPL_B_VOTE_0 = row[0]
                SPL_B_1 = 'sameer'
                SPL_B_VOTE_1 = row[1]
                SPL_B_2 = 'yash'
                SPL_B_VOTE_2 = row[2]
    return render_template('admin/simple_post_info.html', SPL_B_0=SPL_B_0, SPL_B_VOTE_0=SPL_B_VOTE_0,
                                                          SPL_B_1=SPL_B_1, SPL_B_VOTE_1=SPL_B_VOTE_1,
                                                          SPL_B_2=SPL_B_2, SPL_B_VOTE_2=SPL_B_VOTE_2)

@adminApp.route('/simple-dash', methods=['POST', 'GET'])
def simpleDash():
    return render_template('admin/simple_dash.html')

@adminApp.route('/simple-dash-data', methods=['POST', 'GET'])
def simpleDashData():
    #code
    with open('data/voteagg_db.csv') as csvR:
        csvReader=csv.reader(csvR)
        i = 0
        for row in csvReader:
            if row==[]: continue
            i+=1
            high = max(row)
            ind = row.index(high)
            if i == 1:
                post = "SPL_B"
                SPL_B_VOTE = high
                if ind == 0: SPL_B = "nikhil"
                if ind == 1: SPL_B = "sameer"
                if ind == 2: SPL_B = "yash"
            elif i == 2: post = "SPL_G"
            elif i == 3: post = "CS_B"
            elif i == 4: post = "CS_G"
            elif i == 5: post = "SS_B"
            elif i == 6: post = "SS_G"
            elif i == 7: post = "ASPL_B"
            elif i == 8: post = "ASPL_G"
            elif i == 9: post = "ACS_B"
            elif i == 10: post = "ACS_G"
            elif i == 11: post = "ASS_B"
            elif i == 12: post = "ASS_G"
            elif i == 13: post = "IN_PRES"
            elif i == 14: post = "IN_VPRES"
            elif i == 15: post = "IN_SEC"
            elif i == 16: post = "IN_TRES"
    return render_template('admin/simple_dash.html', SPL_B=SPL_B, SPL_B_VOTE=SPL_B_VOTE)

#app_init
if __name__ == '__main__':
    adminApp.run(host='0.0.0.0' , port=2427, debug=True)
