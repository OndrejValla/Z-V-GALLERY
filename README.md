# Z-V-Gallery
## Code Institute: Milestone Project 4

![Preview Image](media/readme-files/z-v-gallery-front-page-image.png)
Created by Ondrej Valla


## View [Z-V-Gallery](https://z-v-gallery.herokuapp.com/) website on Heroku.

---
The Z-V-Gallery (Zuzu Valla Gallery) website is my fourth ‘Milestone Project’ as part of the Full Stack Development course of Code Institute. The focus lies on using the Django framework, using an authorisation and authentication system and using Stripe payment system. I believe this website could be a fundation for the real online store, selling printed portraits of Zuzu Valla's work in the future.

## * PLEASE NOTE! *

### This website is for educational purposes only. 
### Don’t use real credit card details, instead use the following details for testing purposes:  
Card number: 4242 4242 4242 4242   
Use any expiration date (month/year) in the future and any CVC code.

Thank You for understanding, Enjoy!

--- 



# Table of Content
1. [Overview](#overview)

2. [Goals](#goals)

3. [User Experience](#user-experience)
   

4. [Wireframes](#wireframes)

5. [Features](#features)


6. [Used Technologies](#used-technologies)

7. [Testing](#testing)


8. [Bugs](#bugs)

9. [Deployment](#deployment)

10. [Credits](#credits)
---

# Overview

The Z-V-Gallery website is here for all the fans of Zuzu Valla. People have a great opportunity to purchase printed portraits of Zuzu Valla's work. Users can choose to get prints of their choice unframed, or framed in white or black frame and delivered worldwide, straight to their door.

---

# Goals

### User goals:
1. The website to be user-friendly.
2. The website to be visually appealing to users.
3. Easy to navigate website.
4. Ability to register / log in 
5. To be able to save my billing details in my profile for the future.
6. To be able to review products.
7. Easy to use payment system.

### Developer/Admin goals:
1. Have a well-designed / responsive website.
2. To be able to create / manage different project categories and be able to upload products for each category.
3. Use MySQL and Postgres databases effectively.
4. To see users profiles, reviews and messages in the database.
---

# User Experience

## **Strategic level**

I am definitely one of the biggest Zuzu's fan and I always like to find the way how to share her amazing photography work with others. I came up with the idea of website selling Zuzu's prints as soon as I found out, that the last project will be an online store.

Users can browse this website and find out bit more about Zuzu and her photographs.
Users can create an account to safe their order order history and billing details.

The target audience are people interested in the photography.
These can be people, who already know Zuzu Valla, same as people who dont know her yet, never seen her work and want to find out more about her photography. Or returning users, for instance people who have seen her images before and want to go a step further and purchase some of them.

The primary goal is to deliver an interactive web app with gallery portfolio style, which provides its users the ability to purchase framed or unframed piece of printed art. 

The project goal is to show my knowledge I have learned from The Code Institute course and apply it in this project.


## **User Stories**

#### General Site Users / Shoppers

As a general site user, I would like to:
1.  see the content of the page.
2.  see the content, be able to see all Prints and prices.
3.  view other users reviews.
4.  be able to see individual projects.
5.  see all products added in to the shopping bag.
6.  be able to adjust the shopping bag before checkout.
7.  be able to purchase prints as a guest, without creating the profile.
8.  get the confirmation email after the purchase.
9.  be able to register and create my profile.
10. be able to contact the store owner, for further details.
11. find out more through social media.

#### Registered Users  

As a registered user, I would like to:
1. be able to easily login and log out.
2. save and edit my billing details in my profile.
3. see my purchase history details.
4. be able to comment / review products.
5. be able to edit, or delete my review.
6. easily change my forgotten password.

#### Admin User

As an Admin user, I would like to:
1. be able to create new project categories.
2. edit or delete existing project categories.
3. be able to add new products with all the details and images.
4. be able to edit or delete uploaded products.
5. MySQL and Postgres database to store page content effectively and safely.
6. have a access to all website messages, reviews and user profiles / email addresses through my Admin loggin in the database.


## **Scope level**
Based on the user stories I have applied the following requirements:

### **Requirements**
1.  A responsive design.
2.  A home page with navigation menu, About section, Photography projects section, Small Gallery(for desktop view only).
3.  An about section on the home page where users can get more information about Zuzu Valla.
4.  A photography projects section on the home page, where users can see individual projects.
5.  A shop page where all available prints are displayed.
6.  An option to search the prints on the shop page.
7.  An option to sort prints by the individual project.
8.  Individual pages for each prints / products with the framing preview and the ability to choose the frame and the quantity.
9.  Reviews section at the bottom of each product details page with the ability to add, edit or delete the review for 
    registered users.
10. An option to register and login/logout.
11. A profile page where registered users can add or edit billing information and see their order history details.
12. Contact page with the contact form. Receiving confirmation email with the message and sender details for admin and the user.
13. A shopping cart icon with relevant info that is displayed at all times.
14. A shopping cart page with all the items in the bag. Ability to adjust the bag.
15. A checkout page with details on the shopping items.
16. Secure checkout via Stripe payment.
17. Email confirmation on purchase.
18. An admin pages with options to Create or Edit prints / products.
19. Defensive programming, e.g. confirmation on deleting, logging out, etc.


## **Structure Level**
The overall look is kept the same on each page as much as possible.
- The header and footer are kept the same on each page.
- Buttons are styled in the similar way.
- The used color style is kept on each page.

The navigation is kept simple and consistent:
- The logo at the top of the page is also the link to the home page.
- Buttons can be used to navigate.

The information provided should be easily visible for the user:
- Messages(toasts) in the right top corner, are used to confirm or inform about current actions.
- Modal delete pop ups are used as defensive programming, prompting the user if they are sure of their action.
- The user gets a feedback when an error has occurred.

### **Pages**
#### **Frontend**

The website has 12 pages. Each page has a header with the logo linked to the Home page, and a footer.
The links in the header are shown depending on whether a user is logged in or not and if the user is the admin or not.
When a user is not registered nor logged in, the register and login links are shown in My Account section.
When a user is logged in, the register and login links are hidden and a profile link and logout link are shown in My Account section.
When the user is admin, an extra link for the Product Management is shown.

The footer has a section with links to social accounts and a link to GitHub repository of this page.

- **The landing page (Home page):** 
This is the first page a user can see when they come to the site. There is a hero image with the Navigation Menu.
The Navigation Menu has links to the About section, Art series section, Contact Us page and Shop page.
Below the menu, there is an About section.

-About section: 
 Informations about Zuzu Valla plus the button (CONTACT) linked to the contact.html page.

-Art Series section:
 Cards of individual projects. Each card has an button (SEE PRINTS) linked to the products.html (shop page) displaying prints of selected project.

-Gallery section:
 Only visible on medium and larger screen resolutions. This is the section showing nine random images from Zuzu Valla's portfolio. Each image features the function of changing to black and white on hover.


- **The products page (Shop page):**
The heading of this page is Prints. On this page all available prints for sell are displayed. Each print has image, name, project name, price, rating and for admin use only: edit/delete buttons.


- **The product details page:**
The heading of this page is Details. On this page individual/clicked print is displayed with further details. There is the name of the print, description, three images, white framed image, black framed image and no frame image. Underneath is the edit/delete button for Admin use only, the price, rating, followed by the frame option selector, quantity selector and one keep shopping button and add to bag button.
- **The product details/reviews page:**
This page is only displayed as a part of the product details page. This page contains heading Reviews with the count of total reviews for selected print and the current average rating. Underneath there are individual reviews. 
For the user who wrote the review, there is an option to edit, or delete the review.


- **The shopping bag page:**
If the shopping bag is empty, the user is informed by the text, saying the shopping bag is empty and the Keep shopping button.
When there are items in the bag, the user is able to see the table with product informations such as: Product image, name, price, whether or not framed, quantity with the update/remove option and subtotal.
On the bottom of the page, there is bag total sum, delivery charge, grand total sum, keep shopping button and secure checkout button.