# -*- coding: utf-8 -*-
import glob
import os

# Directories in LGC to be checked:
directory_to_check = "/home/ilofar/Data/IE613/monitor/"
# Which directory do you want the single output dates javascript to be saved in?
directory_save_dates = "/home/ilofar/Data/IE613/monitor/"
directories = [os.path.abspath(x[0]) for x in os.walk(directory_to_check)]

substring = "monitor/2"  #this is used to make function create_list only run in subfolders with the required png
substring2 = "00X"
substring3 =  "00Y"
substring4 = "lightcurve"

def cut(str):
  if len(str) < 2:
    return ''
  return str[23:]

def cut_year2(str):
  return str[32:36]
    
def cut_month2(str):
    month = int(str[37:39])
    month2 = month - 1
    return month2

def cut_day2(str):
  return int(str[40:42])

dates = []

#below function creates a list of dates to be blacklisted from the calendar in the website ------------------
def Create_date_list():
    for x in range(2017, 2030):
        for y in range(0,13):
            for z in range(1,32):
                nam = "new Date("  + str(x) + "," + str(y) + "," + str(z)  + ")"
                dates.append(nam)
    s = 0
    for i in directories: 
        if directories[s].find(substring) != -1:  
            os.chdir(i)         # Change working Directory
            part = "new Date("  + cut_year2(directories[s]) + "," + str(cut_month2(directories[s])) + "," + str(cut_day2(directories[s]))  + ")"
            print(part)
            dates.remove(part)
        s += 1
    os.chdir(directory_save_dates)         # Change working Directory back to beginning directory to save file with all the dates
    with open('dates_calendar.js', 'w') as f:  #writing a javascript file that makes a list of all dates with data for calendar function
        print('var date_list = ' + str(dates).replace("'", "") , file = f)
Create_date_list()


#below function creates a list of pngs in each subfolder by date of creation, in a javascript file that can be fetched by website to display all pngs ------------------
def Create_list():
    s = 0
    for i in directories:
        if directories[s].find(substring) != -1:  
            os.chdir(i)         # Change working Directory
            files = glob.glob("*.png")  #finding all files in subdirectory with .png filenames
            files.sort(key=os.path.getmtime, reverse = True)  #sorting png list by modified date
            x_axis = 1
            x_light = 1
            y_axis = 1
            y_light = 1
            with open('figures.js', 'w') as f:  #writing a javascript file for website to show plots
                for t in range(len(files)):
                    if files[t].find(substring2) != -1: #if png is X axis it will show in row above Y axis
                        if files[t].find(substring4) != -1: #if lightcurve put on right of screen
                            print('document.getElementById("spectra_right_X' + str(x_light) + '").innerHTML += "<img src=\\"' + 'https://data.lofar.ie' + cut(directories[s].replace('\\', '/')) + '/' + files[t].replace('\\', '/')  + '\\" style = \\"width:100%\\">" ', file = f)
                            print('', file = f) 
                            x_light += 1 
                        else: 
                            print('document.getElementById("spectra_left_X' + str(x_axis) + '").innerHTML += "<img src=\\"' + 'https://data.lofar.ie' + cut(directories[s].replace('\\', '/')) + '/' + files[t].replace('\\', '/')  + '\\" style = \\"width:100%\\">" ', file = f)
                            print('', file = f)   
                            x_axis += 1
                            
                    if files[t].find(substring3) != -1: #if png is Y axis it will below X-Axis
                        if files[t].find(substring4) != -1: #if lightcurve put on right of screen
                            print('document.getElementById("spectra_right_Y' + str(y_light) + '").innerHTML += "<img src=\\"' + 'https://data.lofar.ie' + cut(directories[s].replace('\\', '/')) + '/' + files[t].replace('\\', '/')  + '\\" style = \\"width:100%\\">" ', file = f)
                            print('', file = f)     
                            y_light += 1
                        else: 
                            print('document.getElementById("spectra_left_Y' + str(y_axis) + '").innerHTML += "<img src=\\"' + 'https://data.lofar.ie' + cut(directories[s].replace('\\', '/')) + '/' + files[t].replace('\\', '/')  + '\\" style = \\"width:100%\\">" ', file = f)
                            print('', file = f)
                            y_axis += 1
        s += 1
Create_list()






