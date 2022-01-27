# Personal-Website
This is my very own Personal Website that I built using the Django framework in Python. It serves as a digital journal filled
with most of my hobbies, interests, and professional experiences. The files uploaded here are stored in Heroku Postgre and 
AWS S3 for media files. 

Potential improvements: Lightbox implementation for the Photography section, and better animations such as page transitions.

<b>Tools Used:</b>
<br>
Front-end:
<ul>
  <li>HTML5</li>
  <li>CSS3</li>
  <li>MDBootstrap 3.6.0</li>
  <li>JavaScript ECMAScript 2018</li>
</ul>
Back-end:
<ul>
  <li>Python 3.8.5</li>
  <li>Django 3.2.7</li>
</ul>

<h1>Personal Website Directory</h1>
<h2>main</h2>
- Contains the html templates that are rendered, the unit test files, and the backend python files that create the functionality

<h2>media/images</h2>
- Contains the media images that are uploaded, and stored in AWS S3

<h2>mysite</h2>
- Contains the python files responsible for configuration and settings for both the development and production aspects of the website

<h2>static</h2>
- Contains the CSS files and static images that are collected and stored in the Django app via WhiteNoise 5.3.0
