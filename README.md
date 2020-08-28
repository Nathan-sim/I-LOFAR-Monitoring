# I-LOFAR-Monitoring
In here is kept all the source code used to develop the https://lofar.ie/research-monitoring/ webpage. 

The "Full website source code 3.html" file contains all the HTML, CSS and Javascript used for website.

The "addtoscript.py" is the python script added onto Alberto's script to:

1. Create a blacklist of dates for the calendar on the website.
2. Create a javascript file in each folder of data.lofar.ie with a list of pngs to display that the webpage can then fetch to display all pngs.

The page is hosted within the lofar.ie wordpress website which means that there is a base theme applied to it, making it more difficult to change some of the CSS aspects of the website. And creating some bugs along the way. The upside is that the website is then integrated with the overall lofar.ie website as had been requested by Peter.

Wordpress allows you to enter your own Javascript/CSS/HTML within a page using a "codeblock", this is how I apply the code to the website.

Ideally, the CSS, Javascript and HTML would be seperated into different files, this is not done in this case as it is easier to just copy all the code directly into the "code block" as one in the wordpress website.
