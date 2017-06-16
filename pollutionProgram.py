import urllib.request
from xml.dom.minidom import *
from tkinter import *
from tkinter import font
import tkinter.simpledialog
import tkinter.messagebox
import smtplib
from email.mime.text import MIMEText

g_Tk = Tk()
g_Tk.geometry("400x600+500+130")
g_Tk.title("대기오염 정보조회")
DataList = []


def main_yebo():
    import http.client
    import urllib.request
    from xml.dom.minidom import parse, parseString
    import datetime

    index = 0
    i = 0

    now = datetime.datetime.now()
    nal = str(now.year).zfill(4) + "-" + str(now.month).zfill(2) + "-" + str(now.day).zfill(2)

    key = "d0%2BHv5pgp8GmP51m%2B3RWr80O1QDyrg%2FLo%2BMoJt1UlLpUiSzcNxzqIbFNBemjEfFR9jmasbOlM8aO%2FIyaYNHX7A%3D%3D"
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMinuDustFrcstDspth?searchDate=" + nal + "&ServiceKey=" + key

    data = urllib.request.urlopen(url).read()
    f = open("Yebo.xml", "wb")
    f.write(data)
    f.close()

    doc = parse("Yebo.xml")
    item = doc.getElementsByTagName("item")
    dataTime = doc.getElementsByTagName("dataTime")
    informOverall = doc.getElementsByTagName("informOverall")
    informCause = doc.getElementsByTagName("informCause")
    informGrade = doc.getElementsByTagName("informGrade")

    data = []
    Overall = []
    Cause = []
    Grade = []

    tmp1 = str(dataTime[index].firstChild.data)
    tmp2 = str(informOverall[index].firstChild.data)
    tmp3 = str(informCause[index].firstChild.data)
    tmp4 = str(informGrade[index].firstChild.data)

    data.append(tmp1)
    Overall.append(tmp2)
    Cause.append(tmp3)
    Grade.append(tmp4)


    def InitBottmText():
        TempFont = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
        BottomText = Label(g_Tk, font=TempFont, text="미세먼지v0.1")
        BottomText.pack()
        BottomText.place(x=310, y=580)

        # 여긴 바로실행
    #def SearchButtonAction():



    def InitRenderText():
        global RenderText
        global  q1
        RenderTextScrollbar = Scrollbar(g_Tk)
        RenderTextScrollbar.pack()
        RenderTextScrollbar.place(x=375, y=200)

        TempFont = font.Font(g_Tk, size=10, family='Consolas')
        RenderText = Text(g_Tk, width=49, height=22, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
        RenderText.pack()
        RenderText.place(x=10, y=265)
        RenderTextScrollbar.config(command=RenderText.yview)
        RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
        RenderText.insert(INSERT, "-------------------금일 예보-------------------\n\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, tmp1)
        RenderText.insert(INSERT, "] ")
        RenderText.insert(INSERT, "\n\n")
        RenderText.insert(INSERT, tmp2)
        RenderText.insert(INSERT, "\n\n")
        RenderText.insert(INSERT, tmp3)
        RenderText.insert(INSERT, "\n\n")
        RenderText.insert(INSERT, tmp4)
        RenderText.insert(INSERT, "\n")
        q1=RenderText.get('0.0',END)
        RenderText.configure(state='disabled')

    InitRenderText()
    InitBottmText()
        #asd=RenderText.get("10.0",END)

def mail_send():
    mailContents = q1
    mailSubject = "대기 정보입니다."
    sendTo = InputMail.get()
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('zzcx88@gmail.com', 'm1a1abrams')
    msg = MIMEText(mailContents)
    msg['Subject'] = str(mailSubject)
    msg['To'] = str(sendTo)
    smtp.sendmail('zzcx88@gmail.com',str(sendTo) , msg.as_string())

    smtp.quit()

def mailmain():
    mail_son1 = Tk()
    mail_son1.title("메일 보내기")
    mail_son1.geometry('200x150+300+130')
    TempFont = font.Font(mail_son1, size=10, weight='bold', family='Consolas')
    MainText = Label(mail_son1, font=TempFont, text="메일 보내기")
    MainText.pack()
    MainText.place(x=20, y=5)
    InfoText = Label(mail_son1, text="ex):student@kpu.ac.kr")
    InfoText.pack()
    InfoText.place(x=20, y=25)

    global InputMail
    TempFont = font.Font(mail_son1, size=10, weight='bold', family='Consolas')
    InputMail = Entry(mail_son1, font=TempFont, width=20, borderwidth=12, relief='ridge')
    InputMail.pack()
    InputMail.place(x=20, y=45)
    TempFont = font.Font(mail_son1, size=10, weight='bold', family='Consolas')
    SendButton = Button(mail_son1, font=TempFont, text="보내기", command=mail_send)
    SendButton.pack()
    SendButton.place(x=75, y=90)

    def InitBottmText():
        TempFont = font.Font(mail_son1, size=10, weight='bold', family='Consolas')
        BottomText = Label(mail_son1, font=TempFont, text="미세먼지v0.1")
        BottomText.pack()
        BottomText.place(x=115, y=130)
    InitBottmText()

def mail_button():

    TempFont = font.Font(g_Tk, size=8, weight='bold', family = 'Consolas')
    b = Button(g_Tk,font = TempFont, text=" 메일보내기 ",  command=mailmain)
    b.pack()
    b.place(x=305,y=2)

def close_win():
    g_Tk.destroy()
    g_Tk.quit()

def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="대기오염  정보조회")
    MainText.pack()
    MainText.place(x=65,y = 20)

def InitBottmText():
    TempFont = font.Font(g_Tk, size=10, weight='bold', family = 'Consolas')
    BottomText = Label(g_Tk, font = TempFont, text="미세먼지v0.1")
    BottomText.pack()
    BottomText.place(x=310,y = 580)

def Button1():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    b = Button(g_Tk,font = TempFont, text="측정소 별 \n　 실시간 조회 　　",  command=button1_click)
    b.pack()
    b.place(x=30,y=110)

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text=" 시도 별 측정소 \n  위치 조회   ",  command=button2_click)
    SearchButton.pack()
    SearchButton.place(x=200, y=110)

