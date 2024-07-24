o = open("yt history.txt", encoding="utf-8")
hist = o.readlines()

class Video:
    def __init__(self, date="", length="None", name="", channel="", views="", desc=""):
        self.date = date
        self.length = length
        self.name = name
        self.channel = channel
        self.views = views
        self.desc = desc
        
    def display(self):
        print("Uploaded: {}\nLength: {}\nName: {}\nChannel: {}\nViews: {}\nDescription: {}\n".format(self.date, self.length, self.name, self.channel, self.views, self.desc))

    def createRow(self):
        return "{}\t{}\t{}\t{}\t{}\t{}\n".format(self.date, self.length, self.name, self.channel, self.views, self.desc)

def isDate(text):
    if text.strip() in days:
        return True
    if text.split(" ")[0] in months:
        try:
            int(text.split(",")[0].split(" ")[1])
        except:
            return False
        return True
    return False

def isLen(text):
    x = text.split("Now playing")[0].split(":")
    for j in x:
        try:
            int(j)
        except:
            return False
    return True
    

videos = []
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days = ['Today', 'Yesterday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

l = []

for i in range(len(hist)):
    if hist[i].strip() in ["•", ""]:
        l.append(i)

for i in l:
    videos.append(Video())
    
    possiblelen = hist[i - 3].split("Now")[0]
    if isLen(possiblelen):
        videos[-1].length = possiblelen
    
    videos[-1].name = hist[i - 2].strip()
    videos[-1].channel = hist[i - 1].strip()
    videos[-1].views = hist[i + 1].strip()
    
    if not isDate(hist[i + 2]) and not isLen(hist[i+2]):
        videos[-1].desc = hist[i+2].strip()

    n = 3
    while True:
        if isDate(hist[i-n]):
            videos[-1].date = hist[i-n].strip()
            break
        n += 1
        


#SOME EXTRA METHODS BELOW

def createSpreadsheet():
  spreadsheet = ""
  for i in videos:
      spreadsheet += i.createRow()
  return spreadsheet

def displayTopVideos():
  d = {}
  for i in videos:
      if i.channel in d:
          d[i.channel] += 1
      else:
          d[i.channel] = 1
  
  for i in d:
      if d[i] == 1:
          d.remove(i)
      print("{}\t{}".format(i, d[i]))
