# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:56:54 2022

@author: adheeb
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def lineplot(dat,dat1):
    """This function produces a lineplot of new covid cases of 
    four different countries in January 2021 and saves the image as a png file"""
    plt.figure()
    line(dat,dat1)
    plt.title("New Covid Positive Cases (January 2021)", size = 18)
    plt.xlabel("Date", size = 15)
    plt.ylabel("No. of Positive Cases", size = 15)
    plt.xticks(rotation = 90)
    plt.legend()
    plt.savefig("lineplot.png", dpi = 300, bbox_inches = "tight")
    plt.show()

def line(dat,dat1):
    """This function produces a lineplot of new covid cases of 
    four different countries in January 2021 by iterating the """
    
    for i in range(len(countries)):
        plt.plot(dat[i]["date"], dat[i]["new_cases"], label = dat1[i])


def bargraph(dat):
    """This function plots bar graph of new covid cases in United Kingdom 
    in January 2021 and saves the image as a png file"""
    plt.figure(1)
    plt.bar(dat["date"],dat["new_cases"])
    plt.xlabel("Date", size = 15)
    plt.ylabel("No. of Positive Cases",size = 15)
    plt.title("New Covid Positive Cases in United Kingdom \n(January 2021)",size = 18 )
    plt.xticks(rotation = 90)
    plt.savefig("bargraph.png", dpi = 300, bbox_inches = "tight")
    plt.show(1)

    
def pieplot(dat):
    """This function produces a pieplot comparing the total 
    covid cases in January 2021 of UK, India, UAE and USA"""
    plt.figure(2)
    plt.pie(dat, autopct="%1.1f%%")
    plt.title("Comparison of Total Covid Positive Cases in\n UK, India, UAE and USA (January 2021)",size=15)
    plt.legend(bbox_to_anchor=(1,1) , labels=["United Kingdom", "India", "United States of America", "United Arab Emirates"])
    plt.savefig("pieplot.png", dpi=300, bbox_inches = "tight")
    plt.show(2)

#Reading data from csv file
data = pd.read_csv("owid-covid-data.csv")


#Filters the rows to select the data of United Kingdom in January 2021 from the dataframe
uk = data[217632 : 217663]

#Filters the rows to select the data of India in January 2021 from the dataframe
ind = data[95005 : 95036]

#Filters the rows to select the data of United Arab Emirates in January 2021 from the dataframe
uae = data[216624 : 216653]

#Filters the rows to select the data of United States of America in January 2021 from the dataframe
us = data[218651 : 218680]

"""Creating an array with sums of new covid cases in UK, India, UAE and USA in 
January 2021 to use for pie plot"""
total_cases = np.array([uk['new_cases'].sum(), ind['new_cases'].sum(), 
                        us['new_cases'].sum(), uae['new_cases'].sum()])

con = ["United Kingdom","India","United Arab Emirates","United States"]
countries = [uk,ind,uae,us]
   
#calling boxplot function
lineplot(countries,con)

#calling bargraph function
bargraph(uk)

#calling pieplot function
pieplot(total_cases)




