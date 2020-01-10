#NEEDS TO WORK FOR MULTIPLE FILES ACROSS MULTIPLE CLIENTS
#1>> make a shared aggregate file
#2>> simple_dash

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
    with open('vote_count_prgms/total_vote_count.csv') as csvR:
        csvReader=csv.reader(csvR)
        i=0
        for row in csvReader:
            if row==[]: continue
            i+=1
            if i==1:
                SPL_B_0 = 'Sameer'
                SPL_B_VOTE_0 = row[0]
                SPL_B_1 = 'Nikhil'
                SPL_B_VOTE_1 = row[1]
                SPL_B_2 = 'Yash'
                SPL_B_VOTE_2 = row[2]
            if i==2:
                SPL_G_0 = 'Sanjana'
                SPL_G_VOTE_0 = row[0]
                SPL_G_1 = 'Parvani'
                SPL_G_VOTE_1 = row[1]
                SPL_G_2 = 'Bhavana'
                SPL_G_VOTE_2 = row[2]
            if i==3:
                CS_B_0 = 'Afzal'
                CS_B_VOTE_0 = row[0]
                CS_B_1 = 'Srinidhih'
                CS_B_VOTE_1 = row[1]
                CS_B_2 = 'Sai Adhitya'
                CS_B_VOTE_2 = row[2]
            if i==4:
                CS_G_0 = 'Kanimita'
                CS_G_VOTE_0 = row[0]
                CS_G_1 = 'Teena'
                CS_G_VOTE_1 = row[1]
                CS_G_2 = 'Manasa'
                CS_G_VOTE_2 = row[2]
                CS_G_3 = 'Praneetha'
                CS_G_VOTE_3 = row[3]
                CS_G_4 = 'Aishwarya'
                CS_G_VOTE_4 = row[4]
            if i==5:
                SS_B_0 = 'Alfred'
                SS_B_VOTE_0 = row[0]
                SS_B_1 = 'Akhilesh'
                SS_B_VOTE_1 = row[1]
                SS_B_2 = 'Anantha'
                SS_B_VOTE_2 = row[2]
            if i==6:
                SS_G_0 = 'Varshaa'
                SS_G_VOTE_0 = row[0]
                SS_G_1 = 'Neha D'
                SS_G_VOTE_1 = row[1]
            if i==7:
                ASPL_B_0 = 'Dheeraj'
                ASPL_B_VOTE_0 = row[0]
                ASPL_B_1 = 'Thiru Kathir'
                ASPL_B_VOTE_1 = row[1]
                ASPL_B_2 = 'Shanthanu'
                ASPL_B_VOTE_2 = row[2]
            #from_here_name_required
            if i==8:
                ASPL_G_0 = 'S Riya'
                ASPL_G_VOTE_0 = row[0]
                ASPL_G_1 = 'Aparna R'
                ASPL_G_VOTE_1 = row[1]
                ASPL_G_2 = 'Harshini Vijayan'
                ASPL_G_VOTE_2 = row[2]
                ASPL_G_3 = 'Neha Yuvraj'
                ASPL_G_VOTE_3 = row[3]
                ASPL_G_4 = 'Smriti Maheshwari'
                ASPL_G_VOTE_4 = row[4]
            if i==9:
                ACS_B_0 = 'Sankruth Sharma'
                ACS_B_VOTE_0 = row[0]
                ACS_B_1 = 'Saathvik B'
                ACS_B_VOTE_1 = row[1]
                ACS_B_2 = 'Harikrishnaa'
                ACS_B_VOTE_2 = row[2]
            if i==10:
                ACS_G_0 = 'Srinidhi B'
                ACS_G_VOTE_0 = row[0]
                ACS_G_1 = 'Aishwarya Ramachandra'
                ACS_G_VOTE_1 = row[1]
                ACS_G_2 = 'Dharshini SS'
                ACS_G_VOTE_2 = row[2]
                ACS_G_3 = 'Advika RA'
                ACS_G_VOTE_3 = row[3]
            if i==11:
                ASS_B_0 = 'Hari Shankar VS'
                ASS_B_VOTE_0 = row[0]
                ASS_B_1 = 'Balaji Ravi'
                ASS_B_VOTE_1 = row[1]
                ASS_B_2 = 'Dheexshan'
                ASS_B_VOTE_2 = row[2]
                ASS_B_3 = 'Annirudh RA'
                ASS_B_VOTE_3 = row[3]
            if i==12:
                ASS_G_0 = 'Anika Pandey'
                ASS_G_VOTE_0 = row[0]
                ASS_G_1 = 'Shamita'
                ASS_G_VOTE_1 = row[1]
                ASS_G_2 = 'Akshara NK'
                ASS_G_VOTE_2 = row[2]
                ASS_G_3 = 'Yuvashree Magesh'
                ASS_G_VOTE_3 = row[3]
            if i==13:
                IC_P_0 = 'Harshita Balaji'
                IC_P_VOTE_0 = row[0]
                IC_P_1 = 'Shivani SI'
                IC_P_VOTE_1 = row[1]
                IC_P_2 = 'Srirangan S'
                IC_P_VOTE_2 = row[2]
            if i==14:
                IC_VP_0 = 'Nethra'
                IC_VP_VOTE_0 = row[0]
                IC_VP_1 = 'Tarun'
                IC_VP_VOTE_1 = row[1]
            if i==15:
                IC_S_0 = 'Sibi Rassal'
                IC_S_VOTE_0 = row[0]
                IC_S_1 = 'Pranav S'
                IC_S_VOTE_1 = row[1]
            if i==16:
                IC_T_0 = 'Bharat Rajesh'
                IC_T_VOTE_0 = row[0]
                IC_T_1 = 'S Vishal'
                IC_T_VOTE_1 = row[1]
    return render_template('admin/simple_post_info.html', SPL_B_0=SPL_B_0, SPL_B_VOTE_0=SPL_B_VOTE_0,
                                                          SPL_B_1=SPL_B_1, SPL_B_VOTE_1=SPL_B_VOTE_1,
                                                          SPL_B_2=SPL_B_2, SPL_B_VOTE_2=SPL_B_VOTE_2,

                                                          SPL_G_0=SPL_G_0, SPL_G_VOTE_0=SPL_G_VOTE_0,
                                                          SPL_G_1=SPL_G_1, SPL_G_VOTE_1=SPL_G_VOTE_1,
                                                          SPL_G_2=SPL_G_2, SPL_G_VOTE_2=SPL_G_VOTE_2,

                                                          ASPL_B_0=ASPL_B_0, ASPL_B_VOTE_0=ASPL_B_VOTE_0,
                                                          ASPL_B_1=ASPL_B_1, ASPL_B_VOTE_1=ASPL_B_VOTE_1,
                                                          ASPL_B_2=ASPL_B_2, ASPL_B_VOTE_2=ASPL_B_VOTE_2,

                                                          ASPL_G_0=ASPL_G_0, ASPL_G_VOTE_0=ASPL_G_VOTE_0,
                                                          ASPL_G_1=ASPL_G_1, ASPL_G_VOTE_1=ASPL_G_VOTE_1,
                                                          ASPL_G_2=ASPL_G_2, ASPL_G_VOTE_2=ASPL_G_VOTE_2,
                                                          ASPL_G_3=ASPL_G_3, ASPL_G_VOTE_3=ASPL_G_VOTE_3,
                                                          ASPL_G_4=ASPL_G_4, ASPL_G_VOTE_4=ASPL_G_VOTE_4,

                                                          CS_B_0=CS_B_0, CS_B_VOTE_0=CS_B_VOTE_0,
                                                          CS_B_1=CS_B_1, CS_B_VOTE_1=CS_B_VOTE_1,
                                                          CS_B_2=CS_B_2, CS_B_VOTE_2=CS_B_VOTE_2,

                                                          CS_G_0=CS_G_0, CS_G_VOTE_0=CS_G_VOTE_0,
                                                          CS_G_1=CS_G_1, CS_G_VOTE_1=CS_G_VOTE_1,
                                                          CS_G_2=CS_G_2, CS_G_VOTE_2=CS_G_VOTE_2,
                                                          CS_G_3=CS_G_3, CS_G_VOTE_3=CS_G_VOTE_3,
                                                          CS_G_4=CS_G_4, CS_G_VOTE_4=CS_G_VOTE_4,

                                                          ACS_B_0=ACS_B_0, ACS_B_VOTE_0=ACS_B_VOTE_0,
                                                          ACS_B_1=ACS_B_1, ACS_B_VOTE_1=ACS_B_VOTE_1,
                                                          ACS_B_2=ACS_B_2, ACS_B_VOTE_2=ACS_B_VOTE_2,

                                                          ACS_G_0=ACS_G_0, ACS_G_VOTE_0=ACS_G_VOTE_0,
                                                          ACS_G_1=ACS_G_1, ACS_G_VOTE_1=ACS_G_VOTE_1,
                                                          ACS_G_2=ACS_G_2, ACS_G_VOTE_2=ACS_G_VOTE_2,
                                                          ACS_G_3=ACS_G_3, ACS_G_VOTE_3=ACS_G_VOTE_3,

                                                          SS_B_0=SS_B_0, SS_B_VOTE_0=SS_B_VOTE_0,
                                                          SS_B_1=SS_B_1, SS_B_VOTE_1=SS_B_VOTE_1,
                                                          SS_B_2=SS_B_2, SS_B_VOTE_2=SS_B_VOTE_2,

                                                          SS_G_0=SS_G_0, SS_G_VOTE_0=SS_G_VOTE_0,
                                                          SS_G_1=SS_G_1, SS_G_VOTE_1=SS_G_VOTE_1,

                                                          ASS_B_0=ASS_B_0, ASS_B_VOTE_0=ASS_B_VOTE_0,
                                                          ASS_B_1=ASS_B_1, ASS_B_VOTE_1=ASS_B_VOTE_1,
                                                          ASS_B_2=ASS_B_2, ASS_B_VOTE_2=ASS_B_VOTE_2,
                                                          ASS_B_3=ASS_B_3, ASS_B_VOTE_3=ASS_B_VOTE_3,

                                                          ASS_G_0=ASS_G_0, ASS_G_VOTE_0=ASS_G_VOTE_0,
                                                          ASS_G_1=ASS_G_1, ASS_G_VOTE_1=ASS_G_VOTE_1,
                                                          ASS_G_2=ASS_G_2, ASS_G_VOTE_2=ASS_G_VOTE_2,
                                                          ASS_G_3=ASS_G_3, ASS_G_VOTE_3=ASS_G_VOTE_3,

                                                          IC_P_0=IC_P_0, IC_P_VOTE_0=IC_P_VOTE_0,
                                                          IC_P_1=IC_P_1, IC_P_VOTE_1=IC_P_VOTE_1,
                                                          IC_P_2=IC_P_2, IC_P_VOTE_2=IC_P_VOTE_2,

                                                          IC_S_0=IC_S_0, IC_S_VOTE_0=IC_S_VOTE_0,
                                                          IC_S_1=IC_S_1, IC_S_VOTE_1=IC_S_VOTE_1,

                                                          IC_VP_0=IC_VP_0, IC_VP_VOTE_0=IC_VP_VOTE_0,
                                                          IC_VP_1=IC_VP_1, IC_VP_VOTE_1=IC_VP_VOTE_1,

                                                          IC_T_0=IC_T_0, IC_T_VOTE_0=IC_T_VOTE_0,
                                                          IC_T_1=IC_T_1, IC_T_VOTE_1=IC_T_VOTE_1)


