while True:
    import sys
    import time
    '''
    sys.path.append('~/Documents/deployment-base/client-01/utility/')
    sys.path.append('~/Documents/deployment-base/client-02/utility/')
    sys.path.append('~/Documents/deployment-base/client-03/utility/')
    sys.path.append('~/Documents/deployment-base/client-04/utility/')
    sys.path.append('~/Documents/deployment-base/client-05/utility/')'''

    import vote_counter_client1, vote_counter_client2, vote_counter_client3, vote_counter_client4, vote_counter_client5, vote_counter_client6, vote_counter_client7

    f = open('total_vote_count.csv', 'w')
    f.truncate()
    f.close()

    vote_counter_client1.voteCount()
    vote_counter_client2.voteCount()
    vote_counter_client3.voteCount()
    vote_counter_client4.voteCount()
    vote_counter_client5.voteCount()
    vote_counter_client6.voteCount()
    vote_counter_client7.voteCount()

    print ("vote count works")

    from operator import add
    import csv

    dataFile='total_vote_count.csv'
    def csvWriter(data, filename):
        with open(filename, 'a') as csvfileW:
            writerObject=csv.writer(csvfileW)
            writerObject.writerow(data)

    all_votes=[]
    with open('../../client-01/data/voteagg_db.csv', 'r') as csvfileR:
    	readerObject=csv.reader(csvfileR)
    	for row in readerObject:
    		if row==[]: continue
    		else:
    			all_votes.append(list(map(int, row)))

    #print (all_votes)
    def voteCountOthers(filename):
    	with open(filename, 'r') as csvfileR:
    		readerObject=csv.reader(csvfileR)
    		i=-1
    		for row in readerObject:
    			if row==[]: continue
    			else:
    				i+=1
    				#print (all_votes[i], row)
    				all_votes[i]=list(map(add, all_votes[i], list(map(int,row))))

    #print ("next func works")
    voteCountOthers('../../client-02/data/voteagg_db.csv')
    voteCountOthers('../../client-03/data/voteagg_db.csv')
    voteCountOthers('../../client-04/data/voteagg_db.csv')
    voteCountOthers('../../client-05/data/voteagg_db.csv')
    voteCountOthers('../../client-06/data/voteagg_db.csv')
    voteCountOthers('../../client-07/data/voteagg_db.csv')
    
    for post in all_votes:
    	if post==[]: continue
    	else:
    		csvWriter(post, dataFile)

    time.sleep(5)
