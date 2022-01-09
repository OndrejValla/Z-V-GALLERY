# Z-V-Gallery
## Code Institute: Milestone Project 4

![Preview Image](media/readme-files/z-v-gallery-front-page-image.png)
Created by Ondrej Valla


## View [Z-V-Gallery](https://z-v-gallery.herokuapp.com/) website on Heroku.

---
The Z-V-Gallery (Zuzu Valla Gallery) website is my fourth ‘Milestone Project’ as part of the Full Stack Development course of The Code Institute. The main focus is on using the Django framework, an authorization and authentication system, same as using The Stripe payment system. I believe this website could be a foundation for the real online store, selling printed portraits of Zuzu Valla's work in the future.

---
### **PLEASE NOTE!**

### This website is for educational purposes only. 
### Don’t use a real credit card details, instead use the following details for testing purposes:  
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

8. [Deployment](#deployment)

9. [Credits](#credits)
---

# Overview

The Z-V-Gallery website is here for all the fans of Zuzu Valla. People have a great opportunity to purchase printed portraits of Zuzu Valla's work. Users can choose to get prints of their choice unframed, or framed in a white or black frame and delivered worldwide, straight to their door.

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
4. To see users' profiles, reviews, and messages in the database.
---

# User Experience

## **Strategic level**

I am definitely one of the biggest Zuzu's fan and I always like to find a way to share her amazing photography with others. I came up with this idea of selling Zuzu's prints as soon as I found out, that the last project will be an online store.

Users can browse this website and find out a bit more about Zuzu and her photographs.
Users can create an account to save their order history and billing details.

The target audience are people interested in photography.
These can be people, who already know Zuzu Valla, same as people who dont know her yet, never seen her work and want to find out more about her and her photography. Target audience are also returning users, for instance, people who have seen Zuzu's images before and want to go a step further and purchase some of them.

The primary goal is to deliver an interactive web app with gallery portfolio style, which provides its users the ability to purchase framed or unframed pieces of printed art. 

The project's goal is to show the knowledge I have learned from The Code Institute course.


## **User Stories**

#### General Site Users / Shoppers

As a general site user, I would like to:
1.  see the content of the page.
2.  see the content, be able to see all Prints and prices.
3.  view other users' reviews.
4.  be able to see individual projects.
5.  see all products added to the shopping bag.
6.  be able to adjust the shopping bag before checkout.
7.  be able to purchase prints as a guest, without creating the profile.
8.  get the confirmation email after the purchase.
9.  be able to register and create my profile.
10. be able to contact the store owner, for further details.
11. find out more through social media.

#### Registered Users  

As a registered user, I would like to:
1. be able to easily log in and log out.
2. save and edit my billing details in my profile.
3. see my purchase history details.
4. be able to comment / review products.
5. be able to edit or delete my review.
6. easily change my forgotten password, if needed.

#### Admin User

As an Admin user, I would like to:
1. be able to create new project categories.
2. edit or delete existing project categories.
3. be able to add new products with all the details and images.
4. be able to edit or delete uploaded products.
5. MySQL and Postgres database to store page content effectively and safely.
6. have access to all website messages, reviews, and user profiles / email addresses through my Admin login in the database.


## **Scope level**
Based on the user stories I have applied the following requirements:

### **Requirements**
1.  A responsive design.
2.  A home page with navigation menu, About section, Photography projects section, little gallery section (currently desktop view only).
3.  An about section on the home page where users can get more information about Zuzu Valla.
4.  A photography projects section on the home page, where users can see individual projects.
5.  A shop page where all available prints are displayed.
6.  An option to search the prints on the shop page.
7.  An option to sort prints by the individual project.
8.  Individual pages for each prints / products with the framing preview and the ability to choose the frame and the quantity.
9.  Reviews section at the bottom of each product details page with the ability to add, edit or delete the review if user is registered.
10. An option to register and log in / log out.
11. A profile page where registered users can add or edit billing information and see their order history details.
12. Contact page with the contact form. Receiving confirmation email with the message and sender details for admin and the user.
13. A shopping cart icon with relevant info is displayed at all times.
14. A shopping cart page with all the items in the bag. Ability to adjust the bag.
15. A checkout page with details on the shopping items.
16. Secure checkout via Stripe payment.
17. Email confirmation on purchase.
18. An admin pages with options to Create or Edit prints / products.
19. Defensive programming, e.g. confirmation on deleting, logging out, etc.


## **Structure Level**
The overall look is kept the same on each page as much as possible.
- The header and footer are kept the same on each page.
- Buttons are styled in a similar way.
- The used color style is kept on each page.

The navigation is kept simple and consistent:
- The logo at the top of the page is also the link to the home page.
- Buttons can be used to navigate.

The information provided should be easily visible for the user:
- Messages(toasts) in the right top corner, are used to confirm or inform about current actions.
- Modal delete pop-ups are used as defensive programming, prompting the user if they are sure of their action.
- The user gets feedback when an error has occurred.

### **Pages**
#### **Frontend**

The website has 12 main content pages plus account registration / login pages. Each page has a header with the logo linked to the Home page, and a footer.
The links in the header are shown depending on whether a user is logged in or not and if the user is the admin or not.
When a user is not registered nor logged in, the register and login links are shown in the My Account section.
When a user is logged in, the register and login links are hidden and a profile link and logout link are shown in My Account section.
When the user is admin, an extra link for the Product Management is shown.

The footer has a section with links to social accounts and a link to the GitHub repository of this page.

- **The landing page (Home page):** 
This is the first page a user can see when they visit this website. There is a hero image with the Navigation Menu.
The Navigation Menu has four link buttons, taking users to the About section, Art series section, Contact Us page, and Shop page.
Below the menu, there is an Art series section.

-Art Series section:
 Cards of individual projects. Each card has a button (SEE PRINTS) linked to the products.html (shop page) displaying prints of selected project.

 -Gallery section:
 Only visible on medium and larger screen resolutions. This is the section showing nine random images from Zuzu Valla's portfolio. Each image features the function of changing to black and white on hover.

-About section: 
 Information about Zuzu Valla plus the button (CONTACT) linked to the contact.html page.

- **The products page (Shop page):**
The heading of this page is Prints. On this page, all available prints for sale are displayed. Each print has an image, name, project name, price, rating and for admin use only: edit button.


- **The product details page:**
The heading of this page is Details. On this page individual/clicked print is displayed with further details. There is the name of the print, description, three images: white-framed image, black-framed image, and un-framed image. Underneath are the edit/delete buttons for Admin use only, the price, rating, followed by the frame option selector, quantity selector and one keep shopping button, and add to bag button.
- **The product details/reviews page:**
This page is only displayed as a part of the product details page. This page contains heading Reviews with the count of total reviews for selected print and the current average rating. Underneath there are individual reviews. 
For the user who wrote the review, there is an option to edit, or delete the review.


- **The contact page:**
This page has a contact form, where the user can ask questions or give remarks. 
A confirmation email is sent to the user’s email address after submitting.
Admin receives the email with the message.


- **The sign-up page:**  
This page has a signup form where the user can register and create an account. After registration, 
the user is asked to confirm their email address. After confirmation, the user is redirected to the
login page.


- **The sign-in page:**  
This page has a login form where users that have an account can log in. After login, the user will be 
redirected to the home page. There is a button to the register page, in case the user has no account.


- **The profile page:**  
This is the personal page of the user. Here the user can see and edit their shipping information, 
see an overview of their orders (with links to each order confirmation page).


- **The product management page:**  
On this page, the admin can add a new print / product by filling in the form. After submitting the admin 
is redirected to the individual page of the added print / product.

- **The edit product page:**  
On this page, the admin can edit an existing print / product by editing the pre-filled form. After submitting the admin is redirected to the individual page of the added print / product.


- **The shopping bag page:**
If the shopping bag is empty, the user is informed by the text, saying the shopping bag is empty and the Keep shopping button.
When there are items in the bag, the user is able to see the table with product information such as Product image, name, price, whether or not framed, quantity with the update/remove option, and subtotal.
At the bottom of the page, there is bag total sum, delivery charge, grand total sum, keep shopping button, and secure checkout button.


- **The checkout page:**  
This page has a form the user has to fill out to complete their order. The user has to provide delivery information and credit card details. After submitting the form, the user gets a confirmation email.
There is also an order summary view, showing all items in the bag, subtotals and grand total including delivery charges.


- **The checkout success page:**  
This page is shown when the payment was successful. It has an overview of the order, delivery details, and payment details.

#### **Backend**
During development, the Sqlite3 database is used. This is the default database used by Django.
During production, HerokuPostgres is used in conjunction with deployment on Heroku.

---
### **The Chart of the database models**
![Preview Image](media/readme-files/database-diagram.png)

---

### **Images Used**

Website's Header and Footer background image is downloaded from:
[www.teahub.io](https://www.teahub.io/viewwp/iTTm_1920x1080-white-abstract-wallpaper-desktop-background-abstract-white/)

All other images used on this website are owned by Zuzana Valla - Zuzu Valla Photography.

### **Colors**

The website's color theme is MOSTLY White with the combination of different shades of Grey color and texts are black or "text-dark" Bootstrap class.

![Preview Image](media/readme-files/color-pallete.png)

- rgba(0, 0, 0,) black is mostly used for text color, a part of text with the Bootstrap class of "text-dark".
- rgba(255, 255, 255,) white is used across the page to create nice, clean gallery-style background.
- rgba(181, 181, 181,) a shade of gray is used for border colors.
- rgba(233, 230, 230,) used for review cards and hovers
- Image from www.teahub.com is used
- The standard colors of Bootstrap for success, info, danger, and warning were also used.


### **Typography**
For the headings (h1 to h6) and paragraphs, I've used 'Playfair Display' fonts and sans-serif fonts as a backup.
![Preview Image](media/readme-files/fonts-example.png)


### **Icons**

- To achieve a better appearance and user experience, Font Awesome icons are used in this website.
- The source: [Font Awesome](https://fontawesome.com/)

---

# Wireframes

The final appearance of the website varies from original wireframes, however, the main structure / idea has been followed.

- [Wireframes for Home Page PC](media/readme-files/wireframes/home-page-pc.png)
- [Wireframes for Home Page Mobile](media/readme-files/wireframes/home-page-mobile.png)
- [Wireframes for Home Page Tablet](media/readme-files/wireframes/home-page-tablet.png)
- [Wireframes for Art series section home page PC](media/readme-files/wireframes/art-series-section-pc.png)
- [Wireframes for Art series section home page Mobile](media/readme-files/wireframes/art-series-section-mobile.png)
- [Wireframes for Art series section home page Tablet](media/readme-files/wireframes/art-series-section-tablet.png)
- [Wireframes for Product Details PC](media/readme-files/wireframes/product-details-pc.png)
- [Wireframes for Product Details Mobile](media/readme-files/wireframes/product-details-mobile.png)
- [Wireframes for Product Details Tablet](media/readme-files/wireframes/product-details-tablet.png)

---


# Features

- **Responsiveness** on all viewports, which allows users to use the website probably on all devices.
- **Burger menu**, which allows users to easily navigate the website on devices below 992px. This menu creates a cleaner and more organized look for smaller screen devices.
- **Search bar**, which allows users to search prints, by entering a keyword into the search bar.
- **View by project** will display only prints of selected projects.
- **Contact form** is a great feature for users to get in touch with the owner of the website.
- **Delete modal** as a defensive programming tool, which allows users to double confirm to delete their review.
- **Register functionality**, which allows users to create an account, by filling in the registration form. 
- **Login functionality**, which allows users to log in to their account, by filling in the login form. 
- **Logout functionality**, which allows users to log out of their account, by clicking the logout button.
- **Stripe functionality**, which simulates a safe environment for payments by credit card.

- **CRUD functionality (Create, Read, Update, Delete) functionality:**

    **Create:**  
        - Admin can create / add new prints / products.  
        - Users can create a review for a print / product.

    **Read:**  
        - All users can search and view prints / products and Reviews.

    **Update:**
        - Admin can edit prints / products.  
        - Users can edit their own review.

    **Delete:**
        - Admin can delete prints / products.  
        - Users can delete their own review.



## Features left to implement

- Register and Login by using Social media account.
- Sign up for the newsletter feature.
- Add your favorite prints to the Wishlist displayed on the profile page.
- Set the Stripe, to make the payment gate fully functional.

---


# Used Technologies

### **Languages used**  
- [HTML5](https://en.wikipedia.org/wiki/HTML) for markup.  
- [CSS](https://en.wikipedia.org/wiki/CSS) for styling.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) for interactivity.
- [Python3](https://www.python.org/) for backend programming.

### **Frameworks and libraries used**   
- [Bootstrap v4.4.1](https://getbootstrap.com/) frontend-framework with precoded code-snippets, like navigation bars, modals. Also used to help with the responsiveness of the website.
- [jQuery](https://jquery.com/), a javascript library for easier DOM traversing and manipulation, and shortening of the JavaScript. 	
- [Google fonts](https://fonts.google.com/) for the fonts used on the website. 
- [Font Awesome](https://fontawesome.com/) for the icons used on the website. 
- [Django](https://www.djangoproject.com/) is a high-level Python web framework that encourages rapid development and clean, pragmatic design. 

### **Tools and Programmes used**
- [Balsamiq](https://balsamiq.com/) for making the wireframes. 
- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
 to debug and check/test the website.
- [Git](https://git-scm.com/) for version control.  
- [GitHub](https://github.com/) for storing the files and version control of the website.  
- [PostgreSQL](https://www.postgresql.org/) is used as an open-source relational cloud database after development to Heroku.
- [Amazon AWS](https://aws.amazon.com/) used to store static files after deployment.
- [Heroku](https://www.heroku.com/) is a cloud platform for deploying the website.
- [W3C Markup Validation Service](https://validator.w3.org/) to validate Html files.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to check the CSS code.
- [JSHint](https://jshint.com/) to check the Javascript code.
- [PEP8 checker](http://pep8online.com/) to check the python code for PEP8 requirements. 
- [Favicon.io/](https://favicon.io/) to create the favicon for the website.
- [Coolors](https://coolors.co/) to make the color scheme.
- [quickdatabasediagrams.com](https://quickdatabasediagrams.com) to create the database diagram.
- [autopep8 1.6.0](https://pypi.org/project/autopep8/) to make my Python files pep8 compliant.


---
# Testing
For testing results, please see [TEST.md](https://github.com/OndrejValla/Z-V-GALLERY/blob/main/TEST.md)


---
# Deployment
Heroku is used to deploy this application, as GitHub can only deploy static websites.

The GitHub repository is linked to the Heroku App via automatic deployment.
Every time commits and pushes are sent to GitHub, the Heroku App starts deploying the site.

    git add .
    git commit -m "commit message"
    git push


## **To deploy to Heroku**

1. **Create a Heroku App**

        1. Create a new app by clicking the ‘New’ button in 
    [Heroku Dashboard](https://dashboard.heroku.com/apps).
        2. Give it a unique name and set region to your nearest region.
        3. Click ‘Create App’ in right top corner.
        4. Click on the 'Resources' tab and in Add-ons type: postgress, then select 'Heroku Postgres'. 
        5. For the subscription plan, choose the free plan and click submit form.

2. **Setup the Postgres Database**

        1. In your workspace install dj_database_url and psycopg2:   
    ```
        pip3 install dj_database_url
    ```
        and
    ```
        pip3 install psycopg2-binary
    ```
        2. Create a requirements file.  
    ```
        pip3 freeze > requirements.txt
    ```
        3. Import dj_database_url in **settings.py**.
    ```
        import dj_database_url
    ```

        4. Backup the database if you're using a local database instead of fixtures.  
    ```
        python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
    ```
        PLEASE make sure you're connected to your mysql database at this stage.  
        5. In Settings.py scroll down to DATABASES, comment out the default configuration and add the database url from Heroku   
    ```
        DATABASES = {
                'default': dj_database_url.parse('DATABASE_URL')
        }
    ```
        You can add the database url from Heroku's Config Vars in the Settings tab. 
        PLEASE MAKE SURE THAT you dont commit and push The DATABASE_URL from Heroku.

    ```
        6. Run migrations.
        python3 manage.py migrate
    ```
        7. If you are using a local database type:  
    ```
        python3 manage.py loaddata db.json

        to import the data from the mySQL database to Postgres.
    ```  
        8. If You Are using fixtures do as following:

        First import the categories:  
    ```
        python3 manage.py loaddata categories
    ```  
        And then the products:  
    ```
        python3 manage.py loaddata products

    ``` 
        9. If not, you can upload your files to the database later on.

3. **Create a superuser**

            - Use command: `python3 manage.py createsuperuser`
            - Create a username and password.

4. **Set up a local and remote database in settings.py**  
    In **settings.py** :
    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    ```
    Therefore, when the app is running on Heroku it connects to Postgres(remote database). Otherwise, when running locally on GitPod it will connects to MYSQL(local database).

5. **Install Gunicorn** 

        Once the app is deployed to Heroku, Gunicorn will replace the development server and will act as the web server.  
        - Use command: `pip3 install gunicorn`

6. **Create a Heroku 'Procfile'**

        The Procfile is the file that let Heroku know which file runs the app and how to run the app.
        1. In the terminal type: `touch Procfile` to create 'Procfile'.
        2. Inside the Procfile type:   
    ```
    web: gunicorn <Github yourappname>.wsgi:application
    ```

7. **Connect to Heroku in the terminal**

        1. Login to your account on the Heroku website.
        2. Go to account settings (click on your avatar).
        3. Scroll down to the API Key section.
        4. Click 'Reveal' and copy your API Key.
        5. Login to Heroku via the Command line  
    ```
    heroku login -i
    ```
        6. Login with your email but use the API Key as the password.
        7. Temporarily disable the collection of static files until AWS has been setup.  
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1 --app <Heroku appname>
    ```  
        8. Add the hostnames to allowed hosts in `settings.py`.  
    ```
    ALLOWED_HOSTS = ['<heroku appname>.herokuapp.com', 'localhost']
    ```
        9. Commit to GitHub.
    ``` 
    git add .
    git commit -m "commit message"
    git push
    ``` 
        10. Commit to Heroku. Make sure you have git remote initialized.  
    ```
    heroku git:remote -a <Heroku appname>
    ```  
    Push to Heroku.  
    ```
    git push heroku
    ```

8. **Setup automatic deployment from GitHub to Heroku.**  

        1. In Heroku, click the Deploy tab.  
        2. Under 'Deployment method', Click on 'Connect to GitHub'.
        3. Under 'Connect to GitHub', enter the GitHub repository name and click ‘Search’. Find Your Repository and click 'Connect'.
        4. Next click the ‘Enable Automatic Deploys’ button further down.


---

## **How To Set up Amazon AWS**
    I highly recommend to check the official documentation of AWS to get more understanding.
    [Create bucket overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html)

    1. Create an account, and login to Amazon web services.
    2. Search for S3 and select it.
    3. Click Create a new bucket button.  
    4. Give the bucket a unique name.
    5. Select the region closest to you.
    6. Uncheck block all public access box and acknowledge that the bucket will be public.
    7. Click 'Create bucket'.  
    8. Set basic settings
        - Click on the bucket name.
        - Click the 'Properties' tab.
        - Scroll down to 'Static website hosting' and click 'Edit'
        - Click 'Enable', Keep 'Host a static website' selected.
          Enter the default values for index and error document as shown in the example:
          index.html and error.html
        - Click 'Save changes'.
    9. Set permissions
        - Click on the 'Permissions' tab.
        - Scroll down to 'CORS' and click 'Edit'.
        - Past the following configuration:

```

[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]

    - MAKE SURE YOU ARE FOLOWING JSON FORMAT!
```
    - Click 'Save changes'

#### **Set Bucket Policy**
        - In the Permissions tab scroll to Bucket Policy and click 'Edit'.
        - NOTICE THE Bucket ARN, **You will need it in next steps**
        - Click on 'Policy generator'  
        - In the new window that opens select 'S3 bucket policy' as the 'Type of Policy'.
        - Add * to 'Principal'.
        - Select 'GetObject' in 'Actions'.
        - Copy your ARN from the other tab and paste it in the ARN field.
        - Click 'Add Statement'.
        - Click 'Generate policy'.
        - Copy the policy and paste it in the Bucket Policy of the first tab.
        - Add '/*' to the end of the resource key.
        - Click 'Save changes'.
        - Scroll down to Access control list (ACL) and click 'Edit'.
        - Select 'List' for Everyone (public access) and select 'I understand...' at the bottom.
        - Click 'Save changes'.

#### **Create AWS groups, policies, and users**
        - Search term  "Iam" via the main search bar and open it.

        - To create a group:
            - Click on 'Users groups' on the left.
            - Click 'Create group' and enter a group name. E.G. manage-z-v-gallery
            - Scroll down and click 'Create group'.

        - To create the policy to access the bucket:
            - Click on 'Policies' on the left.
            - Click 'Create policy'.
            - Click the JSON tab and then on 'Import managed policy'.
            - Search for 'S3' in the pop up window and select 'AmazonS3FullAccess' and click 'Import'.  
            - Copy your ARN from previous steps (Open S3 in a new tab, click the bucket name, Permission, Bucket policy - copy the ARN)
            - Paste it in the 'Resource' field in the JSON tab.  
            - Click 'Next: Tags', then 'Next: Review'.
            - Give the policy a name and description.
            - Click 'Create policy'.

        - To attach the policy to the group:
            - Click 'User groups' on the left.
            - Click the group name.
            - Click the 'Permissions' tab.
            - Click 'Add permission', then click 'Attach Policies'.  
            - Search for the policy that you created above, select it.
            - Click 'Attach policy'.

        - To create a user for the group:
            - Click 'Users' on the left.
            - Click 'Add user' and create a username.
            - Select 'Access Key - Programmatic access' and click 'Next: Permissions'.
            - Select the group you want to add the user to.
            - Click 'Next: Tags', then 'Next: Review' and 'Create User'.
            - Download the .csv file and save it well, since it contains this users access key and secret access key and can't be  downloaded again.

#### **Connect Django to S3**

    - To install boto3 and django-storages:

```
            pip3 install boto3  
            pip3 install django-storages
```

    - Now update the requirements.txt file:

```
            pip3 freeze > requirements.txt
```  


    - Add storages to INSTALLED APPS in `settings.py`.
    - Add the following settings to `settings.py`:


```
            if 'USE_AWS' in os.environ:
                # Cache control
                AWS_S3_OBJECT_PARAMETERS = {
                    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
                    'CacheControl': 'max-age=94608000',
                }
                
                # Bucket Config
                AWS_STORAGE_BUCKET_NAME = '<bucket name>' eg. 'z-v-gallery'
                AWS_S3_REGION_NAME = '<bucket region>' eg. 'eu-west-2'
                AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID') 
                AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY') 
                AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

                # Static and media files
                STATICFILES_STORAGE = 'custom_storages.StaticStorage'
                STATICFILES_LOCATION = 'static'
                DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
                MEDIAFILES_LOCATION = 'media'

                # Override static and media URLs in production
                STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
                MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
  
                Cache control' will tell the browser that it's okay to cache static files for a long time.  
                Bucket Config' will tell Django which bucket it should be communicating with.  
                Static and media files' will tell where to find static and media files.  
                Override static and media URLs in production' will tell which url's to use in production.    
```

    - Go to Heroku and add these values to the Config Vars in the Settings section: 
    - Create a custom class to tell django that in production we want to use s3 to store our static files.

    - Add the folowing code to custom_storages.py in your workspace:

```
            from django.conf import settings
            from storages.backends.s3boto3 import S3Boto3Storage


            class StaticStorage(S3Boto3Storage):
                location = settings.STATICFILES_LOCATION


            class MediaStorage(S3Boto3Storage):
                location = settings.MEDIAFILES_LOCATION
``` 
    - Push to GitHub.

#### **Add media files to S3 Bucket**

``` 
        - In your Amazon S3 bucket click 'Create folder' and name it 'media'.
        - Open the folder and click 'Upload'.
        - Click 'Add files' and select all your product images.
        - Under 'Permissions' select 'Grant public-read access'.
        - Select 'I understand...' and click 'Upload'.
``` 


---

## **How to Set up STRIPE**


#### **To add Stripe keys to Config Var**:
        - Login to Stripe or create an [account](https://dashboard.stripe.com/register).
        - Click developers and then API Keys.
        - Copy the public and secret key and add them to Config Vars in Heroku SETTINGS  
        ```
        STRIPE_PUBLIC_KEY = <your Stripe public key>
        STRIPE_SECRET_KEY = <your Stripe secret key>
        ```  
#### **To create a webhook endpoint**:
        - In Stripe - Open the Developers section and click 'webhooks'.
        - Click on 'Add endpoint'.
        - Enter your heroku url and add /checkout/wh/ in the end of the url.
        Example:
        https://<projectname>.herokuapp.com/checkout/wh/
  
        - Select 'receive all events' and click 'Add endpoint.
        - Scroll down to 'Signing secret' and click 'Reveal signing secret'.
        - Copy the signing secret and add to the Config Vars in Heroku.

---

## **How to Fork or Clone GitHub Repository**

#### **To FORK this repository**:
    A fork is basically a copy of a repository. 
    Forking a repository allows you to freely experiment with changes 
    without affecting the original project.

    1. Login to GitHub and follow this link to 
[Z-V-Gallery Repository](https://github.com/OndrejValla/Z-V-GALLERY).
    2. At the top right of the page, click on the fork button.
    3. Now You should have a copy of the repository in your GitHub account.

#### **To CLONE this repository**:
    1. Login to GitHub and follow this link to 
[Z-V-Gallery Repository](https://github.com/OndrejValla/Z-V-GALLERY).
    2. Click on the ‘Code’ button 
    3. To clone using HTTPS, copy the link that is displayed by clicking on the copy icon 
[Code Clone Icon](https://github.com/OndrejValla/Z-V-GALLERY.git).
    4. Open a terminal in your preferred IDE (e.g. GitPod, VSCode)
    5. Use  the ‘git clone’ command and add the link that you copied in step 3.
    6. Click the button 'Clone Repository', add the url you copied above and hit enter.
    8. A clone will be created locally.

For more info on how to clone a repository click [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)



---

## **How To Setup local deployment**:

**Clone or fork this repository**

**Install the requirements by typing:**  
    ```
    pip3 install -r requirements.txt
    ```  
    in the terminal.

**Set the environment variables:**
 ```
    if you're using GitPod: 
    - In your workspace click 'Settings'.
    - In Environment Variables insert the following variables:

        'DEVELOPMENT', 'True'
        'SECRET_KEY', '<your secret key>'  e.g. from a key generator
        'STRIPE_PUBLIC_KEY', '<your stripe public key>'
        'STRIPE_SECRET_KEY', '<your stripe secret key>'
        'STRIPE_WH_SECRET', '<your stripe webhook secret>'
```

 
```
    If you're using a local IDE, like VSCode:
    - Create a .gitignore file in the root directory, if there isn't one.
    - Open the .gitignore file and add 'env.py' to it, if it isn't in there. 
    - Create an env.py file and set the environment variables by adding the following text: 

        import os

        os.environ["STRIPE_PUBLIC_KEY"] = '<your stripe public key>'
        os.environ["STRIPE_SECRET_KEY"] = '<your stripe secret key>'
        os.environ["STRIPE_WH_SECRET"] = '<your stripe webhook secret>'

        os.environ["SECRET_KEY"] = '<your secret key>'  e.g. from a key generator

        os.environ["DEVELOPMENT"] = 'True'

```

4. **Set up the STRIPE** 
    As described above.

    PLEASE NOTE: It is highly recomended to use random Django Secret Key Generator to generate your secret keys.

4. **Migrate the database models**
    Check before migrations
    ```
    python3 manage.py makemigrations --dry-run
    ```
    Make migrations
    ```
    python3 manage.py makemigrations
    ```
    Check before migrate
    ```
    python3 manage.py migrate --plan
    ```
    Migrate
    ```
    python3 manage.py migrate
    ```

5. **Load product data.**
    Type `python3 manage.py loaddata db.json`
    or Load all your data manualy.
6. **Create a superuser account**
    `python3 manage.py createsuperuser`
    Add a username and password.   
7. **Run the app.**
   In the terminal, type: `python3 manage.py runserver`



---

# Credits

## THE MAIN CREDITS FOR:

### [The Code Institute learning programme](https://codeinstitute.net/full-stack-software-development-diploma-uk/)
All Tutorial videos are such a fantastic help and inspiration. Thanks to these tutorial videos of The Boutique Ado project, I was able to create most of my project. Thank You very much!

### [Code Institute Submissions](https://github.com/orgs/Code-Institute-Submissions/repositories?page=1) 
I always find it very motivational to scroll through other student's projects. I like to browse the Code Institute Submissions page and look deeper into interesting projects. There is by my opinion a lots of great projects and ideas. Some of these project functions I have unsuccessfully tried to apply, and some I have successfully applied into my project by adapting to how I wanted the Z-V-Gallery website to appear and perform. This is a great learning curve. I am glad to be a part of this community and learn the code. I hope that also my project will inspire someone out there.

## Additional Credits:

### HTML5
- The HTML code for this project is HIGHLY INSPIRED by The [Code Institute, Boutique Ado Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1), adjusted to fit this project's needs.

- [Code Institute Submissions](https://github.com/orgs/Code-Institute-Submissions/repositories?page=1) As mentioned above.

### CSS
- Some CSS was also used after research on [Google](https://www.google.co.uk/) and the websites [W3-SCHOOLS](https://www.w3schools.com/) and  [Stack Over Flow](https://stackoverflow.com/)

### JavaScript

- The main JavaScript functionalities are from The [Code Institute, Boutique Ado Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1).

### Python
- The Python code for this project is HIGHLY INSPIRED by The [Code Institute, Boutique Ado Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1), adjusted to fit this project's needs.

- [Code Institute Submissions](https://github.com/orgs/Code-Institute-Submissions/repositories?page=1) As mentioned above.

### Media
- The majority of images used in this website are property of Zuzu Valla Photography (my spouse)
[zuzuvalla.com](https://zuzuvalla.com/)

- Website's Top Header and The Footer theme background from [teahub.io](https://www.teahub.io/viewwp/iTTm_1920x1080-white-abstract-wallpaper-desktop-background-abstract-white/)

### Contact Application
- Contact Form by following steps from [www.twilio.com](https://www.twilio.com/blog/build-contact-form-python-django-twilio-sendgrid)

---

### Acknowledgments

- My BIGGEST THANK YOU goes to my loved wife Zuzana, for all her support in the past year.
- BIG THANK YOU for my GREAT Mentor, **Nishant Kumar** [Nishant Kumar Github](https://github.com/nishant8BITS), Thank You Nishant, for the whole year of mentoring!! Danke schoen!
- THANK YOU to my friend Dariusz Huk for answering many of my questions regarding database.

- **The Code Institute** for creating this learning program.
- **Tutoring support** at The Code Institute for their help and patience.

---
---
---
09.01.2022
T Y G