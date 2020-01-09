import csv
import time

def voteCount():

    voteData='../../client-02/data/cache_db.csv'
    voteAggData='../../client-02/data/voteagg_db.csv'

    f = open(voteAggData, 'w')
    f.truncate()
    f.close()
    data={'splb':[], 'splg':[], 'asplb':[], 'asplg':[],
    'csb':[], 'csg':[], 'acsb':[], 'acsg':[],
    'ssb':[], 'ssg':[], 'assb':[], 'assg':[],
    'in_pres':[], 'in_vpres':[], 'in_sec':[], 'in_tres':[]}

    with open(voteData) as csvR:
        csvReader=csv.reader(csvR)
        for row in csvReader:
            if row==[]: continue
            data['splb'].append(row[1])
            data['splg'].append(row[2])
            data['csb'].append(row[3])
            data['csg'].append(row[4])
            data['ssb'].append(row[5])
            data['ssg'].append(row[6])
            data['asplb'].append(row[7])
            data['asplg'].append(row[8])
            data['acsb'].append(row[9])
            data['acsg'].append(row[10])
            data['assb'].append(row[11])
            data['assg'].append(row[12])
            data['in_pres'].append(row[13])
            data['in_vpres'].append(row[14])
            data['in_sec'].append(row[15])
            data['in_tres'].append(row[16])

            #print (data)
    def csvWriter(filename, data):
        with open(filename, 'a') as csvfileW:
            writerObject=csv.writer(csvfileW)
            writerObject.writerow(data)

    def count_vote2(data):
        cand1=data.count('1')
        cand2=data.count('2')
        return list(map(str, [cand1, cand2]))

    def count_vote3(data):
        cand1=data.count('1')
        cand2=data.count('2')
        cand3=data.count('3')
        return list(map(str, [cand1, cand2, cand3]))

    def count_vote4(data):
        cand1=data.count('1')
        cand2=data.count('2')
        cand3=data.count('3')
        cand4=data.count('4')
        return list(map(str,[cand1, cand2, cand3, cand4]))

    def count_vote5(data):
        cand1=data.count('1')
        cand2=data.count('2')
        cand3=data.count('3')
        cand4=data.count('4')
        cand5=data.count('5')
        return list(map(str, [cand1, cand2, cand3, cand4, cand5]))

    csvWriter(voteAggData, count_vote3(data['splb']))
    csvWriter(voteAggData, count_vote3(data['splg']))
    csvWriter(voteAggData, count_vote3(data['csb']))
    csvWriter(voteAggData, count_vote5(data['csg']))
    csvWriter(voteAggData, count_vote3(data['ssb']))
    csvWriter(voteAggData, count_vote2(data['ssg']))
    csvWriter(voteAggData, count_vote3(data['asplb']))
    csvWriter(voteAggData, count_vote5(data['asplg']))
    csvWriter(voteAggData, count_vote3(data['acsb']))
    csvWriter(voteAggData, count_vote4(data['acsg']))
    csvWriter(voteAggData, count_vote4(data['assb']))
    csvWriter(voteAggData, count_vote4(data['assg']))
    csvWriter(voteAggData, count_vote3(data['in_pres']))
    csvWriter(voteAggData, count_vote2(data['in_vpres']))
    csvWriter(voteAggData, count_vote2(data['in_sec']))
    csvWriter(voteAggData, count_vote2(data['in_tres']))
