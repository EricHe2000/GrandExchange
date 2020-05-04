from pyspark import SparkContext

'''
1. Read data in as pairs of (user_id, item_id clicked on by the user)
2. Group data into (user_id, list of item ids they clicked on)
3. Transform into (user_id, (item1, item2) where item1 and item2 are pairs of items the user clicked on
4. Transform into ((item1, item2), list of user1, user2 etc) where users are all the ones who co-clicked (item1, item2)
5. Transform into ((item1, item2), count of distinct users who co-clicked (item1, item2)
6. Filter out any results where less than 3 users co-clicked the same pair of items

'''
sc = SparkContext("spark://spark-master:7077", "PopularItems")
data = sc.textFile("/tmp/data/access.txt", 2)     # each worker loads a piece of the data file
pairs = data.map(lambda line: line.split("\t"))   # tell each worker to split each line of it's partition
output = pairs.collect()                          # collecting all pairs of data, split by the tab

print('End step 1')

usertoListofItems = pairs.groupByKey().mapValues(list)
output = usertoListofItems.collect()
for user_id, list_of_items in output:
    print('User ' + str(user_id) + ' clicked on items ' + str(list_of_items))

print('End step 2')


#use .distinct() so that the same user isn't counted twice
usertoPairs = usertoListofItems.flatMapValues(lambda y: [(y[x], y[x+1]) for x in range(0, len(y)-1)]).distinct()
output = usertoPairs.collect()

for user_id, pairs in output:
    print('User ' + str(user_id) + ' clicked on items ' + str(pairs))

print('end step 3')

itemPairs = usertoPairs.map(lambda x: (x[1], x[0]))
itemPairstoClickedUsers = itemPairs.groupByKey().mapValues(list)

output = itemPairstoClickedUsers.collect()
for item_pair, user_list in output:
    print ("item_pair %s user_list %s" % (str(item_pair), str(user_list)))

print('end of 4')


#again, using .filter() so that pairs of < 3 unique users viewing it are excluded from the results
item_pair_map = itemPairstoClickedUsers.flatMapValues(lambda x: x).map(lambda pair: (pair[0], 1))
count = item_pair_map.reduceByKey(lambda x,y: int(x)+int(y)).filter(lambda x: x[1] >= 3)
output = count.collect()
for item_pair, count in output:
    print ("item_pair %s count %d" % (str(item_pair), count))

print('end of 5 and 6')



'''
pages = pairs.map(lambda pair: (pair[1], 1))      # re-layout the data to ignore the user id
count = pages.reduceByKey(lambda x,y: int(x)+int(y))        # shuffle the data so that each key is only on one worker
                                                  # and then reduce all the values by adding them together

output = count.collect()                          # bring the data back to the master node so we can print it out
for page_id, count in output:
    print ("page_id %s count %d" % (page_id, count))
print ("Popular items done")
'''

sc.stop()