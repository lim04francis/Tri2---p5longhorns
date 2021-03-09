# Tri 2 Period 5 Longhorns - [Link to Art Museum](http://76.176.107.1/)

### [LINK TO EASTER EGG](http://76.176.107.1/marc)



## Technicals

### Image Uploading Database (Marc H)
- [Database](https://github.com/lim04francis/Tri2---p5longhorns/blob/42dd9608cb96f2554bfadddc52021f91c185e5bf/main.py#L142-L165) that allows users to submit images of art pieces they want to see included into the website
- Integrated into website with proper [front end](https://github.com/lim04francis/Tri2---p5longhorns/blob/682d4e079c920b7f9a759b56cc563603956a7141/templates/index.html#L189-L192)

### Painting List (Marc H)
- Has a python file with [dictionaries of each paintings](https://github.com/lim04francis/Tri2---p5longhorns/blob/40bbc06216777d0b60c6d700c9be540a6379ab43/paintings.py#L1-L27) with key values assigned. Then has the dictionaries put into a [single list](https://github.com/lim04francis/Tri2---p5longhorns/blob/40bbc06216777d0b60c6d700c9be540a6379ab43/paintings.py#L29) to be referenced in code elsewhere
- Uses a [variable in the app.route](https://github.com/lim04francis/Tri2---p5longhorns/blob/40bbc06216777d0b60c6d700c9be540a6379ab43/main.py#L106-L108) for the jinja for loop in the html file
- [Jinja for loop](https://github.com/lim04francis/Tri2---p5longhorns/blob/40bbc06216777d0b60c6d700c9be540a6379ab43/templates/paintinglist.html#L124-L139) to iterate through the dictionaries in the list and print key values into the table

### Painting Overlays (Marc H)
- Uses CSS in order to create a [sliding overlay](https://github.com/lim04francis/Tri2---p5longhorns/blob/04f124523ddc6f6416bd2b3a7f77d0d9be4bb635/templates/cubism.html#L50-L160) that covers the paintings
  - Uses [classes and divs](https://github.com/lim04francis/Tri2---p5longhorns/blob/04f124523ddc6f6416bd2b3a7f77d0d9be4bb635/templates/cubism.html#L181-L189) in order to have CSS apply
- Has links embedded into the overlays that takes the users to [paintingdescriptions.html](https://github.com/lim04francis/Tri2---p5longhorns/blob/main/templates/paintingdescriptions.html) so users can know the meaning behind the paintings.



### JavaScript Description Buttons(Francis L)
- After setting up the front end work for the [description boxes](https://github.com/lim04francis/Tri2---p5longhorns/blob/04f124523ddc6f6416bd2b3a7f77d0d9be4bb635/templates/photography.html#L185-L225) and [buttons](https://github.com/lim04francis/Tri2---p5longhorns/blob/04f124523ddc6f6416bd2b3a7f77d0d9be4bb635/templates/photography.html#L256-L311) on the Photography page, [I used JavaScript to make the buttons reveal and hide the description box](https://github.com/lim04francis/Tri2---p5longhorns/blob/04f124523ddc6f6416bd2b3a7f77d0d9be4bb635/templates/photography.html#L317-L358). JavaScript is executed when a button is clicked and an onclick event occurs when the user clicks an element. A function named [myfunction(#)](https://github.com/lim04francis/Tri2---p5longhorns/blob/a33dd4f226630c22b76f2693621cfcb42e4e69a5/templates/photography.html#L258) is assigned to an html element and when executed, toggles the description box from revealed to hidden and vice versa.

### Web/Rest API - Random Quotes Machine(Francis L)
- After setting up the [front end CSS work](https://github.com/lim04francis/Tri2---p5longhorns/blob/a33dd4f226630c22b76f2693621cfcb42e4e69a5/templates/quotesapi.html#L8-L150) needed for my random Trump quotes generator, I moved onto the [Javascript](https://github.com/lim04francis/Tri2---p5longhorns/blob/a33dd4f226630c22b76f2693621cfcb42e4e69a5/templates/quotesapi.html#L184-L208) and [HTML](https://github.com/lim04francis/Tri2---p5longhorns/blob/a33dd4f226630c22b76f2693621cfcb42e4e69a5/templates/quotesapi.html#L159-L182). I first selected and element with the [DOM](https://github.com/lim04francis/Tri2---p5longhorns/blob/a33dd4f226630c22b76f2693621cfcb42e4e69a5/templates/quotesapi.html#L185) 
Then I assigned a reference to the quote button to a new variable with [(code)](https://github.com/lim04francis/Tri2---p5longhorns/blob/a33dd4f226630c22b76f2693621cfcb42e4e69a5/templates/quotesapi.html#L185)
I used the documentation of of an API that required no authentication and saved the url endpoint in a variable using 
[(code)](https://github.com/lim04francis/Tri2---p5longhorns/blob/a33dd4f226630c22b76f2693621cfcb42e4e69a5/templates/quotesapi.html#L188)
To make a request to the API to grab a random quote I set up a [getQuote function](https://github.com/lim04francis/Tri2---p5longhorns/blob/a33dd4f226630c22b76f2693621cfcb42e4e69a5/templates/quotesapi.html#L190-L200) using fetch, a try block, and a catch block 

### Dictionaries/Lists for Subpage Headers(Francis L)
- I devised a method for each member of my group to create and add a unique header for each subpage using data stored in a single line dictionary. In the python file main.py, following the [app route to my photography subpage](https://github.com/lim04francis/Tri2---p5longhorns/blob/a33dd4f226630c22b76f2693621cfcb42e4e69a5/main.py#L26-L29), [I added the following code](https://github.com/lim04francis/Tri2---p5longhorns/blob/a33dd4f226630c22b76f2693621cfcb42e4e69a5/main.py#L28), storing information such as the title, author, summary and period in a dictionary called “posts”. After assigning the dictionary value to the key “posts”, I went to my photography html file and using css and html, [printed out the data](https://github.com/lim04francis/Tri2---p5longhorns/blob/a33dd4f226630c22b76f2693621cfcb42e4e69a5/templates/photography.html#L242-L250) in an aesthetic format. 




### Authorized User Login (Manuel V)
- [Login Page](https://github.com/lim04francis/Tri2---p5longhorns/blob/b6cc49f46688c709231343a2e11388b97f196ef5/templates/login.html) that allows authorized users log into the page
- uses [javascript](https://github.com/lim04francis/Tri2---p5longhorns/blob/b6cc49f46688c709231343a2e11388b97f196ef5/templates/login.html#L119)to tell the user if the username and password was correct and they have logged in, or if it was incorrect, give an error message

### Buttons to Other Genres (Manuel V)
- made [buttons](https://github.com/lim04francis/Tri2---p5longhorns/blob/b6cc49f46688c709231343a2e11388b97f196ef5/templates/Movies.html#L22) that link the main movies page to other [genres](https://github.com/lim04francis/Tri2---p5longhorns/blob/b6cc49f46688c709231343a2e11388b97f196ef5/templates/actionmovies.html) of the movies page as well as the more information tab

### More Information tab(Manuel V)
- Created [more information tab](https://github.com/lim04francis/Tri2---p5longhorns/blob/b6cc49f46688c709231343a2e11388b97f196ef5/templates/moviesummaries.html) that had trailers and descriptions in it about all movies
  - Has links to trailers [embedded](https://github.com/lim04francis/Tri2---p5longhorns/blob/b6cc49f46688c709231343a2e11388b97f196ef5/templates/moviesummaries.html#L101) so you can watch the trailers for the movies directly on the website




### Home Page Background and Navbar (James H)
- I created the [moving waves background](https://github.com/lim04francis/Tri2---p5longhorns/blob/90b33d24c9616d3cbdf82cc24e57216bc89a6ca2/static/home.css#L1-L72) on the homepage as well as the created and edited the [navbar](https://github.com/lim04francis/Tri2---p5longhorns/blob/90b33d24c9616d3cbdf82cc24e57216bc89a6ca2/static/home.css#L79-L110) many times including for crossover suggestions

### Created Music Genres Page and Search Bar (James H)
- Created the [Music genres](https://github.com/lim04francis/Tri2---p5longhorns/blob/main/templates/Music.html) page as well as every [subpage](https://github.com/lim04francis/Tri2---p5longhorns/tree/main/templates/Music).
- Created the [post form](https://github.com/lim04francis/Tri2---p5longhorns/blob/90b33d24c9616d3cbdf82cc24e57216bc89a6ca2/templates/Music.html#L25-L29) for the music page and [routed it's formaction](https://github.com/lim04francis/Tri2---p5longhorns/blob/90b33d24c9616d3cbdf82cc24e57216bc89a6ca2/main.py#L55-L95)

### Added Playable Songs On To Each Music Page (James H)
- On each music subpage, I added playable songs that pertain to the genre that was searched. [Example](https://github.com/lim04francis/Tri2---p5longhorns/blob/90b33d24c9616d3cbdf82cc24e57216bc89a6ca2/templates/Music/MusicCountry.html#L30-L33) + [Example](https://github.com/lim04francis/Tri2---p5longhorns/blob/main/static/Friends.mp3)

### Deployment and Raspberry Pi Work (James H)
- I did the Raspberry Pi deployment process for my group. 


### [AP CSP Requirements Reflection Document](https://docs.google.com/document/d/1VXpFwf4a9hbRfqNfUkyfq4cgYS_rohieEd5pFr5qums/edit?usp=sharing)

### [Project Plan and Design](https://docs.google.com/document/d/17C_nAyFtFvbdhyxUsUb1094QCTnxOj8Qtv0jS7bWbzI/edit?usp=sharing)

### Members:
- James Hunt
- Francis Lim
- Manuel Villa-Hernandez
- Marc Humeau

## Project Ideas
- Our project idea is an virtual art museum. We would show the history of certain genres, such as music, painting, and even gaming.

### Contributions 

| Manuel/Mewe14        | Marc/marchumeau                              |  Francis/lim04francis  | James/Bob1437                                   |
| ------------- |:-------------                                |:-----    |:----                                            |
| [Contributions](https://github.com/Mewe14)               |[Contributions](https://github.com/marchumeau)|[Contributions](https://github.com/lim04francis)|[Contributions](https://github.com/Bob1437)      |


## Scrum Board
[Period 5 Longhorns](https://github.com/lim04francis/Tri2---p5longhorns/projects/1)


# Log of Changes
[Log of Weekly Changes](https://github.com/lim04francis/Tri2---p5longhorns/projects/2)





# Raspberry Pi Run Instructions
   **Deployment Process**
   
   1 - Obtain git location, login to Github on Pi Browser, copy HTTPS address, Run Git Clone within Terminal, Continue in the Terminal and run Web Server on Pi Browser using Local Host
   
   2 - Find the IP Address of Specific Raspberry Pi, Edit main.py file of project to reflect the IP Address of Raspberry Pi
   
   3 - Login in to home router, Reserve an IP Address for you Raspberry Pi on your home router through allocation, Setup port forwarding to your Raspberry Pi through Service Assignment, Find public IP address of Raspberry Pi

   **Run Instructions from Terminal**
   
   1 - ssh pi@[IP] (enter password)
   
   2 - cd Tri1---HTML-Portfolio/
   
   3 - python3 main.py
   

### Crossover Suggestions
- Change the navigation bar so that the buttons are the same for each page (as there are currently different buttons on some of the pages), to prevent confusion 
- Maybe try thinking about using jinja and CSS to make it a bit easier on the formatting and make website navigation easier for the user



## Week 4 Grading 
### Tickets
| Ticket 1  | Ticket 2  | Ticket 3 | Ticket 4  |
| :------------- |:-------------                                |:-----    |:----                                            |
| [Marc - Ticket #1](https://github.com/lim04francis/Tri2---p5longhorns/projects/1#card-52605914)               |[Francis - Ticket #2](https://github.com/lim04francis/Tri2---p5longhorns/projects/1#card-52606518)[, Running Photography Subpage](http://76.176.107.1/photography)|[Manuel - Ticket #3](https://github.com/lim04francis/Tri2---p5longhorns/projects/1#card-52607517)|[James - Ticket #4](https://github.com/lim04francis/Tri2---p5longhorns/projects/1#card-52772616)      |
| [Added more paintings,](https://github.com/lim04francis/Tri2---p5longhorns/blob/65b20709bcfd9f6603c30a3241d2870623146cca/templates/cubism.html#L220)[ and added more descriptions](https://github.com/lim04francis/Tri2---p5longhorns/blob/ce63d00e5b3a677b5af804ca4c8636a74d966a77/templates/paintingdescriptions.html#L152)               |[Set up button in html,](https://github.com/lim04francis/Tri2---p5longhorns/blob/fb795bfdf542c032f86516f949e20d80e565c4ef/templates/photography.html#L211)[ set up code to hide and show description box](https://github.com/lim04francis/Tri2---p5longhorns/blob/d0dcd78a4e118dbca119c27fcdecd00c3405ab59/templates/photography.html#L255)|[Added button that links to other page](https://github.com/lim04francis/Tri2---p5longhorns/blob/58c6a17980ef8a29c46785c8d80f823dbcd379e7/templates/Movies.html#L18) [Added another movies page](https://github.com/lim04francis/Tri2---p5longhorns/blob/58c6a17980ef8a29c46785c8d80f823dbcd379e7/templates/actionmovies.html#L1)      | [Contributions](https://github.com/Bob1437)      |

## Model Week #2 Grading 
### Tickets
| Ticket 1  | Ticket 2  | Ticket 3 | Ticket 4  |
| :------------- |:-------------                                |:-----    |:----                                            |
| [Marc - Ticket #1](https://github.com/lim04francis/Tri2---p5longhorns/projects/1#card-53785220)               |[Francis - Ticket #2](https://github.com/lim04francis/Tri2---p5longhorns/projects/1#card-53784992)[ Photography Page](http://76.176.107.1/photography)|[Manuel - Ticket #3](https://github.com/lim04francis/Tri2---p5longhorns/projects/1#card-53785621)|[James - Ticket #4](https://github.com/lim04francis/Tri2---p5longhorns/projects/1#card-53793743)      |
| [Worked on styling for LinkedIn page on Easter Egg](https://github.com/lim04francis/Tri2---p5longhorns/blob/26d566acd2708728b356ce29aa12ef4d5aeadb89/templates/marclinkedin.html#L3-L120)     |[Created multiple separate buttons with each description,](https://github.com/lim04francis/Tri2---p5longhorns/blob/3df21013322bdf6736d22cde01f05c4a8c29e8dc/templates/photography.html#L185-L225)[ Used JavaScript to create separate functions for each picture, ](https://github.com/lim04francis/Tri2---p5longhorns/blob/4c7f5210cdb9c0f972df95f3c09df3f1d6750a49/templates/photography.html#L309-L350)[Set up pictures in rows](https://github.com/lim04francis/Tri2---p5longhorns/blob/7b88445867f79b543adcbdf6771b8ebf7b8f5c6e/templates/photography.html#L246-L304)|[Added Private page for future, added a login page where you submit username and password](https://github.com/lim04francis/Tri2---p5longhorns/blob/04d911884ef52cf2fa1bbd71f00ee346cd609958/templates/login.html#L83-L131) [](https://github.com/lim04francis/Tri2---p5longhorns/blob/58c6a17980ef8a29c46785c8d80f823dbcd379e7/templates/actionmovies.html#L1)      | [Created all the files in this folder](https://github.com/lim04francis/Tri2---p5longhorns/tree/main/templates/Music) [Routed files to they can be accessed](https://github.com/lim04francis/Tri2---p5longhorns/blob/22899867dee6f003a3e1f5b60f7e330725e3c359/main.py#L49-L89) |


## Feb 16-18 Tickets 
### Tickets
| Ticket 1  | Ticket 2  | Ticket 3 | Ticket 4  |
| :------------- |:-------------                                |:-----    |:----                                            |
| [Marc - Ticket #1 (CB Requirement)](https://github.com/lim04francis/Tri2---p5longhorns/projects/1#card-55067521)               |[Francis - Ticket #2](https://github.com/lim04francis/Tri2---p5longhorns/projects/1#card-55145327)[ Photography Page](http://76.176.107.1/photography)|[Manuel - Ticket #3](https://github.com/lim04francis/Tri2---p5longhorns/projects/1#card-55146220)|[James - Ticket #4](https://github.com/lim04francis/Tri2---p5longhorns/projects/1#card-53793743)      |
| [Created a list with dictionaries of paintings,](https://github.com/lim04francis/Tri2---p5longhorns/blob/e7e86da93aa27b8f02b527e0401604374a435428/paintings.py#L1-L17)[used jinja to assign a variable, ](https://github.com/lim04francis/Tri2---p5longhorns/blob/96fdbd147e8b56ecce9133a3f4ec6465d4da60fd/main.py#L105-L107)[and used a jinja for loop to print values into a table](https://github.com/lim04francis/Tri2---p5longhorns/blob/8ac185875c9bc702a04f21afbbc63f2850ec4a8c/templates/paintinglist.html#L121-L136 )    |[Table of Contents on homepage with buttons to subpages using inputs,]( https://github.com/lim04francis/Tri2---p5longhorns/blob/7180fa5e5bbf1bfe5446d9fe2b1abfee09499cf0/templates/home.html#L60-L133)[ Dictionary with photography page info and printed in header with jinja, ](https://github.com/lim04francis/Tri2---p5longhorns/blob/7180fa5e5bbf1bfe5446d9fe2b1abfee09499cf0/templates/photography.html#L243-L250)[3]( )|[Added Private page for future, added a login page where you submit username and password](https://github.com/lim04francis/Tri2---p5longhorns/blob/04d911884ef52cf2fa1bbd71f00ee346cd609958/templates/login.html#L83-L131) [](https://github.com/lim04francis/Tri2---p5longhorns/blob/58c6a17980ef8a29c46785c8d80f823dbcd379e7/templates/actionmovies.html#L1)      | [Fixed the navbar on every page (crossover suggestion). Link shows an example](https://github.com/lim04francis/Tri2---p5longhorns/blob/b7150392927ef6520ffd5a880daec9e4f38038eb/templates/home.html#L14-L23) [3d modeled and added Monalisa on bottom of Cubism page](https://github.com/lim04francis/Tri2---p5longhorns/blob/a88678e02d290a1489dd12eeeea050a338f88ad8/templates/cubism.html#L431-L444) |

