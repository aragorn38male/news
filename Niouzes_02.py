import urequests
#from m5stack import *
from m5ui import clear_bg,M5Button,M5TextBox

clear_bg(0x0)
lcd.font(lcd.FONT_DefaultSmall)

btnA = M5Button(name="ButtonA", text="ButtonA", visibility=False)
btnB = M5Button(name="ButtonB", text="ButtonB", visibility=False)
btnC = M5Button(name="ButtonC", text="ButtonC", visibility=False)

def remplace_accent(t):
  for i in range(len(t)):
    if t[i]=="é":
      t=t[:i]+"e"+t[i+1:]
    if t[i]=="ë":
      t=t[:i]+"e"+t[i+1:]
    if t[i]=="ê":
      t=t[:i]+"e"+t[i+1:]
    if t[i]=="è":
      t=t[:i]+"e"+t[i+1:]
    if t[i]=="ç":
      t=t[:i]+"c"+t[i+1:]
    if t[i]=="à":
      t=t[:i]+"a"+t[i+1:]
    if t[i]=="ä":
      t=t[:i]+"a"+t[i+1:]
    if t[i]=="â":
      t=t[:i]+"a"+t[i+1:]
    if t[i]=="ù":
      t=t[:i]+"u"+t[i+1:]
    if t[i]=="û":
      t=t[:i]+"u"+t[i+1:]
    if t[i]=="œ":
      t=t[:i]+"oe"+t[i+1:]
    if t[i]=="ô":
      t=t[:i]+"o"+t[i+1:]
  return t

def news():
  lst=[]
  resp=urequests.get("https://www.lemonde.fr/rss/une.xml")
  txt = resp.text
  spam=0
  while txt.find("<title>") != -1:
    spam+=1
    a=txt.find("<title>")
    b=txt.find("</title>")
    if spam>2:
      lst.append(txt[a+7:b])
    txt=txt[b+8:]
  del resp,txt,spam
  return lst

n=news()

for i in range(len(n)):
  tmp=remplace_accent(n[i])
  n[i]=tmp
  #M5TextBox(0,i*12, n[i], lcd.FONT_DefaultSmall,0xFFFFFF, rotate=0)
  #M5TextBox(0,(i+1)*12, "                                   ", lcd.FONT_DefaultSmall,0xFFFFFF, rotate=0)
  lcd.print(n[i],0, i*24, 0xffffff)
  #lcd.print("                                   ",0, (i+1)*13, 0xffffff)
