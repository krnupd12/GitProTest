import json
import datetime
import os
import shutil
from pattern.en import sentiment
from pattern.text.en import positive


def task1():
    print "\n ******* task 1 ******** \n"
    print "Hello World"


def task2():
    print "\n ******* task 2 ******** \n"
    list = [1, 2, 3, 4, 5]
    print list


def task3():
    print("\n ******* task 3 ******** \n")
    items1 = []
    items2 = []
    textfile = open('task3.data', 'r')
    list = textfile.read()

    list = list.split(" ")

    for i in list:
        if (int(i) < 6):
            items1.append(int(i))
        else:
            items2.append(int(i))

    print(items1)
    print(items2)


ex_dir = {'school': 'UAlbany', 'address': '1400 Washington Ave, Albany, NY 12222', 'phone': '(518) 442-3300'}


def task4():
    print("\n ******* task 4 ******** \n")

    for k in ex_dir.keys():
        print(k + ": " + ex_dir[k])


def task5():
    print("\n ******* task 5 ******** \n")

    with open('task5.txt', 'w') as file5:
        json.dump(ex_dir, file5)

    with open('task5.txt', 'r') as file:
        dictdata = json.load(file)

    print(dictdata.keys())
    print(dictdata.items())
    print(dictdata.values())


items = [1, 2, 3, 4, 5]


def task6():
    print("\n ******* task 6 ******** \n")

    with open('task6.txt', 'w') as file6:
        json.dump([ex_dir,items], file6)

    with open('task6.txt', 'r') as file:
        json_data = json.load(file)

    dictdata = json_data[0]
    print(dictdata.keys())
    print(dictdata.items())
    print(dictdata.values())

    itemsdata = json_data[1]
    print(itemsdata)


def task7():
    print("\n ******* task 7 ******** \n")
    for line in open('CrimeReport.txt').readlines():
        tweet = json.loads(line)
        print tweet['id']


def task8():
    print("\n ******* task 8 ******** \n")
    tweets = []

    for line in open('CrimeReport.txt').readlines():
        tweet = json.loads(line)
        datetime_obj = datetime.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
        tweets.append(tweet)


    sorted_tweets = sorted(tweets, key=lambda item:
    datetime.datetime.strptime(item['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))

    f = open('task8.txt', 'w')
    for tweet in sorted_tweets[-10:]:
        f.write(json.dumps(tweet) + '\n')
    f.close()

    print "See file task8.txt"


def task9():
    print("\n ******* task 9 ******** \n")
    tweets = []
    datetime_filename = datetime
    filename = ''

    for line in open('CrimeReport.txt').readlines():
        tweet = json.loads(line)
        tweets.append(tweet)

    sorted_tweets = sorted(tweets, key=lambda item:
    datetime.datetime.strptime(item['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))

    if os.path.exists('task9'):
        shutil.rmtree('task9')

    os.makedirs('task9')

    for tweet in sorted_tweets[:]:
        datetime_obj = datetime.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
        filename = datetime_obj.strftime('%m-%d-%y-%H') + ".txt"


        if os.path.exists('task9/'+filename):
            f = open('task9/'+filename, 'a')
            f.write(json.dumps(tweet) + '\n')
            f.close()

        else:
            f = open('task9/'+filename,'w')
            f.write(json.dumps(tweet) + '\n')
            f.close()

    print "See filder task9"


def task10():
    print("\n ******* task 10 ******** \n")
    tweets = []

    for line in open('CrimeReport.txt').readlines():
        tweet = json.loads(line)
        tweets.append(tweet)

    f = open("positive-sentiment-tweets.txt", 'w')
    f.close()

    f = open("negative-sentiment-tweets.txt", 'w')
    f.close()

    for tweet in tweets:
        print sentiment(tweet["text"])
        if positive(tweet["text"], threshold=0.1):
            f = open('positive-sentiment-tweets.txt', 'a')
            f.write(json.dumps(tweet) + '\n')
            f.close()
        else:
            f = open('negative-sentiment-tweets.txt', 'a')
            f.write(json.dumps(tweet) + '\n')
            f.close()


if __name__ == '__main__':
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
    task8()
    task9()
    task10()


