import operator
import random
import sys
import time
import numpy as np
from email.mime.multipart import MIMEMultipart
import pyautogui
import pyttsx3
import requests
import self as self
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import instaloader
import PyPDF2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup
import pywikihow
from jarvisGui import Ui_JarvisGui
import winsound
import pygeoip


def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing, "%I:%M %p"))
    print(altime)

    altime = altime[11:-3]

    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)
    print(f"done, alarm set for {Timing}")

    while True:
        if Horeal == datetime.datetime.now().hour:
            if Mireal == datetime.datetime.now().minute:
                print("alarm is running")
                winsound.PlaySound('abc', winsound.SND_LOOP)

            elif Mireal < datetime.datetime.now().minute:
                break


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


# engine.setProperty('rate', 250)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour > 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis sir. please tell me how can i help you")


#
# def sendEmail(to,content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('knowledgeandentertainment4u@gmail.com', 'Shivannamahadeva')
#     server.sendmail('kumar62.shivu@gmail.com', to, content)
#
#     server.close()

def news():
    main_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=e1a42eac64a64ab7abd3c68f3c4f4fff"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"todays {day[i]} news is: {head[i]}")


def search_wikihow(query, max_results=10, lang="en"):
    return list(pywikihow.WikiHow.search(query, max_results, lang))