def Button3():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    b = Button(g_Tk,font = TempFont, text=" 통합대기 환경지수 \n 나쁨 이상 조회 ",  command=button3_click)
    b.pack()
    b.place(x=30,y=210)

def Button4():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    b = Button(g_Tk,font = TempFont, text="전국주간 미세먼지\n 평균 수치 조회 ",  command=button4_click)
    b.pack()
    b.place(x=200,y=210)



def button1_click():
    import http.client
    import urllib.request
    from xml.dom.minidom import parse, parseString
    import datetime

    g_Tk_son1 = Tk()
    g_Tk_son1.title("측정소 별 실시간 조회")
    g_Tk_son1.geometry('400x600+900+130')
    TempFont = font.Font(g_Tk_son1, size=20, weight='bold', family='Consolas')
    MainText = Label(g_Tk_son1, font=TempFont, text="측정소 별 실시간 조회")
    MainText.pack()
    MainText.place(x=65, y=30)
    InfoText = Label(g_Tk_son1, text="ex):정왕동, 종로구")
    InfoText.pack()
    InfoText.place(x=250, y=78)
    InfoText2 = Label(g_Tk_son1, text="해당 지역의 시간별 평균 대기정보 조회")
    InfoText2.pack()
    InfoText2.place(x=138, y=62)
    index = 0
    dong = ""

    def InitBottmText():
        TempFont = font.Font(g_Tk_son1, size=10, weight='bold', family='Consolas')
        BottomText = Label(g_Tk_son1, font=TempFont, text="미세먼지v0.1")
        BottomText.pack()
        BottomText.place(x=310, y=580)

    def InitInputLabel():
        global InputLabel
        TempFont = font.Font(g_Tk_son1, size=15, weight='bold', family='Consolas')
        InputLabel = Entry(g_Tk_son1, font=TempFont, width=26, borderwidth=12, relief='ridge')
        InputLabel.pack()
        InputLabel.place(x=10, y=105)

    def InitSearchButton():
        TempFont = font.Font(g_Tk_son1, size=12, weight='bold', family='Consolas')
        SearchButton = Button(g_Tk_son1, font=TempFont, text="검색", command=SearchButtonAction)
        SearchButton.pack()
        SearchButton.place(x=330, y=110)

    def SearchButtonAction():
        global SearchListBox
        global dong
        global InputLabel
        global q2
        RenderText.configure(state='normal')
        RenderText.delete(0.0, END)
        dong = InputLabel.get()
        key = "agRTEvpQv1bNvtoPQr3DNvE5juZ9EAws47JkmLbQnf4OYYAXw%2FAh9TULJtGxrEBzqH2767koxGlukyRTjweQcg%3D%3D"
        url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=" + urllib.parse.quote(dong) + "&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=" + key+"&ver=1.3"
        #print(url)
        data = urllib.request.urlopen(url).read()
        f = open("sidobyul.xml", "wb")
        f.write(data)
        f.close()

        doc = parse("sidobyul.xml")
        item = doc.getElementsByTagName("item")
        dataTime = doc.getElementsByTagName("dataTime")
        mangName = doc.getElementsByTagName("mangName")
        so2Value = doc.getElementsByTagName("so2Value")
        coValue = doc.getElementsByTagName("coValue")
        o3Value = doc.getElementsByTagName("o3Value")
        no2Value = doc.getElementsByTagName("no2Value")
        pm10Value = doc.getElementsByTagName("pm10Value")
        pm10Value24 = doc.getElementsByTagName("pm10Value24")
        pm25Value = doc.getElementsByTagName("pm25Value")
        pm25Value24 = doc.getElementsByTagName("pm25Value24")
        khaiValue = doc.getElementsByTagName("khaiValue")
        khaiGrade = doc.getElementsByTagName("khaiGrade")
        so2Grade = doc.getElementsByTagName("so2Grade")
        coGrade = doc.getElementsByTagName("coGrade")
        o3Grade = doc.getElementsByTagName("o3Grade")
        no2Grade = doc.getElementsByTagName("no2Grade")
        pm10Grade = doc.getElementsByTagName("pm10Grade")
        pm25Grade = doc.getElementsByTagName("pm25Grade")
        pm10Grade1h = doc.getElementsByTagName("pm10Grade1h")
        pm25Grade1h = doc.getElementsByTagName("pm25Grade1h")

        mangnum = mangName.length

        if mangnum == 0:
            tkinter.messagebox.showwarning("알림", "정보가 최신화되지 않았거나, 잘못된 위치입니다.")
        else:
            dataInfo = []
            mangInfo = []
            so2Info = []
            coInfo = []
            o3Info = []
            no2Info = []
            pm10Info = []
            pm10Info24 =[]
            pm25Info = []
            pm25Info24 = []
            khaiInfo = []
            khaiGradeInfo = []
            so2GradeInfo = []
            coGradeInfo = []
            o3GradeInfo = []
            no2GradeInfo = []
            pm10GradeInfo = []
            pm25GradeInfo = []
            pm10Grade1hInfo = []
            pm25Grade1hInfo = []
            index = 0
            while index < mangnum:
                tmp1 = str(dataTime[index].firstChild.data)
                tmp2 = str(mangName[index].firstChild.data)
                tmp3 = str(so2Value[index].firstChild.data)
                tmp4 = str(o3Value[index].firstChild.data)
                tmp5 = str(no2Value[index].firstChild.data)
                tmp6 = str(pm10Value[index].firstChild.data)
                tmp7 = str(pm10Value24[index].firstChild.data)
                tmp8 = str(pm25Value [index].firstChild.data)
                tmp9 = str(pm25Value24[index].firstChild.data)
                tmp10 = str(khaiValue[index].firstChild.data)
                tmp11 = str(khaiGrade[index].firstChild.data)
                tmp12 = str(so2Grade[index].firstChild.data)
                tmp13 = str(coGrade[index].firstChild.data)
                tmp14 = str(o3Grade[index].firstChild.data)
                tmp15 = str(no2Grade[index].firstChild.data)
                tmp16 = str(pm10Grade[index].firstChild.data)
                tmp17 = str(pm25Grade[index].firstChild.data)
                tmp18 = str(pm10Grade1h[index].firstChild.data)
                tmp19 = str(pm25Grade1h[index].firstChild.data)
                tmp20 = str(coValue[index].firstChild.data)

                dataInfo.append(tmp1)
                mangInfo.append(tmp2)
                so2Info.append(tmp3)
                o3Info.append(tmp4)
                no2Info.append(tmp5)
                pm10Info.append(tmp6)
                pm10Info24.append(tmp7)
                pm25Info.append(tmp8)
                pm25Info24.append(tmp9)
                khaiInfo.append(tmp10)
                khaiGradeInfo.append(tmp11)
                so2GradeInfo.append(tmp12)
                coGradeInfo.append(tmp13)
                o3GradeInfo.append(tmp14)
                no2GradeInfo.append(tmp15)
                pm10GradeInfo.append(tmp16)
                pm25GradeInfo.append(tmp17)
                pm10Grade1hInfo.append(tmp18)
                pm25Grade1hInfo.append(tmp19)
                coInfo.append(tmp20)
                index += 1

        for i in range(mangnum):
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "측정 일시 : ")
            RenderText.insert(INSERT, dataInfo[i])
            RenderText.insert(INSERT, "\n측정 망 정보 : ")
            RenderText.insert(INSERT, mangInfo[i])
            RenderText.insert(INSERT, "\n아황산가스 농도 : ")
            RenderText.insert(INSERT, so2Info[i])
            RenderText.insert(INSERT, "\n일산화탄소 농도 : ")
            RenderText.insert(INSERT, coInfo[i])
            RenderText.insert(INSERT, "\n오존 농도 : ")
            RenderText.insert(INSERT, o3Info[i])
            RenderText.insert(INSERT, "\n이산화질소 농도 : ")
            RenderText.insert(INSERT, no2Info[i])
            RenderText.insert(INSERT, "\n미세먼지(PM10) 농도 : ")
            RenderText.insert(INSERT, pm10Info[i])
            RenderText.insert(INSERT, "\n미세먼지(PM10) 24시간예측이동농도 : ")
            RenderText.insert(INSERT, pm10Info24[i])
            RenderText.insert(INSERT, "\n미세먼지(PM2.5) 농도 : ")
            RenderText.insert(INSERT, pm25Info[i])
            RenderText.insert(INSERT, "\n미세먼지(PM2.5) 24시간예측이동농도 : ")
            RenderText.insert(INSERT, pm25Info24[i])
            RenderText.insert(INSERT, "\n통합대기환경수치 : ")
            RenderText.insert(INSERT, khaiInfo[i])
            RenderText.insert(INSERT, "\n통합대기환경지수 : ")
            RenderText.insert(INSERT, khaiGradeInfo[i])
            RenderText.insert(INSERT, "\n아황산가스 지수 : ")
            RenderText.insert(INSERT, so2GradeInfo[i])
            RenderText.insert(INSERT, "\n일산화탄소 지수 : ")
            RenderText.insert(INSERT, coGradeInfo[i])
            RenderText.insert(INSERT, "\n오존 지수 : ")
            RenderText.insert(INSERT, o3GradeInfo[i])
            RenderText.insert(INSERT, "\n이산화질소 지수 : ")
            RenderText.insert(INSERT, no2GradeInfo[i])
            RenderText.insert(INSERT, "\n미세먼지(PM10) 24시간 등급 : ")
            RenderText.insert(INSERT, pm10GradeInfo[i])
            RenderText.insert(INSERT, "\n미세먼지(PM2.5) 24시간 등급 : ")
            RenderText.insert(INSERT, pm25GradeInfo[i])
            RenderText.insert(INSERT, "\n미세먼지(PM10) 1시간 등급 : ")
            RenderText.insert(INSERT, pm10Grade1hInfo[i])
            RenderText.insert(INSERT, "\n미세먼지(PM2.5) 1시간 등급 : ")
            RenderText.insert(INSERT, pm25Grade1hInfo[i])
            RenderText.insert(INSERT, "\n\n")
            i += 1
        q2 = RenderText.get('0.0',END)
        RenderText.configure(state='disabled')

    def InitRenderText():
        global RenderText

        RenderTextScrollbar = Scrollbar(g_Tk_son1)
        RenderTextScrollbar.pack()
        RenderTextScrollbar.place(x=375, y=200)

        TempFont = font.Font(g_Tk_son1, size=20, family='Consolas')
        RenderText = Text(g_Tk_son1, width=49, height=30, borderwidth=12, relief='ridge',
                          yscrollcommand=RenderTextScrollbar.set)
        RenderText.pack()
        RenderText.place(x=10, y=157)
        RenderTextScrollbar.config(command=RenderText.yview)
        RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

        RenderText.configure(state='disabled')

    InitInputLabel()
    InitSearchButton()
    InitRenderText()
    InitBottmText()

