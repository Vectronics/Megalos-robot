import googletrans
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
import bluetooth
import openai
import re
import gtts
import playback
import time


r=sr.Recognizer()

def gpt(prompt):
    openai.api_key="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"
    train_model="text-davinci-002"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1300,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    message = re.sub('[^0-9a-zA-Z\n\.\?,!]+', ' ', message).strip()
    message.lower()
    message.replace('chatgpt','megalos robot')
    print(message)

    
def swrite(serialwrite):
     port=serial.Serial('COM3',9600)
     port.write(seialwrite.encode())
 
 
   

if _name_=="_main_":

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
                     translator=Translator()
                     tet=translator.translate(text,dest='en')
                     print("tamil:",text,"englis:",tet)
                     tet=tet.lower()
                     tet=tet.replace("plus","+")
                     tet=tet.replace("times,'×")
                     if "ஹாய்" in text:
                         # en.say("hi how are you")
                          print(" hi how are you")
                          port.write(b'h')
                          #en.runAndWait()
                          
                          
                     elif "உன் பெயர் என்ன " in tet:
                        
                          
                     elif "எப்படி இருக்க" in tet:
                       textg="நான் நல்லா இருக்கேன் நீங்க எப்படி இருக்கீங்க"
                       tts=gTTs(textg, language='ta')
                       tts.save('hi.mp3')
                       playback.playback('him.mp3')
    
                    
  
                         
      
                         
                     elif "ஹாய்" in tet:
                        
                          
                     elif "உன்ன பத்தி சொல்லு" in tet:
                        textg="நான் உங்களோட ஃபிரண்ட் என்னால நடக்க முடியும் பேச முடியும் எல்லா விஷயங்களும் பண்ண முடியும் நீங்க கேட்கிற கேள்விக்கு எல்லாம்  பதில் சொல்ல முடியும் சிறந்த நண்பனாக எப்பவுமே இருப்பேன் நான் ஒரு செயற்கை நுண்ணறிவு பெற்ற ரோபோ ஆனா நான் பேசும்போது உங்களுக்கு நான் ஒரு ரோபோ மாதிரியே தெரியாது நீங்க என்கிட்ட வச்சு கேட்டு பார்க்கலாம்"
                        tts=gTTs(textg, language='ta')
                       tts.save('tell about you.mp3')
                       playback.playback('tell about you.mp3')
                        
                         
                     elif "கணக்கு பண்ணு" in tet:
                         result=eval(tet)
                         speak(result)
                            
                     elif "இன்னைக்கு என்ன தேதி" in tet:
                         en.say(nday)
                         en.runAndWait()
                         
                     elif "மணி என்ன" in tet:
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
                            
                     elif " இது எந்த வருஷம்" in tet:
                       en.say(year)
                       en.runAndWait()
                      
                     elif "இது எந்த மாசம் " in tet:
                       month={1: "JANUARY",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December" }
                        print(monthnum,"is",month[monthnum])
                        en.say(month[monthnum])
                        en.runAndWait()
                      
                      elif "இன்னைக்கு என்ன கிழமை" in tet:
                        dayn=dt.date.today()
                        dayname=[,"Monday","Tuesday""Wednesday" , "Thursday","friday" ,"Saturday","sunday" ]
                        print(dayname[dayn])
                        en.say(dayname[dayn])
                        en.runAndWait()
             
                        
                     elif" நல்லா இருக்கியா" in tet:
                        textg="நான் நல்லா இருக்கேன் நீங்க எப்படி இருக்கீங்க"
                        tts=gTTs(textg, language='ta')
                       tts.save('how are you.mp3')
                       playback.playback('him.mp3')
 
                    else:
                        gpt(tet)
                        #speak(message)
                        print(message)
                        english_to_tamil= translator.tranlate(message,dest='ta')
                        print(english_to_tamil)
                        tts=GTTs(english_to_tamil.text, language='ta')
                        gTTs.save('extrainfo.mp3')
                        playback.playback('extrainfo.mp3')
                        file_name="extrainfo.mp3"
                        current_dir_path=os.getcwd()
                        file_path=os.path.join(current_dir_path,filename)
                        os.remove(file_path)
                       
        
         except Exception as e:
                      print(e)