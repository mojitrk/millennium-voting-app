import csv
import time

workFile = 'db/cacheAgg_db.csv'
c_1_file = '../client-01/data/cache_db.csv'
c_2_file = '../client-02/data/cache_db.csv'
c_3_file = '../client-03/data/cache_db.csv'
c_4_file = '../client-04/data/cache_db.csv'
c_5_file = '../client-05/data/cache_db.csv'

while True:
    f = open(workFile, 'w')
    f.truncate()
    f.close()

    def csvFileWriter(data, filename):
        with open(filename, 'a') as csvfileW:
            writerObject=csv.writer(csvfileW)
            writerObject.writerow(data)

    def csvFileReader(file):
        with open(file) as csvfileR:
            readCSV = csv.reader(csvfileR)
            forfeitUSN = []
            for row in readCSV:
                if row==[]: continue
                csvFileWriter(row, workFile)

    csvFileReader(c_1_file)
    csvFileReader(c_2_file)
    csvFileReader(c_3_file)
    csvFileReader(c_4_file)
    csvFileReader(c_5_file)

    time.sleep(5)