def button2_click():
    g_Tk_son2=Tk()
    g_Tk_son2.title("시도 별 측정소 위치조회")
    g_Tk_son2.geometry('400x600+900+130')
    TempFont = font.Font(g_Tk_son2, size=20, weight='bold', family='Consolas')
    MainText = Label(g_Tk_son2, font=TempFont, text="시도 별 측정소 위치조회")
    MainText.pack()
    MainText.place(x=35, y=30)
    InfoText = Label(g_Tk_son2, text="ex):정왕동, 종로구")
    InfoText.pack()
    InfoText.place(x=250, y=78)
    InfoText2 = Label(g_Tk_son2, text="해당 지역의 대기정보 측정소 위치 조회")
    InfoText2.pack()
    InfoText2.place(x=138, y=62)
    dong = ""


    def InitBottmText():
        TempFont = font.Font(g_Tk_son2, size=10, weight='bold', family='Consolas')
        BottomText = Label(g_Tk_son2, font=TempFont, text="미세먼지v0.1")
        BottomText.pack()
        BottomText.place(x=310, y=580)

    def InitSearchListBox():
        global SearchListBox,tag
        ListBoxScrollbar = Scrollbar(g_Tk_son2)
        ListBoxScrollbar.pack()
        ListBoxScrollbar.place(x=310, y=105)

        TempFont = font.Font(g_Tk_son2, size=15, weight='bold', family='Consolas')
        SearchListBox = Listbox(g_Tk_son2, font=TempFont, activestyle='none',
                                width=25, height=1, borderwidth=12, relief='ridge',
                                yscrollcommand=ListBoxScrollbar.set)
        SearchListBox.insert(1, "정왕동")
        SearchListBox.insert(2, "초지동")
        SearchListBox.insert(3, "군자동")
        SearchListBox.insert(4, "고잔동")

        SearchListBox.pack()
        SearchListBox.place(x=10, y=105)

        ListBoxScrollbar.config(command=SearchListBox.yview)

    def InitInputLabel():
        global InputLabel
        TempFont = font.Font(g_Tk_son2, size=15, weight='bold', family='Consolas')
        InputLabel = Entry(g_Tk_son2, font=TempFont, width=26, borderwidth=12, relief='ridge')
        InputLabel.pack()
        InputLabel.place(x=10, y=105)

    def InitSearchButton():
        TempFont = font.Font(g_Tk_son2, size=12, weight='bold', family='Consolas')
        SearchButton = Button(g_Tk_son2, font=TempFont, text="검색", command=SearchButtonAction)
        SearchButton.pack()
        SearchButton.place(x=330, y=110)

    def checkStationData(tx, ty):

        RenderText.configure(state='normal')
        #RenderText.delete(0.0, END)
        key = "d0%2BHv5pgp8GmP51m%2B3RWr80O1QDyrg%2FLo%2BMoJt1UlLpUiSzcNxzqIbFNBemjEfFR9jmasbOlM8aO%2FIyaYNHX7A%3D%3D"
        #chsdUrl = "http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getNearbyMsrstnList?tmX=" + tx + "&tmY=" +ty + "&pageNo=1&numOfRows=10&ServiceKey=" + key
        chsdUrl = "http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getNearbyMsrstnList?tmX=" + str(tx) + "&tmY=" + str(ty) + "&pageNo=1&numOfRows=10&ServiceKey=" + key

        l_data = urllib.request.urlopen(chsdUrl).read()
        l_f = open("checkStationData.xml", "wb")
        l_f.write(l_data)
        l_f.close()
        doc = parse("checkStationData.xml")
        stationName = doc.getElementsByTagName("stationName")
        addr = doc.getElementsByTagName("addr")
        l_num = stationName.length
        l_station = []
        l_add = []
        index = 0
        while index < l_num:
            tmp1 = str(stationName[index].firstChild.data)
            tmp2 = str(addr[index].firstChild.data)
            l_station.append(tmp1)
            l_add.append(tmp2)
            index += 1
        RenderText.insert(INSERT, "\n\n*조회 정보*\n")
        for i in range(l_num):
            RenderText.insert(INSERT, "(")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, ") ")
            RenderText.insert(INSERT, l_station[i])
            RenderText.insert(INSERT, " ")
            RenderText.insert(INSERT, l_add[i])
            RenderText.insert(INSERT, "\n")
            i += 1
        RenderText.insert(INSERT, "\n\n===============================================\n\n")

    def SearchButtonAction():
        global SearchListBox
        global dong
        global InputLabel
        RenderText.configure(state='normal')
        RenderText.delete(0.0, END)
        #iSearchIndex = SearchListBox.curselection()[0]
        #if iSearchIndex == 0:
        #    dong = '%EC%A0%95%EC%99%95%EB%8F%99'
        #elif iSearchIndex == 1:
        #    dong = "%EC%B4%88%EC%A7%80%EB%8F%99"
        #elif iSearchIndex == 2:
        #    dong = "%EA%B5%B0%EC%9E%90%EB%8F%99"
        #elif iSearchIndex == 3:
        #    dong = "%EA%B3%A0%EC%9E%94%EB%8F%99"
        dong = InputLabel.get()
        key = "agRTEvpQv1bNvtoPQr3DNvE5juZ9EAws47JkmLbQnf4OYYAXw%2FAh9TULJtGxrEBzqH2767koxGlukyRTjweQcg%3D%3D"
        url = "http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getTMStdrCrdnt?umdName=" + urllib.parse.quote(dong) + "&pageNo=1&numOfRows=10&ServiceKey=" + key
        data = urllib.request.urlopen(url).read()
        f = open("tmxtmy.xml", "wb")
        f.write(data)
        f.close()

        doc = parse("tmxtmy.xml")
        sidoName = doc.getElementsByTagName("sidoName")
        sggName = doc.getElementsByTagName("sggName")
        umdName = doc.getElementsByTagName("umdName")
        tmX = doc.getElementsByTagName("tmX")
        tmY = doc.getElementsByTagName("tmY")
        num = sidoName.length
        if num == 0:
            tkinter.messagebox.showwarning("알림", "정보가 최신화되지 않았거나, 잘못된 위치입니다.")
        else:
            sido = []
            sgg = []
            umd = []
            tmx = []
            tmy = []
            index = 0
            while index < num:
                tmp1 = str(sidoName[index].firstChild.data)
                tmp2 = str(sggName[index].firstChild.data)
                tmp3 = str(umdName[index].firstChild.data)
                tmp4 = str(tmX[index].firstChild.data)
                tmp5 = str(tmY[index].firstChild.data)
                sido.append(tmp1)
                sgg.append(tmp2)
                umd.append(tmp3)
                tmx.append(tmp4)
                tmy.append(tmp5)
                index += 1
        RenderText.insert(INSERT, "\n===============================================\n")
        for i in range(num):
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "*조회 지역*\n")
            RenderText.insert(INSERT, sido[i])
            RenderText.insert(INSERT, " ")
            RenderText.insert(INSERT, sgg[i])
            RenderText.insert(INSERT, " ")
            RenderText.insert(INSERT, umd[i])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "tmX : ")
            RenderText.insert(INSERT, tmx[i])
            RenderText.insert(INSERT, " ")
            RenderText.insert(INSERT, "tmY : ")
            RenderText.insert(INSERT, tmy[i])
            checkStationData(tmx[i], tmy[i])
            i += 1
        RenderText.configure(state='disabled')

    def InitRenderText():
        global RenderText

        RenderTextScrollbar = Scrollbar(g_Tk_son2)
        RenderTextScrollbar.pack()
        RenderTextScrollbar.place(x=375, y=200)

        TempFont = font.Font(g_Tk_son2, size=10, family='Consolas')
        RenderText = Text(g_Tk_son2, width=49, height=30, borderwidth=12, relief='ridge',
                          yscrollcommand=RenderTextScrollbar.set)
        RenderText.pack()
        RenderText.place(x=10, y=157)
        RenderTextScrollbar.config(command=RenderText.yview)
        RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

        RenderText.configure(state='disabled')

    #InitSearchListBox()
    InitInputLabel()
    InitSearchButton()
    InitRenderText()
    InitBottmText()

