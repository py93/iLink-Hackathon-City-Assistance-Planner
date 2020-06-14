import threading
import time
import math
import json
from operator import itemgetter
from datetime import datetime
from collections import deque
import datetime as dt
from lib.utilities.RunShortestPath import *

runStatus = {}

# def update_queue():
#     import time
#     # while(len(hospital_queue) > 0):
#     #     print(hospital_queue[0])
#     #     hospital_queue.popleft()
#     #
#     while True:
#         if(len(hospital_queue)>0):
#             print(type(hospital_queue[0]))
#         print(datetime.now())
#         time.sleep(5)




class Controller:
    def __init__(self):
        self.mx = 200
        self.my = 200
        global datetimeObj
        global hospital_queue
        global grocery_queue
        global sbi_queue
        global hdfc_queue
        global medical_queue
        global hospitals_data
        global grocery_data
        global sbi_data
        global hdfc_data
        global medical_data

        hospital_queue = deque([])
        grocery_queue = deque([])
        sbi_queue = deque([])
        hdfc_queue = deque([])
        medical_queue = deque([])

        datetimeObj = datetime.now()

        hospital_file = open('web/assets/hospital.json')
        grocery_file = open('web/assets/grocery.json')
        sbi_file = open('web/assets/sbi.json')
        hdfc_file = open('web/assets/hdfc.json')
        medical_file = open('web/assets/medical.json')

        hospitals_data = json.load(hospital_file)
        hospital_file.close()
        grocery_data = json.load(grocery_file)
        grocery_file.close()
        sbi_data = json.load(sbi_file)
        sbi_file.close()
        hdfc_data = json.load(hdfc_file)
        hdfc_file.close()
        medical_data = json.load(medical_file)
        medical_file.close()
        self.nav = {}

        self.nav["travel001"] = {
            "dest": [300, 300],
            "orig": [100, 100],
            "path": [
                {"a": [100, 100], "b":[150, 100]},
                {"a": [150, 100], "b":[90, 200]},
                {"a": [90, 200], "b":[300, 250]},
                {"a": [300, 250], "b":[300, 300]},
            ]
        }

    def setDestination(self, data):
        self.destination = data["destination"]
        print(self.destination)
        if(self.destination=="hospital"):
            while(len(hospital_queue)>0):
                datetimeObj1 = datetime.now()
                h = hospital_queue[0]
                now = (datetime.strptime(datetimeObj1.strftime('%H')+':'+datetimeObj1.strftime('%M')+':'+datetimeObj1.strftime('%S'),"%H:%M:%S"))
                startTime = (datetime.strptime(h["start"],"%H:%M:%S"))

                if(now>=startTime):
                    diff = now - startTime
                elif(startTime>=now):
                    break
                if(diff.seconds >= 0):
                    (hospitals_data[h["id"]])["count"]-=1
                    if((hospitals_data[h["id"]])["count"]==0):
                        (hospitals_data[h["id"]])["start"]="now"
                    hospital_queue.popleft()

            sorted_hospitals_data = hospitals_data
            for x in sorted_hospitals_data:
                if "dist" in x.keys():
                    x["dist"] = math.sqrt( ((x["x_dest"]-(int)(self.mx))**2) + ((x["y_dest"]-(int)(self.my))**2))

            return(sorted(sorted_hospitals_data,key=itemgetter('count','start','dist')))

        elif(self.destination=="grocery" or self.destination=="grocerie"):
            while(len(grocery_queue)>0):
                datetimeObj1 = datetime.now()
                g = grocery_queue[0]

                now = (datetime.strptime(datetimeObj1.strftime('%H')+':'+datetimeObj1.strftime('%M')+':'+datetimeObj1.strftime('%S'),"%H:%M:%S"))
                startTime = (datetime.strptime(g["start"],"%H:%M:%S"))

                if(now>=startTime):
                    diff = now - startTime
                elif(startTime>=now):
                    break
                if(diff.seconds >= 0):
                    (grocery_data[g["id"]])["count"]-=1
                    if((grocery_data[g["id"]])["count"]==0):
                        (grocery_data[g["id"]])["start"]="now"
                    grocery_queue.popleft()

            sorted_grocery_data = grocery_data
            for x in sorted_grocery_data:
                if "dist" in x.keys():
                    x["dist"] = math.sqrt( ((x["x_dest"]-(int)(self.mx))**2) + ((x["y_dest"]-(int)(self.my))**2))

            return(sorted(sorted_grocery_data,key=itemgetter('count','start','dist')))

        elif(self.destination=="sbi" or self.destination=="sbibank"):
            while(len(sbi_queue)>0):
                datetimeObj1 = datetime.now()
                s = sbi_queue[0]

                now = (datetime.strptime(datetimeObj1.strftime('%H')+':'+datetimeObj1.strftime('%M')+':'+datetimeObj1.strftime('%S'),"%H:%M:%S"))
                startTime = (datetime.strptime(s["start"],"%H:%M:%S"))

                if(now>=startTime):
                    diff = now - startTime
                elif(startTime>=now):
                    break
                if(diff.seconds >= 0):
                    (sbi_data[s["id"]])["count"]-=1
                    if((sbi_data[s["id"]])["count"]==0):
                        (sbi_data[s["id"]])["start"]="now"
                    sbi_queue.popleft()

            sorted_sbi_data = sbi_data
            for x in sorted_sbi_data:
                if "dist" in x.keys():
                    x["dist"] = math.sqrt( ((x["x_dest"]-(int)(self.mx))**2) + ((x["y_dest"]-(int)(self.my))**2))

            return(sorted(sorted_sbi_data,key=itemgetter('count','start','dist')))

        elif(self.destination=="hdfc" or self.destination=="hdfcbank"):
            while(len(hdfc_queue)>0):
                datetimeObj1 = datetime.now()
                hd = hdfc_queue[0]

                now = (datetime.strptime(datetimeObj1.strftime('%H')+':'+datetimeObj1.strftime('%M')+':'+datetimeObj1.strftime('%S'),"%H:%M:%S"))
                startTime = (datetime.strptime(hd["start"],"%H:%M:%S"))

                if(now>=startTime):
                    diff = now - startTime
                elif(startTime>=now):
                    break
                if(diff.seconds >= 0):
                    (hdfc_data[hd["id"]])["count"]-=1
                    if((hdfc_data[hd["id"]])["count"]==0):
                        (hdfc_data[hd["id"]])["start"]="now"
                    hdfc_queue.popleft()

            sorted_hdfc_data = hdfc_data
            for x in sorted_hdfc_data:
                if "dist" in x.keys():
                    x["dist"] = math.sqrt( ((x["x_dest"]-(int)(self.mx))**2) + ((x["y_dest"]-(int)(self.my))**2))

            return(sorted(sorted_hdfc_data,key=itemgetter('count','start','dist')))

        elif(self.destination=="medical"):
            while(len(medical_queue)>0):
                datetimeObj1 = datetime.now()
                m = medical_queue[0]

                now = (datetime.strptime(datetimeObj1.strftime('%H')+':'+datetimeObj1.strftime('%M')+':'+datetimeObj1.strftime('%S'),"%H:%M:%S"))
                startTime = (datetime.strptime(m["start"],"%H:%M:%S"))

                if(now>=startTime):
                    diff = now - startTime
                elif(startTime>=now):
                    break
                if(diff.seconds >= 0):
                    (medical_data[m["id"]])["count"]-=1
                    if((medical_data[m["id"]])["count"]==0):
                        (medical_data[m["id"]])["start"]="now"
                    medical_queue.popleft()

            sorted_medical_data = medical_data
            for x in sorted_medical_data:
                if "dist" in x.keys():
                    x["dist"] = math.sqrt( ((x["x_dest"]-(int)(self.mx))**2) + ((x["y_dest"]-(int)(self.my))**2))

            return(sorted(sorted_medical_data,key=itemgetter('count','start','dist')))


    def getNav(self, data):
        travelId = data["travelId"]
        if travelId in self.nav:
            return self.nav[travelId]
        print(self.nav)
        return None

    def finalizeTravel(self, data):
        dest = data["destination"]
        destObj = None
        for x in hospitals_data:
            if(x["name"]==dest):
                destObj = x
                datetimeObj = datetime.now()
                datetimeObj = datetimeObj + dt.timedelta(seconds=25)
                x["start"] = datetimeObj.strftime('%H')+':'+datetimeObj.strftime('%M')+':'+datetimeObj.strftime('%S')
                hospital_queue.append(x)
                x["count"]+=1
                break
        for x in grocery_data:
            if(x["name"]==dest):
                destObj = x
                datetimeObj = datetime.now()
                datetimeObj = datetimeObj + dt.timedelta(seconds=25)
                x["start"] = datetimeObj.strftime('%H')+':'+datetimeObj.strftime('%M')+':'+datetimeObj.strftime('%S')
                grocery_queue.append(x)
                x["count"]+=1
                break
        for x in sbi_data:
            if(x["name"]==dest):
                destObj = x
                datetimeObj = datetime.now()
                datetimeObj = datetimeObj + dt.timedelta(seconds=25)
                x["start"] = datetimeObj.strftime('%H')+':'+datetimeObj.strftime('%M')+':'+datetimeObj.strftime('%S')
                sbi_queue.append(x)
                x["count"]+=1
                break
        for x in hdfc_data:
            if(x["name"]==dest):
                destObj = x
                datetimeObj = datetime.now()
                datetimeObj = datetimeObj + dt.timedelta(seconds=25)
                x["start"] = datetimeObj.strftime('%H')+':'+datetimeObj.strftime('%M')+':'+datetimeObj.strftime('%S')
                hdfc_queue.append(x)
                x["count"]+=1
                break
        for x in medical_data:
            if(x["name"]==dest):
                destObj = x
                datetimeObj = datetime.now()
                datetimeObj = datetimeObj + dt.timedelta(seconds=25)
                x["start"] = datetimeObj.strftime('%H')+':'+datetimeObj.strftime('%M')+':'+datetimeObj.strftime('%S')
                medical_queue.append(x)
                x["count"]+=1
                break

        print(dest)

        dx, dy = 200, 200
        if destObj is not None:
            dx, dy = destObj["x_dest"], destObj["y_dest"]

        id = str(int(time.time() * 10000))
        self.nav[id] = {
            "dest": [dx, dy],
            "orig": [self.mx, self.my],
            "path": [
                # {"a": [100, 100], "b":[150, 100]},
                # {"a": [150, 100], "b":[90, 200]},
                # {"a": [90, 200], "b":[300, 250]},
                # {"a": [300, 250], "b":[300, 300]},
            ]
        }

        shortPath = RunShortestPath(self.mx, self.my, dx, dy)
        print("Short Path", shortPath)
        shortPath = json.loads(shortPath)

        if "path" not in shortPath:
            print("Path data missing from java output")
        else:
            print("Extracting path from java")

        # for point in shortPath["path"]:
        #     self.nav[id]["path"].append(
        #         # {"a": [point[0], point[1]], "b":[point[0] + 1, point[1] + 1]}
        #         # {"a": [point[0], point[1]], "b":[point[0] + 1, point[1] + 1]}
        #     )

        self.nav[id]["path"].append(
            {"a": [shortPath["path"][0][0], shortPath["path"][0][1]], \
             "b":[shortPath["path"][1][0], shortPath["path"][1][1]]}
            # {"a": [point[0], point[1]], "b":[point[0] + 1, point[1] + 1]}
        )

        return {
            "travel": id
        }

    def setOrigin(self, data):
        self.mx = data["mx"]
        self.my = data["my"]
        print(self.mx, self.my)
        return True
