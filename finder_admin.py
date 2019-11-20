import sys,os,random
import threading
import requests
import OpenSSL,time




PANELS = [panel.strip() for panel in open("....../admin-finder.txt")]
USER_AGENTS = [gent.strip() for gent in open("...../user-agents.txt")]


say = 0
def Finder():
    global PANELS
    global say
    try:
        say += 1
        if say == len(PANELS)-1:
            exit()
        istek = requests.get(sys.argv[1]+PANELS[say],headers={"User-Agent":random.choice(USER_AGENTS)})
        if istek.status_code == 200:
                print("*"*100)
                print("["+str(say)+"]"+"+++++++++++++++++++++++ Panel bulundu +++++++++++++++++++++++ "+str(PANELS[say]) + " --- " + str(istek.status_code)+" --- "+str(istek.elapsed))
                print("*" * 100)
                sys.exit()
        elif istek.status_code == 302:
           print("["+str(say)+"]"+"------ Yönlendirme ------- "+str(PANELS[say]) + "---" + str(istek.status_code)+" --- "+str(istek.elapsed))
           pass
        elif istek.status_code == 404:
            print("["+str(say)+"]"+"------ Sayfa bulunamadı ------- "+str(PANELS[say]) + "---" + str(istek.status_code)+" --- "+str(istek.elapsed))
            pass
        else:
            print("Bulunamadı...")
            pass
    except requests.exceptions.ConnectionError:
        pass
    except OpenSSL.SSL.Error:
        pass



thread = []
for i in range(len(PANELS)-1):
    t = threading.Thread(target=Finder)
    thread.append(t)


for g in thread:
    g.start()
    time.sleep(0.05)













