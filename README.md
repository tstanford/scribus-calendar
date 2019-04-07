# scribus-calendar

> Produce an elegant and simple "page per month" calendar using this script.

## About
I've created this script because I couldn't find one that suited my tastes. I already had a commercially bought A4 sized calendar in my kitchen and I wanted to produce my own in a similar format. Although there are other calendar script available for scribus, most notibly the CalendarWizard (https://wiki.scribus.net/canvas/CalendarWizard), this script wasn't based on any of those and was developed from scratch. There is currently no GUI to adjust the configuration or to select the year you want to produce or import special dates you would like prepopulated. This currently has to be done by editing the script directly.

## Installation
This script requires Scribus is installed (https://www.scribus.net/). This script has been developed and tested against version 1.4.8 running on Debian Linux. Installation can be as simple as placing into your home directory and selecting Script > Execute Script from the Scribus menu. 

## Features
The calendar feature a page per month in portrait orientation. The days of the month are listed in an 3x11 grid leaving enough space to write in. The calendar can prepopulate special events prior to printing. To do this, you'll need to edit the list of events in the script itself.

## Usage
* Open Scribus.
* From the Application menu select Script > Execute Script. A dialog will appear. Select the file cal.py. The script will not prompt you for any values. At this point, you're expected to have configured it yourself prior to executing.

## Example Calendar
![Image](https://i.imgur.com/DWJZEn9.jpg)

## Feedback, contribution.
Please feel free to get in touch if you wish to give feedback or to contribute, fork my project etc.

Finally, enjoy and I hope you find it useful.



