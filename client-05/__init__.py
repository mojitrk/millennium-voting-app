from flask import Flask, render_template, request, url_for, redirect
from flask import flash
import csv

#flask_app_declaration
baseApp = Flask(__name__, static_folder = 'static', template_folder='templates')
baseApp.config['SECRET_KEY']= 'sdfvbukjfn738uif78g2ne8ivb78er'

#external_file_declarations
baseFile = '../client-master/db/valid_db.csv'
cacheFile = 'data/cache_db.csv'
dataFile = 'data/data_cache.csv'
forfeitFile = 'data/forfeit_db.csv'
sharedCacheFile = '../client-master/db/cacheAgg_db.csv'

global getPollVal

#csv_file_interact_function
def csvWriter(data, filename):
    with open(filename, 'a') as csvfileW:
        writerObject=csv.writer(csvfileW)
        writerObject.writerow(data)

#csv_file_interact_function
def csvWriterSTRING(data, filename):
    with open(filename, 'a') as csvfileWSTR:
        csvfileWSTR.write(data)

#landing_login_page_render
@baseApp.route('/', methods = ['POST','GET'])
def rootForm():
    return render_template('__login_page.html')

#poll_page
@baseApp.route('/spl-b', methods = ['POST','GET'])
def spl_b():
    return render_template('poll-pages/spl_b.html',title = 'spl_b')

#poll_page
@baseApp.route('/spl-g', methods = ['POST','GET'])
def spl_g():
    if request.method == 'POST':
        if 'name1' in request.form: getPollVal='1'
        if 'name2' in request.form: getPollVal='2'
        if 'name3' in request.form: getPollVal='3'
        csvWriter(getPollVal, dataFile)
    return render_template('poll-pages/spl_g.html', title = 'spl_g')

#poll_page
@baseApp.route('/cs-b',methods=['POST','GET'])
def cs_b():
    if request.method == 'POST':
        if 'name1' in request.form: getPollVal='1'
        if 'name2' in request.form: getPollVal='2'
        if 'name3' in request.form: getPollVal='3'
        csvWriter(getPollVal, dataFile)
    return render_template('poll-pages/cs_b.html', title = 'cs_b')

#poll_page
@baseApp.route('/cs-g',methods=['POST','GET'])
def cs_g():
    if request.method == 'POST':
        if 'name1' in request.form: getPollVal='1'
        if 'name2' in request.form: getPollVal='2'
        if 'name3' in request.form: getPollVal='3'
        csvWriter(getPollVal, dataFile)
    return render_template('poll-pages/cs_g.html', title = 'cs_g')

#poll_page
@baseApp.route('/ss-b',methods=['POST','GET'])
def ss_b():
    if request.method == 'POST':
        if 'name1' in request.form: getPollVal='1'
        if 'name2' in request.form: getPollVal='2'
        if 'name3' in request.form: getPollVal='3'
        if 'name4' in request.form: getPollVal='4'
        if 'name5' in request.form: getPollVal='5'
        csvWriter(getPollVal, dataFile)
    return render_template('poll-pages/ss_b.html', title = 'ss_b')

#poll_page
@baseApp.route('/ss-g',methods=['POST','GET'])
def ss_g():
    if request.method == 'POST':
        if 'name1' in request.form: getPollVal='1'
        if 'name2' in request.form: getPollVal='2'
        if 'name3' in request.form: getPollVal='3'
        csvWriter(getPollVal, dataFile)
    return render_template('poll-pages/ss_g.html', title = 'ss_g')

#poll_page
@baseApp.route('/aspl-b',methods=['POST','GET'])
def aspl_b():
    if request.method == 'POST':
        if 'name1' in request.form: getPollVal='1'
        if 'name2' in request.form: getPollVal='2'
        csvWriter(getPollVal, dataFile)
    return render_template('poll-pages/aspl_b.html', title = 'aspl_b')

#poll_page
@baseApp.route('/aspl-g',methods=['POST','GET'])
def aspl_g():
    if request.method == 'POST':
        if 'name1' in request.form: getPollVal='1'
        if 'name2' in request.form: getPollVal='2'
        if 'name3' in request.form: getPollVal='3'
        csvWriter(getPollVal, dataFile)
    return render_template('poll-pages/aspl_g.html', title = 'aspl_g')

#poll_page
@baseApp.route('/acs-b',methods=['POST','GET'])
def acs_b():
    if request.method == 'POST':
        if 'name1' in request.form: getPollVal='1'
        if 'name2' in request.form: getPollVal='2'
        if 'name3' in request.form: getPollVal='3'
        if 'name4' in request.form: getPollVal='4'
        if 'name5' in request.form: getPollVal='5'
        csvWriter(getPollVal, dataFile)
    return render_template('poll-pages/acs_b.html', title = 'acs_b')

#poll_page
@baseApp.route('/acs-g',methods=['POST','GET'])
def acs_g():
    if request.method == 'POST':
        if 'name1' in request.form: getPollVal='1'
        if 'name2' in request.form: getPollVal='2'
        if 'name3' in request.form: getPollVal='3'
        csvWriter(getPollVal, dataFile)
    return render_template('poll-pages/acs_g.html', title = 'acs_g')

#poll_page
@baseApp.route('/ass-b',methods=['POST','GET'])
def ass_b():
    if request.method == 'POST':
        if 'name1' in request.form: getPollVal='1'
        if 'name2' in request.form: getPollVal='2'
        if 'name3' in request.form: getPollVal='3'
        if 'name4' in request.form: getPollVal='4'
        csvWriter(getPollVal, dataFile)
    return render_template('poll-pages/ass_b.html', title = 'ass_b')

