# Mini-Projects

## [mobile-tracker.py](https://github.com/yogeshwaran01/Mini-Projects/blob/master/mobile-tracker.py)
Track the mobile number with python
### Requirements
1. requests
2. bs4
### Usage:
<code> python mobile-tracker.py {mobile_number} </code>
<br>

## [html-generator.py](https://github.com/yogeshwaran01/Mini-Projects/blob/master/html-generator.py)
### Usage:
##### importing
<code> from html_generator import HtmlGenerator,HtmlViewer</code>
##### object creation by passing name of the html file
<code> html = HtmlGenerator("python.html") </code> 
##### To clear any content in html file
<code> html.clear() </code> 
##### To create the simple tag by giving inner_html and tag-name
<code> html.tag("Hello World","h1") </code> <br>
<code> html.tag("Welcome !","p") </code> 
 ##### To create the anchor tag by giving link and text
<code> html.link_tag("https://www.google.com","Google") </code> 
 ##### To create the image tag by giving source and alternative
<code> html.img_tag("https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png","Google")</code> 
##### To View in webbrowser
<code> HtmlViewer("python.html") </code>
<br>

## [url-forker.py](https://github.com/yogeshwaran01/Mini-Projects/blob/master/url_forker.py)
To get urls of the url
### Requirements:
1. bs4
2. urllib3
3. requests
### Usage:
<code>python url-forker.py url </code></br>
#### For get urls of the url
<code>>>> 3</code>  type the url number it get all url of that url</br>
#### For Download:
<code>save</code>    type save </br>
<code>(save)>>> 4  </code>   type the url number to download a file from the url </br>
#### For open in webbrowser:
<code>open </code>    type open </br>
<code>(open)>>> 5 </code>   type the url number to open in default webbrowser </br> 
 </br>
 ## [facebook-login.py](https://github.com/yogeshwaran01/Mini-Projects/blob/master/facebook-login.py)
 Login to facebook from command line 
 ### Requirements:
 1. selenium
 2. Chrome driver
 ### Usage:
 ##### change the path of driver in the script 
 <code> python facebook-login.py </code>
 <br>
 
 ## [instadp.py](https://github.com/yogeshwaran01/Mini-Projects/blob/master/instadp.py)
 To Download Instagram dp
 ### Requirements:
 <code> pip install instagramy </code>     [Github repo](https://github.com/yogeshwaran01/instagramy) </br>
 ### Usage:
  <code>python instadp username </code>
</br>

## [tic-tac-toe.py](https://github.com/yogeshwaran01/Mini-Projects/blob/master/tic-tac-toe.py)
Play the tic-tac-toe Game </br>
### Usage:
<code> python tic-tac-toe.py </code>
<br>

## [extract-contact.py](https://github.com/yogeshwaran01/Mini-Projects/blob/master/extract-contact.py)
It extracts all contact details (E-mail and Phone Numbers) from any websites and text-files
### Requirements:
1. bs4
2. urllib3
3. selenium (First in open in Browser and then scrape the information)
4. requests
### Usage:
###### Not open in webbrowser:
<code>python extract-contact.py web_address 0 </code> <br>
  
###### To open in webbrowser and then Scrape:
Required:chrome driver must be installed in specified loaction </br>
  
<code>python extract-contact.py web_address 1 </code>

###### For text files:
<code>python extract-contact.py text_file.txt </code>
  




 