@adminApp.route('/simple-dash', methods=['POST', 'GET'])
def simpleDash():
    return render_template('admin/simple_dash.html')

@adminApp.route('/simple-dash-data', methods=['POST', 'GET'])
def simpleDashData():
    #code
    with open('vote_count_prgms/total_vote_count.csv') as csvR:
        csvReader=csv.reader(csvR)
        i = 0
        for row in csvReader:
            if row==[]: continue
            i+=1
            cacheRow = []
            for item in row:
                cacheRow.append(int(item))
            high = max(cacheRow)
            ind = row.index(str(high))
            if i == 1:
                post = "School Pupil Leader"
                SPL_B_VOTE = high
                if ind == 0: SPL_B = "Sameer"
                elif ind == 1: SPL_B = "Nikhil"
                elif ind == 2: SPL_B = "Yash"
            elif i == 2:
                post = "SPL_G"
                SPL_G_VOTE = high
                if ind == 0: SPL_G = "Sanjana"
                if ind == 1: SPL_G = "Parvani"
                if ind == 2: SPL_G = "Bhavana"
            elif i == 3:
                post = "CS_B"
                CS_B_VOTE = high
                if ind == 0: CS_B = "Afzal"
                if ind == 1: CS_B = "Srinidhih"
                if ind == 2: CS_B = "Sai Adhitya"
            elif i == 4:
                post = "CS_G"
                CS_G_VOTE = high
                if ind == 0: CS_G = "Kanimita"
                if ind == 1: CS_G = "Teena"
                if ind == 2: CS_G = "Manasa"
                if ind == 3: CS_G = "Praneetha"
                if ind == 4: CS_G = "Aishwarya"
            elif i == 5:
                post = "SS_B"
                SS_B_VOTE = high
                if ind == 0: SS_B = "Alfred"
                if ind == 1: SS_B = "Akhilesh"
                if ind == 2: SS_B = "Anantha"
            elif i == 6:
                post = "SS_G"
                SS_G_VOTE = high
                if ind == 0: SS_G = "Varshaa"
                if ind == 1: SS_G = "Neha"
            elif i == 7:
                post = "ASPL_B"
                ASPL_B_VOTE = high
                if ind == 0: ASPL_B = "Dheeraj"
                if ind == 1: ASPL_B = "Thiru Kathir"
                if ind == 2: ASPL_B = "Shanthanu"
            #CHANGE
            elif i == 8:
                post = "ASPL_G"
                ASPL_G_VOTE = high
                if ind == 0: ASPL_G = "S Riya"
                if ind == 1: ASPL_G = "Aparna R"
                if ind == 2: ASPL_G = "Harshini Vijayan"
                if ind == 3: ASPL_G = "Neha Yuvaraj"
                if ind == 4: ASPL_G = "Smriti Maheshwari"
            elif i == 9:
                post = "ACS_B"
                ACS_B_VOTE = high
                if ind == 0: ACS_B = "Sankruth Sharma"
                if ind == 1: ACS_B = "Saathvik B"
                if ind == 2: ACS_B = "Harikrishnaa"
            elif i == 10:
                post = "ACS_G"
                ACS_G_VOTE = high
                if ind == 0: ACS_G = "Srinidhi B"
                if ind == 1: ACS_G = "Aishwarya Ramachandra"
                if ind == 2: ACS_G = "Dharshini SS"
                if ind == 3: ACS_G = "Advika RA"
            elif i == 11:
                post = "ASS_B"
                ASS_B_VOTE = high
                if ind == 0: ASS_B = "Hari Shankar VS"
                if ind == 1: ASS_B = "Balaji Ravi"
                if ind == 2: ASS_B = "Dheexshan"
                if ind == 3: ASS_B = "Annirudh RA"
            elif i == 12:
                post = "ASS_G"
                ASS_G_VOTE = high
                if ind == 0: ASS_G = "Anika Pandey"
                if ind == 1: ASS_G = "Shamita"
                if ind == 2: ASS_G = "Akshara NK"
                if ind == 3: ASS_G = "Yuvashree Magesh"
            elif i == 13:
                post = "IN_PRES"
                IN_PRES_VOTE = high
                if ind == 0: IN_PRES = "Harshita Balaji"
                if ind == 1: IN_PRES = "Shivani SI"
                if ind == 2: IN_PRES = "Srirangan S"
            elif i == 14:
                post = "IN_VPRES"
                IN_VPRES_VOTE = high
                if ind == 0: IN_VPRES = "Nethra"
                if ind == 1: IN_VPRES = "Tarun"
            elif i == 15:
                post = "IN_SEC"
                IN_SEC_VOTE = high
                if ind == 0: IN_SEC = "Sibi Rassal"
                if ind == 1: IN_SEC = "Pranav S"
            elif i == 16:
                post = "IN_TRES"
                IN_TRES_VOTE = high
                if ind == 0: IN_TRES = "Bharat Rajesh"
                if ind == 1: IN_TRES = "S Vishal"
    return render_template('admin/simple_dash.html', SPL_B=SPL_B, SPL_B_VOTE=SPL_B_VOTE,
                                                     SPL_G=SPL_G, SPL_G_VOTE=SPL_G_VOTE,
                                                     CS_G=CS_G, CS_G_VOTE=CS_G_VOTE,
                                                     CS_B=CS_B, CS_B_VOTE=CS_B_VOTE,
                                                     SS_B=SS_B, SS_B_VOTE=SS_B_VOTE,
                                                     SS_G=SS_G, SS_G_VOTE=SS_G_VOTE,
                                                     ASPL_B=SPL_B, ASPL_B_VOTE=SPL_B_VOTE,
                                                     ASPL_G=SPL_G, ASPL_G_VOTE=SPL_G_VOTE,
                                                     ACS_G=CS_G, ACS_G_VOTE=CS_G_VOTE,
                                                     ACS_B=CS_B, ACS_B_VOTE=CS_B_VOTE,
                                                     ASS_B=SS_B, ASS_B_VOTE=SS_B_VOTE,
                                                     ASS_G=SS_G, ASS_G_VOTE=SS_G_VOTE,
                                                     IN_PRES=IN_PRES, IN_PRES_VOTE=IN_PRES_VOTE,
                                                     IN_VPRES=IN_VPRES, IN_VPRES_VOTE=IN_VPRES_VOTE,
                                                     IN_SEC=IN_SEC, IN_SEC_VOTE=IN_SEC_VOTE,
                                                     IN_TRES=IN_TRES, IN_TRES_VOTE=IN_TRES_VOTE)

#app_init
if __name__ == '__main__':
    adminApp.run(host='192.168.5.1' , port=2427, debug=True)
