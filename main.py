###sources used:
###https://github.com/TomSchimansky/CustomTkinter/wiki/CTkButton
###https://github.com/ParisNeo/FaceAnalyzer/blob/main/examples/OpenCV/eyes_tracker/eyes_tracker.py
import os
from tkinter import *
import customtkinter as ctk
from PIL import Image,ImageTk
from FaceAnalyzer import FaceAnalyzer, Face
from FaceAnalyzer import DrawingSpec, buildCameraMatrix
from FaceAnalyzer.helpers.geometry.orientation import faceOrientation2Euler
from FaceAnalyzer.helpers.ui.opencv import cvOverlayImage
import numpy as np
import cv2
import time
from pathlib import Path
import pickle
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from shapely import affinity
import threading
from pygame import mixer

def clear_all():
    for widget in root.winfo_children():
       widget.destroy()
def pirmas():
    global mygtradius
    clear_all()
    mygtratio=0.85
    mygtradius=16
    button_1=ctk.CTkButton(master=root,width=geomx/2*mygtratio,height=geomy/2*mygtratio,text="1",command=bt1c,corner_radius=mygtradius)#,fg_color='#000000')#,border_width=15,border_color='#FFFFFF',fg_color='#000000')
    button_2=ctk.CTkButton(master=root,width=geomx/2*mygtratio,height=geomy/2*mygtratio,text="2",command=bt2c,corner_radius=mygtradius)#,fg_color='#000000')#,border_width=15,border_color='#FFFFFF',fg_color='#000000')
    button_3=ctk.CTkButton(master=root,width=geomx/2*mygtratio,height=geomy/2*mygtratio,text="3",command=bt3c,corner_radius=mygtradius)##,fg_color='#000000')#,border_width=15,border_color='#FFFFFF',fg_color='#000000')
    button_4=ctk.CTkButton(master=root,width=geomx/2*mygtratio,height=geomy/2*mygtratio,text="4",command=bt4c,corner_radius=mygtradius)#,fg_color='#000000')#,border_width=15,border_color='#FFFFFF',fg_color='#000000')
    button_1.grid(row=0,column=0,padx=geomx/4*(1-mygtratio),pady=geomy/4*(1-mygtratio))
    button_2.grid(row=0,column=1,padx=geomx/4*(1-mygtratio),pady=geomy/4*(1-mygtratio))
    button_3.grid(row=1,column=0,padx=geomx/4*(1-mygtratio),pady=geomy/4*(1-mygtratio))
    button_4.grid(row=1,column=1,padx=geomx/4*(1-mygtratio),pady=geomy/4*(1-mygtratio))
def returnn():
    t1._stop_event=threading.Event()
    t1._stop_event.set()
    t2._stop_event=threading.Event()
    t2._stop_event.set()
    pirmas()
def bt1c():
    global t1
    global labeltext
    clear_all()
    t1=threading.Thread(target=dalykas)
    t1.start()

def loadtxt():
    kraunasi=ctk.CTkLabel(master=root,text=" .")
    kraunasi.pack(side=LEFT)

def tikcapture():
    global alarm
    global beep1
    global width
    global height
    global paveiksliukas
    global arjau
    
    arjau=0
    width = 848
    height = 480 
    cap = cv2.VideoCapture(0)

    image_size = [width, height]
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv2.CAP_PROP_BUFFERSIZE,3)
    paveiksliukas = cap.read()
    arjau=1
    while cap.isOpened():
        paveiksliukas = cap.read()
