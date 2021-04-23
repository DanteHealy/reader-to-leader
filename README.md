![Am I responsive image](https://github.com/DanteHealy/reader-to-leader/blob/master/static/images/amIresponsive.GIF)

# Read to Lead 

Read to Lead is a book review community website covering non-fiction books for for personal development.  
The intent of the website is to provide value to visitors by getting ideas on which books to read by various subjects to 
either solve specific problems and/or develop new skills. 


## Contents

To Be Updated



### Site Goals

The goal of the site is to allow visitors to read reviews created by registered users and to find inspiration for self-help books that they can read by topic. 
The features of the website include: 
-	Show a list of concise book reviews available to all site visitors. 
-	Provide links to the associated books reviewed (non-affiliated links for demonstration purposes only)
-	Allow visitors to register an account in order to create their own reviews on this website for the benefit of other users. 

This is achieved by: 
-	Having a registration form with username and password in order to create an account. 
-	Having a login page for existing users to access their account. 
-	Allowing users to create and edit their own books reviews when logged in. 
-	Having an Admin account which allows a superuser to also add or edit new genres. (New: “and add affiliate links to the book reviews.”) 


### User Experience (UX)

#### User Goals
-	Read book reviews created by other users 
-	Create book reviews for others to read 
-	Access links to purchase the books they are interested in


#### User Stories
New visitor
-	As a user I can see a navigation bar at the top of the page where I can navigate to the available pages. 
-	As a user I can see the site name or brand logo in the navigation bar. 
-	As a user I want to be able to find out the information about the site from the home page 
-	As a user I want to see the Call To Action (CTA) button to learn more about the book reviews available 
-	As a user I wanted search across all available book reviews to find books relating to my specific interest. 
-	As a user I want to click on the book image to access more detailed information about the book. 
-	As a user I want to be able to click on a link that takes me to where I can purchase the book. 
-	As a user I want to understand the terms and conditions when I register my user account. 
-	As a user I can see a I can contact the site owners. 
Returning site visitor
-	As a user I want to see my user account profile page to view all the reviews I have submitted. 
-	As a user I want to be able to create, edit or delete my own book reviews. 
-	As a user I want to ensure that when I delete a book review I am asked for confirmation before confirming final delete. 
Site Owner / Site Administrator
-	As a site owner I want the user to be able to log out of their account. 
-	As a site owner I want an admin account to control the site content by;
        1. Adding links where users can purchase the books (affiliate links possible, but I have not used affiliate links as this is for demonstration purposes only)
        2. Delete book reviews if they have content which violates the terms and conditions of the site. 
-	As a site administrator I want to be able to add, edit and delete the genre topics associated with the book reviews. 
-	As a site owner, I want the site administrator to be able to apply links to reviews through which visitors can purchase the books relating to reviews they liked (potentially monetising through the use of affiliate links).                                                                                                                              
Please note: That the affiliate links are for demonstration purposes only to demonstrate how the site could be potentially be funded and are not actual affiliate links. 


#### Wireframes

Initial
I designed the wireframes using [Balsamiq](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/ms3-book-review-wireframes.pdf) for the basic layout and structure. 
-	Home page 
-	Book reviews 
-	Register
-	Login 
-	Manage genres
-	Add review page 
-	Edit reviews 

Final 
The final mock ups were created using [Canva](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/milestone-3-canva-mockup.pdf) to get a high fidelity view of how the final 
version and key elements might appear before starting to code the site. 
-	Homepage
-	Book reviews 
-	Book card 
-	Register
-	Login


#### Design Features 

Font
I chose Barlow sans-serif for a clean look and feel like the body of a modern non-fiction or text book. 

Colour scheme selection: 
https://grasshopper.com/resources/tools/branding-color-quiz/

My responses were geared toward my target audience who are professionals seeking clear guidance which provides certainty in their career and personal growth decisions. 

Colour scheme
![color scheme](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/colors.gif)

“Blue is a trusting and secure colour, conjuring up the feeling of calm and even spirituality. 
It's often used in corporate designs and is well-known as a favourite colour. Blue is loyal, dependable, 
and it's a great colour to use if you want your customers to trust you. 
Blue is also appealing to shoppers on a budget. It's the most widely-used color for company logos. 
Be careful, as some shades of blue can be perceived as depressing and cold.” (Source: grasshopper.com) 

To get the right shade of blue I used the colour wheel to find a suitable blue shade that contrasted well with the brown tint of my bookstore image 
which I obtained from Canva’s colour wheel: 
https://www.canva.com/colors/color-wheel/


##### Home page
I used royalty-free images from Canva for a traditional bookstore where the user might imagine going to buy a good non-fiction book like a Waterstones. 
The home page includes a responsive navbar. 

![home page top](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/01-home.gif)


![home page bottom](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/02-home.gif)


Includes basic contact details plus social media icons. 

![footer](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/03-footer.gif)


##### Book Review Page
The page includes a search bar plus cards with the image of each book reviewed and a reveal function that shows the review details submitted by the user.

![book review page](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/04-books.GIF)


Search bar contains text input area plus reset and search buttons

![search bar](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/05-search.gif)


Each book card has hoverable to show which book is being targeted by the user. 

![book card](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/06-card.gif)


Opening the card on click reveals the review details. 

![book card open](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/07-card-open.gif)


Only the buy button will be available for users who did not create the review and are logged in or who are not admin. 
If its the user who created the review or admin then the edit and delete opion buttons will also be available. 

![book card open all buttons](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/08-card-open-login.gif)


##### Add Review Page

On the add review page a user who is logged in will have a form card to complete and submit a review. 

![add review](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/09-review-card.gif)


##### Edit Review Page

The author or admin can also edit the review from the edit button on the book card. 

![edit reviews](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/12-edit-review.gif)


##### Manage Genres Page

For admin the Manage genres page will enable the maintenance of the genres table. 

![manage genres page](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/10-manage-genres.gif)


##### Add Genre Page

Click on the add genre button takes you to the form field where admin enters a new genre. 

![add genre](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/11-add-genres.gif)


##### Register new user page

The 'Register' page contains a card where a new user can enter their user name and password credentials. 

![register](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/22-register-card.GIF)


Just above the register button there are terms and conditions which trigger a popup modal with the terms and conditions. 

![Terms and Conditions](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/23-register-t%26c-modal.gif)


The Terms and Conditions also allows for mobile users. 

![T&C mobile](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/28-register-t%26c-modal-mobile.gif)


##### User's profile Page

The profile page has the user's published reviews. 

![profile page](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/26-profile-page.gif)


Where no reviews are submitted the user's profile will have a blank card showing that there are no reviews and a button taking the user to the add review page. 

![profile no review card](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/29-profile-no-review.gif)


##### Defensive programming

When clicking delete on a book review the user is provided with a pop up modal warning asking to confirm the delete action. 

![delete review modal](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/18-delete-warn-modal.gif)

The same applies to admin when trying to delete a genre. 


The same error message appears for 404, 500 and 503 errors. With a button allowing the reader to return to the main page. 

![site error message](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/27-site-error.GIF)


Trying to force break to access unauthorised areas of the website the programme will take the user to the login page. 

![login card](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/21-login-card.gif)

This applies to all CRUD functions that no unauthorised user can modify another user's work. 
The exception is with the admin user profile which is required to apply links to the buy buttoms on the reviews and edit 
or delete any inappropriate content if users violate the community's terms and conditions. 


##### Alerts

Various alerts appear across the website confirming where user actions were successful: 

![added review alert](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/13-review-add-alert.gif)

![review updated alert](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/14-review-update-alert.gif)

![genre added alert](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/15-genre-add-alert.gif)

![genre updated alert](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/16-genre-update-alert.gif)

![book deleted alert](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/19-book-delete-alert.gif)

![genre deleted alert](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/20-genre-delete-alert.gif)

![login successful alert](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/24-login-alert.gif)

![logout successful alert](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/25-logout-alert.gif)



### Technologies Used

Languages : HTML, CSS, JavaScript and Python  

Database : MongoDB Atlas

Libraries
-	MaterializeCSS: https://materializecss.com/
-	JQuery: https://jquery.com/
-	Werkzeug (webpage security): https://werkzeug.palletsprojects.com/en/1.0.x/ 
-	Flask: https://www.fullstackpython.com/flask.html
-	Jinja: https://jinja.palletsprojects.com/en/2.11.x/
-	PyMongo: https://pymongo.readthedocs.io/en/stable/


Tools 
CDN references: cdnjs - The #1 free and open source CDN built to make life easier for developers
Secret Key Generator:  RandomKeygen - The Secure Password & Keygen Generator
Font-Awesome: Font Awesome
Canva (including the colour wheel): https://www.canva.com/colors/color-wheel/
Favicon: https://favicon.io/


### Site Construction 

##### Site Layout 

The [site structure and jinja template relationship](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/site-design.pdf) are stored in this pdf. 

Basic layout includes the the web pages and interactive elements (cards) indicating user access privileges. 


#### Database architecture

The [database architecture](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/data-model.pdf) can be found here. 

Using MongoDB I was able to create the empty collections with all data entered and created via the website's frontend. 


#### Project Management 

(Comment on the use of GitHub Projects etc. - Create a manual kanban board to track features and monitor bug fixes.)


### Testing 

System testing: 


Manual testing: 


Bugs identified

 - Fixed 



 - Still remaining 





### Deployment 

~Information to be added 



### Credits 

#### Content

Parts of the code were re-used from the Take Manager mini-project from the Data Centric module plus with my own additional code. 
A lot of the styling was taken from materializecss and the images used were from Canva. 

Guidance on some of the features and functions was obtained via YouTube. 


#### Acknowledgements

I would like to give a huge and sincere thank you to: 

- Simon Vardy, Sam Laubscher, Michael Standen for their continued support and encouragement,  
- Ulysees Ryan-Flynn for the excellent Tutor support, patience and understanding of my personal circumstances, 
- My mentor Adegbenge Adeye and CI Tutor support for the technical guidance 

They have been super supportive during this project and I appreciate their feedback and advice which helped to get this site to this final state.
















