import datetime
import calendar

from scribus import *

frame = {"width":191.67, "height":33.36, "startX": 10, "startY": 465, "dayWidth": 20}
birthday = []

def renderMonth(month, year):
    monthName = calendar.month_name[month]

    if(month>1):
        newPage(-1)

    createImage(10, 10, 575, 412.50, "image_"+monthName)
    monthFrameName = createText(10, 429, 575/2, 45, "monthLabel_"+monthName)
    yearFrameName = createText((575/2)+10, 429, (575/2), 45, "monthLabel_"+monthName)

    insertText(monthName+" ", -1, monthFrameName)
    insertText(str(year), -1, yearFrameName)
    setStyle("Month", monthFrameName)
    setStyle("Year", yearFrameName)
    
    currentCellX=0
    currentCellY=0
    
    startDay, totalDays = calendar.monthrange(year, month)   
    
    for day in range(0, totalDays):
        currentDate = datetime.date(year, month, day+1)
        dayOfWeek = calendar.day_name[currentDate.weekday()]
        dayOfMonth = day+1
        lineRightMargin=8

        x = frame["startX"]+(currentCellX*frame["width"])
        y = frame["startY"]+(currentCellY*frame["height"])

        dayOfMonthCellName = createText(x, y+(frame["height"]/1.7), frame["dayWidth"], frame["height"]/1.7, "grid_"+monthName+"_"+str(dayOfMonth)+"_1")
        dayOfWeekCellName = createText(x+frame["dayWidth"], y+(frame["height"]/1.7), frame["width"]-frame["dayWidth"], frame["height"]/1.7, "grid_"+monthName+"_"+str(dayOfMonth)+"_2")
        insertText(str(dayOfMonth),-1,dayOfMonthCellName)
        insertText(dayOfWeek[:3],-1,dayOfWeekCellName)
        setStyle("DayOfMonth", dayOfMonthCellName)
        setStyle("DayOfWeek", dayOfWeekCellName)

        for event in events:
            if event.date == currentDate:
                eventCell = createText(x+frame["dayWidth"]+frame["dayWidth"], y+(frame["height"]/1.9), frame["width"]-frame["dayWidth"]-25-lineRightMargin, frame["height"]/1.9, "grid_"+monthName+"_"+str(dayOfMonth)+"_2")
                insertText(event.label,-1,eventCell)
                setStyle("SpecialEvent", eventCell)
                break                

        lineName = createLine(x, y+frame["height"], x+frame["width"]-lineRightMargin, y+(frame["height"]))
        setLineStyle(LINE_DOT, lineName)

        if currentCellY == 10:
            currentCellY = 0
            currentCellX = currentCellX +1
        else:
            currentCellY = currentCellY +1

def generate(year):
    global events
    events = [
        Anniversary("Emily's Birthday", year, 1, 8),
        Anniversary("Vicki's Birthday", year, 6, 6),
        Anniversary("Tim's Birthday", year, 7, 18),      
        Anniversary("Rebecca's Birthday", year, 9, 12),
        Anniversary("Christine's Birthday", year, 3, 3),
        Anniversary("Peter's Birthday", year, 1, 18),
        Anniversary("Marianne's Birthday", year, 5, 4),
        Anniversary("Darren's Birthday", year, 6, 14),
        Anniversary("Jeff's Birthday", year, 7, 22),
        Anniversary("Leanne's Birthday", year, 5, 31),
        Anniversary("Jack & Adam's Birthday", year, 3, 27),
        Anniversary("Jamie's Birthday", year, 4, 25),
        Anniversary("Allan's Birthday", year, 12, 27)
        ]

    newDocument(PAPER_A4, (10, 10, 10, 10), PORTRAIT, 1, UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1)

    defineColor("SpecialEvent",  int(255*0.75), int(255*0.26), int(255*0.0), int(255*0.0))

    createCharStyle("MonthText", font="Montserrat Black", fontsize=32, scalev=1.1)
    createCharStyle("YearText", font="Montserrat Black Italic", fontsize=42, fillshade=0.7, scalev=1.1)
    createCharStyle("DayOfMonthText", font="Noto Sans Bold", fontsize=14)
    createCharStyle("DayOfWeekText", font="Noto Sans Regular", fontsize=10, fillshade=0.7)
    createCharStyle("SpecialEventText", font="Kalam Regular", fontsize=12, fillcolor="SpecialEvent")

    createParagraphStyle("SpecialEvent", charstyle="SpecialEventText", alignment = 1)
    createParagraphStyle("Month", charstyle="MonthText")
    createParagraphStyle("Year", charstyle="YearText", alignment=2)
    createParagraphStyle("DayOfWeek", charstyle="DayOfWeekText")
    createParagraphStyle("DayOfMonth", charstyle="DayOfMonthText")    
    
    for i in range(1,13):
        renderMonth(i, year)

class Anniversary:
    def __init__(self, label, year, month, day):
        self.label = label
        self.date = datetime.date(year, month, day)

generate(2020)