def button3_click():
    import urllib.request
    from xml.dom.minidom import parse, parseString
    import tkinter.messagebox
    global num3
    g_Tk_son3 = Tk()
    g_Tk_son3.title("통합대기 환경지수 나쁨이상 조회")
    g_Tk_son3.geometry('400x600+900+130')
    TempFont = font.Font(g_Tk_son3, size=17, weight='bold', family='Consolas')
    MainText = Label(g_Tk_son3, font=TempFont, text="통합대기 환경지수 나쁨이상 조회")
    MainText.pack()
    MainText.place(x=14, y=60)
    TempFont2 = font.Font(g_Tk_son3, size=8,  weight='bold', family='Consolas')
    #BodyText = Label(g_Tk_son3, font=TempFont2, text="통합대기 환경 지수 : 대기오염도 측정치를 국민이 쉽게 \n알 수 있도록 하고 대기오염으로부터 피해를 예방하기 위한 행동지침을 \n국민에게 제시하기 위하여 대기 오염도에 따른 인체 영향 및 체감 오염도를 고려하여 \n개발된 대기오염도 표현방식")
    #BodyText.pack()
    #BodyText.place(x=14, y=60)

    #index = 1
    #i = 0

    key = "d0%2BHv5pgp8GmP51m%2B3RWr80O1QDyrg%2FLo%2BMoJt1UlLpUiSzcNxzqIbFNBemjEfFR9jmasbOlM8aO%2FIyaYNHX7A%3D%3D"
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getUnityAirEnvrnIdexSnstiveAboveMsrstnList?pageNo=1&numOfRows=10&ServiceKey=" + key

    data = urllib.request.urlopen(url).read()
    f = open("nabbem.xml", "wb")
    f.write(data)
    f.close()

    doc = parse("nabbem.xml")
    stationName = doc.getElementsByTagName("stationName")
    addr = doc.getElementsByTagName("addr")
    num3 = stationName.length
    if num3 == 0:
        tkinter.messagebox.showwarning("알림","정보가 최신화 되지 않았습니다.")
    else:
        station = []
        add = []
        index = 0
        while index < num3:
            tmp1 = str(stationName[index].firstChild.data)
            tmp2 = str(addr[index].firstChild.data)
            station.append(tmp1)
            add.append(tmp2)
            index += 1

    def InitBottmText():
        TempFont = font.Font(g_Tk_son3, size=10, weight='bold', family='Consolas')
        BottomText = Label(g_Tk_son3, font=TempFont, text="미세먼지v0.1")
        BottomText.pack()
        BottomText.place(x=310, y=580)

    def InitRenderText():
        global RenderText

        RenderTextScrollbar = Scrollbar(g_Tk_son3)
        RenderTextScrollbar.pack()
        RenderTextScrollbar.place(x=375, y=200)

        TempFont = font.Font(g_Tk_son3, size=10, family='Consolas')
        RenderText = Text(g_Tk_son3, width=49, height=30, borderwidth=12, relief='ridge',
                          yscrollcommand=RenderTextScrollbar.set)
        RenderText.pack()
        RenderText.place(x=10, y=157)
        RenderTextScrollbar.config(command=RenderText.yview)
        RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
        RenderText.insert(INSERT, "---------------통합대기 환경 지수---------------")
        RenderText.insert(INSERT,
                          "대기오염도 측정치를 국민이 쉽게 알 수 있도록 하고 대기오염으로부터 피해를 예방하기 위한 행동지침을 국민에게 제시하기 위하여 대기 오염도에 따른 인체 영향 및 체감 오염도를 고려하여 개발된 대기오염도 표현방식\n\n")

        for i in range(num3):
            RenderText.insert(INSERT, "\n(")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, ")")
            RenderText.insert(INSERT, "도로명 : ")
            RenderText.insert(INSERT, station[i])
            RenderText.insert(INSERT, "\n   ")
            RenderText.insert(INSERT, "주소 : ")
            RenderText.insert(INSERT, add[i])
            RenderText.insert(INSERT, "\n\n")
            i += 1
        RenderText.configure(state='disabled')

    InitRenderText()
    InitBottmText()


