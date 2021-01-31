from twitter import Twitter
import time
from dateutil.tz import gettz
import datetime as dt
import languageModel as langMod
import parshingJSON as pharser

tw = Twitter()
id=""


def start():
    print("Starting program...")
    dms = list()
    while True:
        try :
            if len(dms) is not 0:
                for i in range(len(dms)):
                    message = dms[i]['message']
                    # I take sender_id just in case you want to know who's sent the message
                    sender_id = dms[i]['sender_id']
                    id = dms[i]['id']


                    print("##### PURG PREF RESLT")
                    if message.find('{"P1":') != -1:
                        print("!!! PURGING !!!")
                        tw.delete_dm(id)


                    if len(message) is not 0 and len(message) < 280:
                        if len(message) != 7:
                            print("try to reply")
                            #tw.reply_dm(sender_id,"ACK BOS")

                        # prikitiw is the keyword
                        # if you want to turn off the case sensitive like: priktiw, Prikitiw, pRiKiTiw
                        # just use lower(message) and check it, but please remove the replace function line
                        

                        if "topic" in message:
                            #message = message.replace("prikitiw", "")
                            if len(message) is not 0:
                                
                                #parsing incoming msg
                                result1,result2,result3=langMod.do_run(message)
                                #print(result1,result2,result3)
                                print("entering to JSONing")
                                final=pharser.JSONing(result1,result2,result3)
                                #print(final)

                                tw.reply_dm(sender_id,final)

                                if dms[i]['media'] is None:
                                    #print("DM will be posted")
                                    #tw.post_tweet(message)
                                    tw.delete_dm(id)
                                else:
                                    print("DM will be posted with media")
                                    print(dms[i]['shorted_media_url'])
                                    #tw.post_tweet_with_media(message, dms[i]['media'],dms[i]['shorted_media_url'], dms[i]['type'])
                                    tw.delete_dm(id)
                            else:
                                print("DM deleted because its empty..")
                                tw.delete_dm(id)
                        
                        else:
                            print("DM will be deleted because does not contains keyword..")
                            tw.delete_dm(id)
                        #check for bugs
                        #print("========PURGING")
                        
                dms = list()

            else:
                tm = dt.datetime.now(gettz("GMT+7"))
                print("Time ::", tm)
                print("Direct message is empty...")
                dms = tw.read_dm()
                try:
                    if len(dms) is 0 or dms is None:
                        print("now sleeping 60s")
                        time.sleep(65)
                except Exception as ex:
                    print(ex)
                    time.sleep(60)
                    pass
        except Exception as EX:
            print("exception occur")
            print(EX)
            time.sleep(1800)

            pass

start()

'''
if __name__ == "__main__":
    pass
    start()
    #run_once()
'''