def dalykas():
    global t2
    global timerclick
    global shortbreak
    shortbreak=5*60
    global longbreak
    longbreak=10*60
    global worktime
    worktime=25*60
    global npomodoro
    timercount=0
    firstr=0
    running=0
    checkevs=time.time()
    npomodoro=3
    canvscale=0.84
    dotsize=4
    bgclr='#1a1a1a'
    global arjau
    timerclick=0
    global width
    screenis=1
    bplaced=0
    global height
    global paveiksliukas
    t2=threading.Thread(target=tikcapture)
    t2.start()
    global paspaudimas
    paspaudimas=0
    global kalibracija
    kalibracija=0
    loadtxt()

    fa = FaceAnalyzer(max_nb_faces=1,image_shape=(width,height))

    box_colors=[
        (255,0,0),
        (255,0,255),
        (255,0,255),

    ]

    calibration_file_name = Path(__file__).parent/"cam_calib.pkl"
    if calibration_file_name.exists():
        with open(str(calibration_file_name),"rb") as f:
            calib = pickle.load(f)
        mtx = calib["mtx"]
        dist = calib["dist"]
    else:
        mtx = None
        dist = np.zeros((4, 1))

    def timerr():
        global timerclick
        timerclick=1
    def screenoff():
        global screenbutton2
        screenbutton2=ctk.CTkButton(master=root,width=geomx,height=geomy,corner_radius=0,textvariable=btn_text2,command=screenon2,fg_color='#000000',hover_color='#000000')
        screenbutton2.place(x=0,y=0,anchor=NW)
        global screenbutton1
        screenbutton1=ctk.CTkButton(master=root,width=geomx,height=geomy,corner_radius=0,text='',command=screenon1,fg_color='#000000',hover_color='#000000')
        screenbutton1.place(x=0,y=0,anchor=NW)
    def screenon1():
        screenbutton1.destroy()
    def screenon2():
        screenbutton2.destroy()
    def screenon():
        screenbutton.destroy()
        alarm.set_volume(100)
    def paspaudimass():
        global paspaudimas
        paspaudimas=1
        kalibracija=0
    def resett():
        global kalibracija
        kalibracija=0
        paspaudimas=0
    def clrbtncmd():
        global screenbutton
        screenbutton=ctk.CTkButton(master=root,width=geomx,height=geomy,corner_radius=0,text='',command=screenon,fg_color='#000000',hover_color='#000000')
        screenbutton.place(x=0,y=0,anchor=NW)
        alarm.set_volume(0)

    beep1.play()
    loadtxt()
    clear_all()
    breakk=0
    timertime="Timer"
    frameee = ctk.CTkFrame(master=root,corner_radius=16,fg_color=bgclr)
    addframescale=0.05
    frameee.place(anchor=NW,x=(geomx-geomx*(addframescale+canvscale))/2,y=(geomy-(geomx/width*height*(canvscale+addframescale)))/2-24-5,height=geomx/width*height*(canvscale),width=geomx*(addframescale+canvscale))
    c=Canvas(master=frameee,width=geomx*canvscale,height=geomx/width*height*canvscale,bg=bgclr,highlightthickness=0)
    posscale=geomx/width*canvscale
    framee = ctk.CTkFrame(master=root,width=geomx,height=geomy-geomx/width*height,corner_radius=16,fg_color=bgclr)
    framee.place(anchor=NE,x=453, y=257-5)
    calbtn= ctk.CTkButton(master=framee,width=100,height=geomy-geomx/width*height,text="Calibration",command=paspaudimass,border_color='#395e9c',fg_color=bgclr,border_width=4,hover_color=bgclr)
    calbtn.pack(side=LEFT,padx=10,pady=5)
    ctk.CTkButton(master=framee,width=100,height=geomy-geomx/width*height,text="Screen Off",command=screenoff,border_color='#395e9c',fg_color=bgclr,border_width=4,hover_color=bgclr).pack(side=LEFT,padx=10,pady=5)
    btn_text = StringVar()
    btn_text2 = StringVar()
    timerbtn=ctk.CTkButton(master=framee,width=100,height=geomy-geomx/width*height,textvariable=btn_text,command=timerr,border_color='#395e9c',fg_color=bgclr,border_width=4,hover_color=bgclr)
    btn_text.set(timertime)
    btn_text2.set("Timer not set")
    timerbtn.pack(side=LEFT,padx=10,pady=5)
    frameeee = ctk.CTkFrame(master=root,corner_radius=0,fg_color="#000000",width=53*0.7,height=58*0.7)
    frameeee.place(x=26+(53*0.4)/2,y=257+(58*0.3)/2-5, anchor=NW) 
    c.pack()
    while arjau==0:
        print("camera not loaded yet")
    lastpos=0
    pos=0
    laststate=-1
    state=0
    alarmm=0
    loopx=-1
    firstrun=1
    

    while True:
        arnuskaite=0
        success, image = paveiksliukas
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)
        fa.process(image)
        if fa.nb_faces>0:
            arnuskaite=1
            for i in range(fa.nb_faces):
                face = fa.faces[i]
                pos, ori = face.get_head_posture()
                if pos is not None:
                    if kalibracija ==0:
                        lastpos=pos
                        lastface=face
                    if kalibracija>0 and abs(lastpos[2]-pos[2])/lastpos[2]>0.4:
                        pos=lastpos
                        face=lastface
                    else:
                        lastpos=pos
                        lastface=face
                if kalibracija <2:
                    c.delete("all")
                    ovalx1=(face.get_landmark_pos(Face.nose_tip_index)[:-1])[0]*posscale-dotsize
                    ovalx2=(face.get_landmark_pos(Face.nose_tip_index)[:-1])[0]*posscale+dotsize
                    ovaly1=(face.get_landmark_pos(Face.nose_tip_index)[:-1])[1]*posscale-dotsize
                    ovaly2=(face.get_landmark_pos(Face.nose_tip_index)[:-1])[1]*posscale+dotsize
                    c.create_oval(ovalx1,ovaly1,ovalx2,ovaly2,fill='#ffffff')
                    c.update()
        if paspaudimas == 1 and kalibracija==0:
            kalibracija=1
            startcal=time.time()
            pirmas=1
        if kalibracija==1:
            laikoskirt=time.time()-startcal
            laikas=5

            if laikoskirt < laikas and arnuskaite==1:
                if pirmas==1:
                    beep1.play()
                    pirmas=2
                pos5=face.get_landmark_pos(Face.nose_tip_index)[:-1]
                posh5=[(face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[1][0]+face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[0][0])/2,(face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[1][1]+face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[0][1])/2]
                poss5=pos
            if laikoskirt < laikas*2 and arnuskaite==1 and laikoskirt>laikas:
                if pirmas==2:
                    beep1.play()
                    pirmas=3
                pos10=face.get_landmark_pos(Face.nose_tip_index)[:-1]
                posh10=[(face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[1][0]+face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[0][0])/2,(face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[1][1]+face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[0][1])/2]
                poss10=pos
                
            if laikoskirt < laikas*3 and arnuskaite==1 and laikoskirt>laikas*2:
                if pirmas==3:
                    beep1.play()
                    pirmas=4
                pos15=face.get_landmark_pos(Face.nose_tip_index)[:-1]
                posh15=[(face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[1][0]+face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[0][0])/2,(face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[1][1]+face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[0][1])/2]
                poss15=pos
            if laikoskirt < laikas*4 and arnuskaite==1 and laikoskirt>laikas*3:
                if pirmas==4:
                    beep1.play()
                    pirmas=5
                pos20=face.get_landmark_pos(Face.nose_tip_index)[:-1]
                posh20=[(face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[1][0]+face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[0][0])/2,(face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[1][1]+face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[0][1])/2]
                poss20=pos
                
            if laikoskirt > laikas*4:
                if pirmas==5:
                    beep1.play()
                    pirmas=6
                kalibracija=2
                polprec=10
                posh=[(face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[1][0]+face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[0][0])/2,(face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[1][1]+face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[0][1])/2]
                polygon = Polygon([(pos5[0]+posh5[0]-posh[0],pos5[1]+posh5[1]-posh[1]), (pos10[0]+posh10[0]-posh[0],pos10[1]+posh10[1]-posh[1]), (pos15[0]+posh15[0]-posh[0],pos15[1]+posh15[1]-posh[1]), (pos20[0]+posh20[0]-posh[0],pos20[1]+posh20[1]-posh[1])])
                viskasok=1
                poss=poss5
                poss[0]=(poss5[0]+poss10[0]+poss20[0])/3
                poss[1]=(poss5[1]+poss10[1]+poss20[1])/3
                poss[2]=(poss5[2]+poss10[2]+poss20[2])/3

        if kalibracija == 2:
            if arnuskaite==1:
                point = Point(face.get_landmark_pos(Face.nose_tip_index)[:-1])
                posh=[(face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[1][0]+face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[0][0])/2,(face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[1][1]+face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[0][1])/2]
                posh=[(face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[1][0]+face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[0][0])/2,(face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[1][1]+face.points_draw_bounding_box(image, color=box_colors[i%3], thickness=5)[0][1])/2]

                polygon = Polygon([(pos5[0]-posh5[0]+posh[0],pos5[1]-posh5[1]+posh[1]), (pos10[0]-posh10[0]+posh[0],pos10[1]-posh10[1]+posh[1]), (pos15[0]-posh15[0]+posh[0],pos15[1]-posh15[1]+posh[1]), (pos20[0]-posh20[0]+posh[0],pos20[1]-posh20[1]+posh[1])])
                if pos is not None:
                    polygon=affinity.scale(polygon,xfact=poss[2]/pos[2],yfact=poss[2]/pos[2],origin=CENTER)
                cv2.drawContours(image, [np.int32(list(polygon.exterior.coords))], -1, (0, 255, 255), -1) 
                dots=np.array(polygon.exterior.coords)
                dots=dots*posscale
                dotss=tuple(map(tuple, dots))
                c.delete("all")
                if breakk==0 or breakk==1:
                    c.create_polygon(*dotss,fill='#395e9c',outline='')
                    ovalx1=(face.get_landmark_pos(Face.nose_tip_index)[:-1])[0]*posscale-dotsize
                    ovalx2=(face.get_landmark_pos(Face.nose_tip_index)[:-1])[0]*posscale+dotsize
                    ovaly1=(face.get_landmark_pos(Face.nose_tip_index)[:-1])[1]*posscale-dotsize
                    ovaly2=(face.get_landmark_pos(Face.nose_tip_index)[:-1])[1]*posscale+dotsize
                    c.create_oval(int(ovalx1),int(ovaly1),int(ovalx2),int(ovaly2),fill='#ffffff')
                    c.update()
            if polygon.contains(point) == True and arnuskaite==1:
                viskasok=1
                alarmm=0
            else:
                if viskasok==1:
                    dabarblogai=time.time()
                    sugrojo=dabarblogai
                    pirmass=1
                    viskasok=0
                else:
                    if time.time()-dabarblogai>3:
                        if sugrojo+3<time.time():
                            alarm.play()
                            sugrojo=time.time()
                            alarmm=1
        if kalibracija==1:
            state=1
        elif breakk==-1 or breakk==2:
            state=6
        elif kalibracija==2 and viskasok==1:
            state=2
        elif alarmm==1:
            state=3
        elif kalibracija==2 and arnuskaite==0:
            state=4
        elif kalibracija==2 and viskasok==0:
            state=5
        if laststate != state:

            if state== 0:
                colorbutton0=ctk.CTkButton(master=frameeee, width=53*0.7,height=58*0.7,text="",corner_radius=16,fg_color=bgclr,command=clrbtncmd) 
                colorbutton0.place(x=0,y=0, anchor=NW)     
            elif state== 1:
                colorbutton1=ctk.CTkButton(master=frameeee, width=53*0.7,height=58*0.7,text="",corner_radius=16,fg_color='#702963',command=clrbtncmd) 
                colorbutton1.place(x=0,y=0, anchor=NW)      
            elif state== 6:
                colorbutton6=ctk.CTkButton(master=frameeee, width=53*0.7,height=58*0.7,text="",corner_radius=16,fg_color='#379956',command=clrbtncmd)   
                colorbutton6.place(x=0,y=0, anchor=NW)   
            elif state== 2:
                colorbutton2=ctk.CTkButton(master=frameeee, width=53*0.7,height=58*0.7,text="",corner_radius=16,command=clrbtncmd)   
                colorbutton2.place(x=0,y=0, anchor=NW)    
            elif state== 3:
                colorbutton3=ctk.CTkButton(master=frameeee, width=53*0.7,height=58*0.7,text="",corner_radius=16,fg_color='#873600',command=clrbtncmd)  
                colorbutton3.place(x=0,y=0, anchor=NW)    
            elif state== 4:
                colorbutton4=ctk.CTkButton(master=frameeee, width=53*0.7,height=58*0.7,text="",corner_radius=16,fg_color=bgclr,command=clrbtncmd)
                colorbutton4.place(x=0,y=0, anchor=NW)    
            elif state== 5:
                colorbutton5=ctk.CTkButton(master=frameeee, width=53*0.7,height=58*0.7,text="",corner_radius=16,fg_color='#9C640C',command=clrbtncmd)  
                colorbutton5.place(x=0,y=0, anchor=NW)    
            
            if laststate== 0:
                colorbutton0.destroy()
            elif laststate== 1:
                colorbutton1.destroy()
            elif laststate== 2:
                colorbutton2.destroy()    
            elif laststate== 3:
                colorbutton3.destroy()   
            elif laststate== 4:
                colorbutton4.destroy()    
            elif laststate== 5:
                colorbutton5.destroy()   
            elif laststate== 6:
                colorbutton6.destroy()   
            laststate=state

        
        if(time.time()-checkevs>1):
            checkevs=time.time()
            if timerclick==1:
                timercount+=1
                timerclick=0
                firstr=1
                running=1
            if firstr==1:
                firstime=time.time()
                firstr=0
                running=1
            if running==1:
                if breakk==-1:
                    breakk=0
                    transition.play()
                    alarm.set_volume(100)
                elif breakk==1:
                    breakk=2
                    transition.play()
                    alarm.set_volume(0)
                currtm=time.time()-firstime
                if timercount%2==1:
                    if currtm>=worktime:
                        firstime=time.time()
                        timercount+=1
                        breakk=1
                    
                    timertimetime=worktime-currtm+1
                    if(int(timertimetime)%60<10):
                        timertime=str(int(timertimetime/60))+':0'+str(int(timertimetime)%60)
                    else:
                        timertime=str(int(timertimetime/60))+':'+str(int(timertimetime)%60)
                elif timercount%2==0 and timercount!=npomodoro*2:
                    if currtm>=shortbreak:
                        firstime=time.time()
                        timercount+=1
                        breakk=-1
                    timertimetime=shortbreak-currtm+1
                    if(int(timertimetime)%60<10):
                        timertime=str(int(timertimetime/60))+':0'+str(int(timertimetime)%60)
                    else:
                        timertime=str(int(timertimetime/60))+':'+str(int(timertimetime)%60)
                else:
                    if currtm>=longbreak:
                        firstime=time.time()
                        timercount=1
                        breakk=-1
                    timertimetime=longbreak-currtm+1
                    if(int(timertimetime)%60<10):
                        timertime=str(int(timertimetime/60))+':0'+str(int(timertimetime)%60)
                    else:
                        timertime=str(int(timertimetime/60))+':'+str(int(timertimetime)%60)
                btn_text.set(timertime)
                if breakk==-1 or breakk==2:
                    btn_text2.set("Break: " + timertime)

                else:
                    btn_text2.set("Work: " + timertime)
                 
def bt2c():
    clear_all()
def bt3c():
    clear_all()
def bt4c():
    clear_all()

if __name__ =="__main__":
    global beep1
    global alarm
    mixer.init()
    transition = mixer.Sound('infobleep-87963.wav')
    beep1 = mixer.Sound('beep-sound-8333.wav')
    alarm = mixer.Sound('beep-6-96243.wav')
    #flsc=os.environ['FLSC']
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    root=ctk.CTk()
    root.configure(background='black')
    geomx=480
    geomy=320
    root.geometry(str(geomx)+"x"+str(geomy))
    #if flsc=='0':
    #    root.attributes('-fullscreen',False)
    #else:
    #    root.attributes('-fullscreen',True)
    root.attributes('-fullscreen',False)
    bt1c()
    root.mainloop()
    

