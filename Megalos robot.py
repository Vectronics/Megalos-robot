import speech_recognition as sr
from googletrans import Translator
import operator
import pyttsx3
import wikipedia
import serial
import datetime as dt
import pyjokes
import random
import cv2
import cvzone
import random
import pyaudio
import gtts
import os
import pybluez
import openai

en=pyttsx3.init('sapi5')
voices=en.getProperty('voices')
en.setProperty(voice,voices[0].id)
print(voices[0].id)
voice=en.getProperty("rate")
en.setProperty("rate",120)
r=sr.Recognizer()

def swrite(serialwrite)
 port=serial.Serial('COM3',9600)
 port.write(seialwrite.encode())

if _name_==_main_:

while True:

      try:
         se.write(b'1')
         names={}
         todate=dt.date.today()
         nday=todate.day
         monthnum=todate.month
         year=todate.year
         with sr.Microphone() as source:
                 print("Say something, good")
                 audio =r.listen(source)
                 text=r.recognize_sphinx(audio,language="ta-in")
                 text = text.lower()
                 translator=translator()
                 tet=translator.translate(text,dest='en')
                 print("tamil:",text,"englis:",tet)
                 tet=tet.lower()
                 tet=tet.replace("plus","+")
                 tet=tet.replace("times,'×")
                 if "hai" in text:
                      en.say("hi how are you")
                      print(" hi how are you")
                      port.write(b'h')
                      en.runAndWait()
                      
                 elif "what is your name " in tet:
                      en.say("en per megalos itarkku arttam periya and Uṅka pēr eṉṉa")
                      en.runAndWait()
                      
                 elif "how are you" in tet:
                     en.say("i am fine ")
                     en.runAndWait()

                 elif "tell me about" in tet:
                     sre=text.replace("tell me about","")
                     results=wikipedia.summary(sre,sentences=2)
                     print(sre)
                     en.say(results)
                     en.runAndWait()
                     
                  elif "tell us about" in tet:
                     sre=text.replace("tell us about","")
                     results=wikipedia.summary(sre,sentences=1)
                     print(sre)
                     en.say(results)
                     en.runAndWait()
                     
                 elif "hi" in tet:
                      en.say("hi how are you")
                      print(" hi how are you")
                      en.runAndWait()
                      
                 elif "tell your story" in tet:
                    en.say('Nāṉtāṉ mekālaṣ rōpōṭ eṉṉāla pēsa muṭiyum pārkka muṭiyum nīṅka kēkkuṟa  kēḷvikaḷukkellām patil solla muṭiyum')
                    en.runAndWait()
                     
                 elif"can you do the math" in tet:
                   en.say("mmm ennala kanakku poda mudiyum")
                     def get_operator_fn(op):
                          return{
                          '+' : operator.add,
                          '-' : operator.sub,
                          'x' : operator.mul,
                          'divided' :operator.__truediv__,
       
        
                     def eval_binary_expr(op1,oper,op2):
                          op1,op2=int(op1),int(op2)
                        return get_operator_fn(oper)(op1,op2)
                        print (eval_binary_expr(*(my_string.split())))
                        en.say (eval_binary_expr(*(my_string.split())))
                        en.runAndWait()
                        
                 elif "date" in tet:
                     en.say(nday)
                     en.runAndWait()
                     
                 elif "time" in tet:
                   ct=dt.time.now()
                   print(ct)
                   hour=ct.hour
                   minutes=ct.minute
                      if hour<=12:
                        en.say(ct)
                        en.say("am")
                        en.runAndWait()
                      elif hour>12:
                        ct= int(hour)-int(12)
                        cct=ct+minutes+"pm"
                        en.say(cct)
                        en.runAndWait()
                        
                 elif "year" in tet:
                   en.say(year)
                   en.runAndWait()
                  
                 elif "month" in tet:
                   month={1: "JANUARY",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December" }
                    print(monthnum,"is",month[monthnum])
                    en.say(month[monthnum])
                    en.runAndWait()
                  
                  elif "day" in tet:
                    dayn=dt.date.today()
                    dayname=[,"Monday","Tuesday""Wednesday" , "Thursday","friday" ,"Saturday","sunday" ]
                    print(dayname[dayn])
                    en.say(dayname[dayn])
                    en.runAndWait()
                    
                 elif "my name is" in tet:
                    name=tet.repalce("my name is","")
                    names.update(name)
                    print("your name is:",names)
                    en.say('hi')
                    en.say(name)
                    en.say('it is nice name')
                    en.runAndWait()
                    
                 else:
                   en.say("sorry")
                   en.say(names)
                   en.say("neenga sonathathu pathi enakku theriyala")
                   en.runAndWait()
    
     except Exception as e:
                  print(e)