def pdf_reader():
    book = open('Rapid Revision Book Geography and Environment.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"total number of pages in this books {pages}")
    speak("please enter the page number i have to read")
    pg = int(input("please enter the page number : "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


def recognize_google(audio):
    pass


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()



    def run(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('C:\\Users\\theja\\PycharmProjects\\pythonProject\\trainer\\trainer.yml')
        cascadePath = "C:\\Users\\theja\\PycharmProjects\\pythonProject\\haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath)
        font = cv2.FONT_HERSHEY_SIMPLEX

        #id = 3

        names = [' ', 'Thejas', 'Kumar']
        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cam.set(3, 640)
        cam.set(4, 480)

        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)

        while True:
            ret, img = cam.read()
            converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                converted_image,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minH)),

            )
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, x + h), (0, 255, 0), 2)
                id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])

                if accuracy < 100:
                    id = names[2]
                    accuracy = " {0}%".format(round(100 - accuracy))
                    cam.release()
                    cv2.destroyAllWindows()
                    self.TaskExecution()

                else:
                    id = "unknown"
                    accuracy = " {0}%".format(round(100 - accuracy))
                    speak("user authentication failed ")

                cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
                cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

            cv2.imshow('camera', img)
            k = cv2.waitKey(10) & 0xff
            if k == 27:
                break

        #print("Thanks for using this program, Have a good day")
        cam.release()
        cv2.destroyAllWindows()


    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening....")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=3, phrase_time_limit=5)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said : {query}")
        except Exception as e:
            speak("say that again please...")
            return "none"
        query = query.lower()
        return query


    def TaskExecution(self):
        speak("Verification Successfull")
        pyautogui.press('esc')
        wish()
        while True:
            # if 1:
            self.query = self.takecommand()

            # logic building for tasks
            if "open notepad" in self.query:
                npath = "C:\\windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif "adobe reader" in self.query:
                apath = ""
                os.startfile(apath)

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)

                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)

                    if k == 27:
                        break;
                cap.release()
                cv2.destroyWindow()

            elif "play music" in self.query:
                music_dir = "D:\\Music"
                songs = os.listdir(music_dir)
                # rd=random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))


            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your ip address is {ip}")

            elif "wikipedia" in self.query:
                speak("searching wikipedia... ")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                # print(results)

            elif "open youtube" in self.query:
                webbrowser.open("https://www.youtube.com")

            # elif "instagram" in self.query:
            #     webbrowser.open("www.instagram.com")

            elif "facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "stack overflow" in self.query:
                webbrowser.open("https://stackoverflow.com/")

            elif "google" in self.query:
                speak("sir,what should i search on google")
                cm = self.takecommand()
                webbrowser.open(f"{cm}")


            elif "whatsapp message" in self.query:
                kit.sendwhatmsg("+919980616104", "this is testing protocol.How are you??", 11, 50)

            elif "play song on youtube" in self.query:
                kit.playonyt("Param Sundari")

            # elif "email kumar" in self.query:
            #     try:
            #         speak("what should i say")
            #         content=self.self.takecommand()().()
            #         to="kumar62.shivu@gmail.com"
            #         sendEmail(to,content)
            #         speak("email has been sent to kumar")
            #
            #     except Exception as e:
            #         print(e)
            #         speak("Sorry Sir i am not able to send mail to kumar")

            elif " go to sleep" in self.query or "no" in self.query or "no thanks" in self.query or "bye" in self.query:
                speak("thanks for using me sir,have a good day")
                sys.exit()

            # to close any application
            elif "close notepad" in self.query:
                speak("okay sir,closing notepad")
                os.system("taskkill /f /im notepad.exe")

            # to set alarm
            elif "set alarm" in self.query:
                nn = int(datetime.datetime.now().r)
                if nn == 22:
                    music_dir = "D:\\Music"
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))
            # to find a joke
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe towrprof.dll,SetSuspendState 0,1,0")

            #################################################################################################################
            #################################################################################################################

            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me today's news" in self.query:
                speak("please wait sir,fetching latest news")
                news()

            elif "email to kumar" in self.query:
                speak("what should i say")
                self.query = self.takecommand()
                if "send a file" in self.query:
                    email = "knowledgeandentertainment4u@gmail.com"
                    password = "Shivannamahadeva"
                    send_to_email = "kumar62.shivu@gmail.com"
                    speak("ok sir,what is the subject for this email")
                    query = self.takecommand()
                    subject = query
                    speak("and sir,what is the message for this email")
                    query2 = self.takecommand()
                    message = query2
                    speak("sir please enter the correct path of the file into the shell")
                    file_location = input("please enter the path here : ")
                    speak("please wait,i am sending email now")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))

                    # setup the attachment

                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment ; filename-%s" % filename)
                    msg.attach(part)

                    ###check once again not working
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("email has been sent to kumar")

                else:
                    email = "knowledgeandentertainment4u@gmail.com"
                    password = "Shivannamahadeva"
                    send_to_email = "kumar62.shivu@gmail.com"
                    message = self.query

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(email, password)
                    server.sendmail(email, send_to_email, message)
                    server.quit()
                    speak("email has been sent to kumar")

            elif "where am i" in self.query or "where we are" in self.query:
                speak("wait sir,let me check")
                try:
                    ipAdd = requests.get("https://ip-api.com/").text
                    print(ipAdd)
                    url = 'http://ip-api.com/json/json/'+ ipAdd
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    state = geo_data['state']
                    country = geo_data['country']
                    speak(f"sir i am not sure but i think we are in {city} city of {state} in {country}")

                except Exception as e:
                    speak("sorry sir,due to network issue,i am not able to find where we are")
                    pass

            elif "instagram profile" in self.query or "profile on instagram" in self.query:
                speak("please enter username correctly sir")

                name = input("enter username her :")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"sir her is the profile of the user {name}")
                #time.sleep(5)
                speak("would you like to download the profile picture of this account")
                self.conditon = self.takecommand()
                if "yes" in self.conditon:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done sir, profile picture is saved in our main folder, now i am ready for next command")
                else:
                    pass

            elif "take screenshot" in self.query:
                speak("sir,please tell me the name for this screenshot file")
                name = self.takecommand()
                speak("please sir,hold the screen for few seconds,i am taking screenshot")
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir, screenshot is saved in our main folder, now i am ready for next command")

            elif "read pdf" in self.query:
                pdf_reader()

            ###############to hide files and folder################

            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak("sir please tell me you want to hide this folder or make it visible for everyone")
                conditon = self.takecommand()

                if "hide" in conditon:
                    os.system("attrib +h /s /d")
                    speak("sir ,all the files in this folder are hidden")

                elif "visible" in conditon:
                    os.system("attrib -h /s /d")
                    speak(
                        "sir, all the files in this folder is visible to everyone. i wish you are taking this decision by your own")

                elif "leave for now" in conditon or "leave it" in conditon:
                    speak("Ok sir")

            elif "do some calculations" in self.query or "calculate" in self.query:
                r = sr.Recognizer()
                try:
                    with sr.Microphone() as source:
                        speak("say what do you want to calculate sir,example 3 plus 3")
                        print("listening...")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                        my_string = r, recognize_google(audio)
                        print(my_string)

                        def get_operator_fn(op):
                            return {
                                '+': operator.add,
                                '-': operator.sub,
                                'x': operator.mul,
                                'divided': operator.__truediv__,

                            }[op]

                        def eval_binary_expr(op1, oper, op2):
                            op1, op2 = int(op1), int(op2)
                            return get_operator_fn(oper)(op1, op2)

                        speak("your result is")
                        speak(eval_binary_expr(*(my_string.split())))
                except Exception as e:
                    speak("sory sir, could not calculate")

            elif "temperature" in self.query:
                search = "temperature in Mysore"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current {search} is {temp}")

            elif "activate mod" in self.query:
                # from pywikihow import search_wikihow
                speak(" mod is activated")
                while True:
                    speak("please tell me what do you want to know")
                    how = self.takecommand()
                    try:
                        if "exit" in how  or "nothing" in how:
                            speak("ok sir, mod is closed")
                            break
                        else:
                            max_results = 1
                            how_to = search_wikihow(how, max_results)
                            assert len(how_to) == 1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as e:
                        speak("sorry sir, i am not able to find this ")

            elif "check battery" in self.query or "how much power left" in self.query or "battery" in self.query:
                import psutil

                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"sir our system have {percentage} percent battery")
                if percentage >= 75:
                    speak("we have enough power to continue our work")
                elif percentage >= 40 and percentage <= 75:
                    speak("we shoud connect our system to charging point to charge our battery")
                elif percentage <= 15 and percentage <= 30:
                    speak("we don't have enough power to work, please connect to charging")
                elif percentage <= 15:
                    speak("we have very low power , please connect to charging or else system will shut down")

            elif "internet speed " in self.query or "net speed" in self.query:
                import speedtest

                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed ")


            elif "send message" in self.query:

                speak("sir what should i say ")
                msz = self.takecommand()
                from twilio.rest import Client
                account_sid = 'AC0fcb318349ceb3283118976aa1cfe379'
                auth_token = '4d26bebba650ad2dd076a507c0e59101'
                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                    body=msz,
                    from_='+15865719835',
                    to='+917259735184'
                )

                print(message.sid)
                speak("sir, message has been sent ")

            elif "alarm" in self.query:
                speak("sir, please tell me the time to set alarm. for example set alarm for 5:00 am")
                tt = self.takecommand()
                tt = tt.replace("set alarm to", "")
                tt = tt.replace(".", "")
                tt = tt.upper()
                import MyAlarm
                MyAlarm.alarm(tt)

            elif "volume up" in self.query:
                pyautogui.press("volumeup")

            elif "volume down" in self.query:
                pyautogui.press("volumedown")

            elif "mute" in self.query:
                pyautogui.press("volumemute")

           #--------Need to check once again for correct output -----------

            elif " open mobile camera" in self.query:
                import urllib.request
                import cv2
                import numpy as np
                import time
                URL = "http://192.168.1.6:8080"
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                    img = cv2.imdecode(img_arr, -1)
                    cv2.imshow('IPWebcam', img)
                    q = cv2.waitKey(1)
                    if q == ord("q"):
                        break;

                cv2.destroyAllWindows()

            speak("sir do you have any other work")


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JarvisGui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../OneDrive/Desktop/ironan.gif")#need to change path when running thorugh this code or else same for exe file
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:\\Users\\theja\\OneDrive\\Desktop\\ironman2.gif") #need to change path when running thorugh this code or else same for exe file
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start()
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
sys.exit(app.exec_())