def button4_click():
    g_Tk_son4=Tk()
    g_Tk_son4.title("전국 미세먼지 평균수치 조회")
    g_Tk_son4.geometry('400x600+900+130')
    import http.client
    import urllib.request
    from xml.dom.minidom import parse, parseString
    global sinum
    #import datetime
    TempFont = font.Font(g_Tk_son4, size=17, weight='bold', family='Consolas')
    MainText = Label(g_Tk_son4, font=TempFont, text="전국 미세먼지 평균수치 조회")
    MainText.pack()
    MainText.place(x=30, y=60)


    #now = datetime.datetime.now()
    #nal = str(now.year).zfill(4) + "-" + str(now.month).zfill(2) + "-" + str(now.day).zfill(2)

    key = "d0%2BHv5pgp8GmP51m%2B3RWr80O1QDyrg%2FLo%2BMoJt1UlLpUiSzcNxzqIbFNBemjEfFR9jmasbOlM8aO%2FIyaYNHX7A%3D%3D"
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst?itemCode=PM10&dataGubun=DAILY&searchCondition=MONTH&pageNo=1&numOfRows=10&ServiceKey=" + key

    data = urllib.request.urlopen(url).read()
    f = open("illill.xml", "wb")
    f.write(data)
    f.close()

    doc = parse("illill.xml")
    item = doc.getElementsByTagName("item")
    dataTime = doc.getElementsByTagName("dataTime")
    dataGubun = doc.getElementsByTagName("dataGubun")
    seoul = doc.getElementsByTagName("seoul")
    gyeonggi = doc.getElementsByTagName("gyeonggi")
    busan = doc.getElementsByTagName("busan")
    daegu = doc.getElementsByTagName("daegu")
    incheon = doc.getElementsByTagName("incheon")
    gwangju = doc.getElementsByTagName("gwangju")
    daejeon = doc.getElementsByTagName("daejeon")
    ulsan = doc.getElementsByTagName("ulsan")
    gangwon = doc.getElementsByTagName("gangwon")
    chungbuk = doc.getElementsByTagName("chungbuk")
    chungnam = doc.getElementsByTagName("chungnam")
    jeonbuk = doc.getElementsByTagName("jeonbuk")
    jeonnam = doc.getElementsByTagName("jeonnam")
    gyeongbuk = doc.getElementsByTagName("gyeongbuk")
    gyeongnam = doc.getElementsByTagName("gyeongnam")
    jeju = doc.getElementsByTagName("jeju")
    sejong = doc.getElementsByTagName("sejong")

    sinum = seoul.length
    if  sinum == 0:
        tkinter.messagebox.showwarning("알림", "정보가 최신화되지 않았습니다.")
    else:
        data = []
        gubun = []
        seoulInfo = []
        gyeonggiInfo = []
        busanInfo = []
        daeguInfo = []
        incheonInfo = []
        gwangjuInfo = []
        daejeonInfo = []
        ulsanInfo = []
        gangwonInfo =  []
        chungbukInfo = []
        chungnamInfo = []
        jeonbukInfo = []
        jeonnamInfo = []
        gyeongbukInfo = []
        gyeongnamInfo = []
        jejuInfo = []
        sejongInfo = []
        index = 0
        while index < sinum:
            tmp1 = str(dataTime[index].firstChild.data)
            tmp2 = str(dataGubun[index].firstChild.data)
            tmp3 = str(seoul[index].firstChild.data)
            tmp4 = str(gyeonggi[index].firstChild.data)
            tmp5 = str(busan[index].firstChild.data)
            tmp6 = str(daegu[index].firstChild.data)
            tmp7 = str(incheon[index].firstChild.data)
            tmp8 = str(gwangju[index].firstChild.data)
            tmp9 = str(daejeon[index].firstChild.data)
            tmp10 = str(ulsan[index].firstChild.data)
            tmp11 = str(gangwon[index].firstChild.data)
            tmp12 = str(chungbuk[index].firstChild.data)
            tmp13 = str(chungnam[index].firstChild.data)
            tmp14 = str(jeonbuk[index].firstChild.data)
            tmp15 = str(jeonnam[index].firstChild.data)
            tmp16 = str(gyeongbuk[index].firstChild.data)
            tmp17 = str(gyeongnam[index].firstChild.data)
            tmp18 = str(jeju[index].firstChild.data)
            tmp19 = str(sejong[index].firstChild.data)

            data.append(tmp1)
            gubun.append(tmp2)
            seoulInfo.append(tmp3)
            gyeonggiInfo.append(tmp4)
            busanInfo.append(tmp5)
            daeguInfo.append(tmp6)
            incheonInfo.append(tmp7)
            gwangjuInfo.append(tmp8)
            daejeonInfo.append(tmp9)
            ulsanInfo.append(tmp10)
            gangwonInfo.append(tmp11)
            chungbukInfo.append(tmp12)
            chungnamInfo.append(tmp13)
            jeonbukInfo.append(tmp14)
            jeonnamInfo.append(tmp15)
            gyeongbukInfo.append(tmp16)
            gyeongnamInfo.append(tmp17)
            jejuInfo.append(tmp18)
            sejongInfo.append(tmp19)
            index += 1

    def InitBottmText():
        TempFont = font.Font(g_Tk_son4, size=10, weight='bold', family='Consolas')
        BottomText = Label(g_Tk_son4, font=TempFont, text="미세먼지v0.1")
        BottomText.pack()
        BottomText.place(x=310, y=580)

    def InitRenderText():
        global RenderText

        RenderTextScrollbar = Scrollbar(g_Tk_son4)
        RenderTextScrollbar.pack()
        RenderTextScrollbar.place(x=375, y=200)

        TempFont = font.Font(g_Tk_son4, size=10, family='Consolas')
        RenderText = Text(g_Tk_son4, width=49, height=30, borderwidth=12, relief='ridge',
                          yscrollcommand=RenderTextScrollbar.set)
        RenderText.pack()
        RenderText.place(x=10, y=157)

        RenderTextScrollbar.config(command=RenderText.yview)
        RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
        RenderText.insert(INSERT, "------일 평균 미세먼지 수치 조회------\n")

        for i in range(sinum):
                RenderText.insert(INSERT, "일시 : ")
                RenderText.insert(INSERT, data[i])
                RenderText.insert(INSERT, "\n서울 : ")
                RenderText.insert(INSERT, seoulInfo[i])
                RenderText.insert(INSERT, "\n경기 : ")
                RenderText.insert(INSERT, gyeonggiInfo[i])
                RenderText.insert(INSERT, "\n부산 : ")
                RenderText.insert(INSERT, busanInfo [i])
                RenderText.insert(INSERT, "\n대구 : ")
                RenderText.insert(INSERT, daeguInfo [i])
                RenderText.insert(INSERT, "\n인천 : ")
                RenderText.insert(INSERT, incheonInfo[i])
                RenderText.insert(INSERT, "\n광주 : ")
                RenderText.insert(INSERT, gwangjuInfo[i])
                RenderText.insert(INSERT, "\n대전 : ")
                RenderText.insert(INSERT, daejeonInfo[i])
                RenderText.insert(INSERT, "\n울산 : ")
                RenderText.insert(INSERT, ulsanInfo [i])
                RenderText.insert(INSERT, "\n강원 : ")
                RenderText.insert(INSERT, gangwonInfo[i])
                RenderText.insert(INSERT, "\n충북 : ")
                RenderText.insert(INSERT, chungbukInfo[i])
                RenderText.insert(INSERT, "\n충남 : ")
                RenderText.insert(INSERT, chungnamInfo[i])
                RenderText.insert(INSERT, "\n전북 : ")
                RenderText.insert(INSERT, jeonbukInfo[i])
                RenderText.insert(INSERT, "\n전남 : ")
                RenderText.insert(INSERT, jeonnamInfo[i])
                RenderText.insert(INSERT, "\n경북 : ")
                RenderText.insert(INSERT, gyeongbukInfo[i])
                RenderText.insert(INSERT, "\n경남 : ")
                RenderText.insert(INSERT, gyeongnamInfo[i])
                RenderText.insert(INSERT, "\n제주 : ")
                RenderText.insert(INSERT, jejuInfo[i])
                RenderText.insert(INSERT, "\n세종 : ")
                RenderText.insert(INSERT, sejongInfo[i])
                RenderText.insert(INSERT, "\n\n")
                i += 1
        RenderText.configure(state='disabled')

    InitRenderText()
    InitBottmText()
main_yebo()
InitTopText()
InitBottmText()
Button1()
InitSearchButton() #검색버튼
Button3()
Button4()
mail_button()
g_Tk.mainloop()