#poll_page
@baseApp.route('/ass-g',methods=['POST','GET'])
def ass_g():
    if request.method == 'POST':
        if 'name1' in request.form: getPollVal='1'
        if 'name2' in request.form: getPollVal='2'
        if 'name3' in request.form: getPollVal='3'
        if 'name4' in request.form: getPollVal='4'
        csvWriter(getPollVal, dataFile)
    return render_template('poll-pages/ass_g.html', title = 'ass_g')

#poll_page
@baseApp.route('/in-pres',methods=['POST','GET'])
def in_pres():
    if request.method == 'POST':
        if 'name1' in request.form: getPollVal='1'
        if 'name2' in request.form: getPollVal='2'
        if 'name3' in request.form: getPollVal='3'
        if 'name4' in request.form: getPollVal='4'
        csvWriter(getPollVal, dataFile)
    return render_template('poll-pages/in_pres.html', title = 'President')

#poll_page
@baseApp.route('/in-vpres',methods=['POST','GET'])
def in_vpres():
    if request.method == 'POST':
        if 'name1' in request.form: getPollVal='1'
        if 'name2' in request.form: getPollVal='2'
        if 'name3' in request.form: getPollVal='3'
        csvWriter(getPollVal, dataFile)
    return render_template('poll-pages/in_vpres.html', title = 'Vice President')

#poll_page
@baseApp.route('/in-sec',methods=['POST','GET'])
def in_sec():
    if request.method == 'POST':
        if 'name1' in request.form: getPollVal='1'
        if 'name2' in request.form: getPollVal='2'
        csvWriter(getPollVal, dataFile)
    return render_template('poll-pages/in_sec.html', title = 'Secretary')

#poll_page
@baseApp.route('/in-tres',methods=['POST','GET'])
def in_tres():
    if request.method == 'POST':
        if 'name1' in request.form: getPollVal='1'
        if 'name2' in request.form: getPollVal='2'
        csvWriter(getPollVal, dataFile)
    return render_template('poll-pages/in_tres.html', title = 'Treasurer')

#login_request_handler
@baseApp.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        getKey = request.form['pwd']
        #staff_vote
        if getKey == 'passteach':
            f = open(dataFile, 'w')
            f.truncate()
            f.close()
            csvWriterSTRING(getKey, dataFile)
            csvWriter('', dataFile)
            return redirect(url_for('forfeitOption'))
        f=open('data/usn_cache.txt','w')
        f.write(getKey)
        f.close()
        with open(sharedCacheFile) as csvfileR:
            readCSV = csv.reader(csvfileR, delimiter=',')
            cacheUSN = []
            for row in readCSV:
                if row==[]: continue
                cacheUSN.append(row[0])
        if getKey in cacheUSN:
            flash('You have already voted!!!')
            return redirect(url_for('rootForm'))
        else:
            with open(forfeitFile) as csvfileR:
                readCSV = csv.reader(csvfileR, delimiter=',')
                forfeitUSN = []
                for row in readCSV:
                    if row==[]: continue
                    forfeitUSN.append(row[0])
            if getKey in forfeitUSN:
                flash('You have forfeited!!')
                return redirect(url_for('rootForm'))
            f = open(dataFile, 'w')
            f.truncate()
            f.close()
            with open(baseFile) as csvfileBase:
                baseUSN=[]
                baseName=[]
                readBaseCSV = csv.reader(csvfileBase, delimiter=',')
                for baseRow in readBaseCSV:
                    baseUSN.append(str(baseRow[0]))
                    baseName.append(str(baseRow[1]))
            for i in range(len(baseUSN)):
                if getKey==baseUSN[i]:
                    csvWriterSTRING(getKey, dataFile)
                    csvWriter('', dataFile)
                    flash(baseName[i]+' IS LOGGED IN')
                    return redirect(url_for('forfeitOption'))
            else:
                flash('Wrong USN!!!')
                return redirect(url_for('rootForm'))

#forfeit_option_render
@baseApp.route('/forfeit-option', methods=['POST','GET'])
def forfeitOption():
    return render_template('forfeit_option_page.html')

#poll_end_page
@baseApp.route('/thank-you',methods=['POST','GET']) # need to modify
def thank():
    if request.method == 'POST':
        try:
            req=request.form['critical_act']
            if req=='forfeit':
                f=open('data/usn_cache.txt','r')
                usnEntered=None
                for line in f:
                    line=line.strip('\n')
                    usnEntered=line
                csvWriterSTRING(usnEntered, forfeitFile)
                csvWriterSTRING('\n', forfeitFile)
                return render_template('thank_you.html')
        except:
            if 'name1' in request.form: getPollVal='1'
            if 'name2' in request.form: getPollVal='2'
            csvWriter(getPollVal, dataFile)
            with open(dataFile) as datafileR:
                readdataCSV = csv.reader(datafileR, delimiter=',')
                cacheData = []
                for row in readdataCSV:
                    if row==[]: continue
                    cacheData.append(row[0])
            csvWriter(cacheData, cacheFile)
            if(request.form == True):
                return render_template('thank_you.html', title = 'Thank You')
        return render_template('thank_you.html', title = 'Thank You')

#app_init
if __name__ == '__main__':
    baseApp.run(host='192.168.5.1' , port=5000, debug=True)
