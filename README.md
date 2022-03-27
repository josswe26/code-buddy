# Code Buddy


![Code Buddy mockup images](assets/readme_files/mockup_image.jpg)


Code Buddy is a website created to allow developers to ask questions and receive relevant answers from other developers.

The main objective of the site is to allow developers to share knowledge and ideas, collaborate and help each other to find solutions to the problems they face. This is achieved by providing a platform of questions and answers, where users can search for the information they are looking for. Developers are also able to upvote or downvote the questions and answers in order to assure that relevant content gets highlighted.

Visit the deployed website [here](https://django-code-buddy.herokuapp.com/).


## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Strategy](#strategy)
        1. [Project Goals](#project-goals)
        2. [User Goals](#user-goals)
        3. [Strategy Table](#strategy-table)
    2. [Scope](#scope)
        1. [User Stories](#user-stories)
    3. [Structure](#structure)
    4. [Skeleton](#skeleton)
    5. [Surface](#surface)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
    1. [Testing User Stories](#testing-user-stories)
    2. [Code Validation](#code-validation)
    3. [Accessibility](#accessibility)
    4. [Tools Testing](#tools-testing)
    5. [Manual Testing](#manual-testing)
5. [Deployment](#deployment)
6. [Finished Product](#finished-product)
7. [Credits](#credits)
8. [Acknowledgements](#acknowledgements)


***


## User Experience (UX)

### Strategy

#### Project Goals

* The website contains simple colors for a modern design and also to not draw attention from the content.

* Responsive design to make the website accessible on different screen sizes.

* Structure is easy to understand and navigates effortlessly.

* Site users are able to register an account in order to interact with the content.

* Site users are able to upvote or downvote the questions and answers to help identify relevant content.


#### User Goals

* As a Site Admin, I want to manage the site content.

* As a Site User, I want to be able to interact with the content.

* As a Site User, I want the information to be easy to find and read.

* As a Site User, I can create new questions and answers.

* As a Site User, I want to manage the content I created.

* As a Site User, I want to be able to help make the content more relevant.


#### Strategy Table

Opportunity / Problem | Importance | Viability / Feasibility
--- | --- | ---
Responsive design | 5 | 5
Account registration | 5 | 5
Ability to add profile picture | 3 | 2
Social media signup | 3 | 2
Create, edit and delete questions | 5 | 4
Create, edit and delete replies | 5 | 4
Ability to search for questions | 4 | 3
Add tags to the questions | 3 | 1
Upvote / downvote question and replies | 4 | 3
**Total** | **37** | **29**


### Scope

According to the strategy table, not all features can be implemented in the first release of the project. For this reason, the project will be divided in multiple phases. The first phase will include the features that have been identified in order to build the minimum viable product.

**First Phase**

* Responsive design

* Account registration

* Create, edit and delete questions

* Create, edit and delete replies

* Ability to search for questions

* Upvote / downvote question and replies

**Second Phase**

* Ability to add profile picture

* Social media signup

* Add tags to the questions


#### User Stories

GitHub projects was used as my project management tool to track user stories. Using a Kanban board helped to focus on specific tasks and track the project progress.

**Start**
![User Stories Progress - Start](assets/readme_files/user_stories_start.png)

**Week 1**
![User Stories Progress - Week 1](assets/readme_files/user_stories_week1.png)

**Week 2**
![User Stories Progress - Week 2](assets/readme_files/user_stories_week2.png)

**Week 3**
![User Stories Progress - Week 3](assets/readme_files/user_stories_week3.png)


### Structure

The website has been organized in a Hierarchical Tree Structure to ensure the site user navigates through the site effortlessly and intuitively. Here you can you can find the website map design.

![Code Buddy website map](assets/readme_files/sitemap.jpg)

* Header, footer and navigation bar are consistent through all pages.

* Links and forms provide clear feedback to the site user.

* The opportunity to add additional content to the website is provided for the site user once they register an account.

* A 404-error page is available.


#### Database Model

The database model has been designed using [drawsql](https://drawsql.app/). The type of database being used for the is relational database being managed using [PostgreSQL](https://www.postgresql.org/).

![Code Buddy website map](assets/readme_files/db_model.png)

**Question Model**

* Title: Unique question title provided by the author.

* Author: Store the author of the question as a User foreign key.

* Content: Question details provided by the author.

* Slug: Store a unique slug to identify the question by.

* Created On: Date and time set automatically at the question's creation.

* Last updated: Date and time set automatically every time the question is updated.

* Votes score: Calculated score of the question's votes.

**Reply Model**

* Question: A foreign key from the Question model, storing the question being replied.

* Author: Store the author of the reply as a User foreign key.

* Body: Reply body with details provided by the author.

* Created On: Date and time set automatically at the reply's creation.

* Last updated: Date and time set automatically every time the reply is updated.

* Votes score: Calculated score of the reply's votes.

**QuestionVote Model**

* Voter: Foreign key from the User model, storing the user voting the question.

* Score: Score provided by the voter. The options are upvote with a value of 1 or downvote with a value of -1.

* Question: A foreign key from the Question model, storing the question being voted.

**ReplyVote Model**

* Voter: Foreign key from the User model, storing the user voting the reply.

* Score: Score provided by the voter. The options are upvote with a value of 1 or downvote with a value of -1.

* Reply: A foreign key from the Reply model, storing the question being voted.


### Skeleton

#### Wireframes

[Balsamiq](https://balsamiq.com/) has been used to showcase the appearance of the site and display the placement of the different elements whitin the pages.

Page | Desktop Version | Mobile Version
--- | --- | ---
Index / User Logged Out | ![Desktop index / user logged out wireframe image](assets/wireframes/index_dektop_logged_out.png) | ![Mobile index / user logged out wireframe image](assets/wireframes/index_mobile_logged_out.png)
Sign Up | ![Desktop sign up wireframe image](assets/wireframes/signup_dektop.png) | ![Mobile sign up wireframe image](assets/wireframes/signup_mobile.png)
Log In | ![Desktop log in wireframe image](assets/wireframes/login_dektop.png) | ![Mobile log in wireframe image](assets/wireframes/login_mobile.png)
Index / User Logged In | ![Desktop index / user logged in wireframe image](assets/wireframes/index_dektop_logged_in.png) | ![Mobile index / user logged out wireframe image](assets/wireframes/index_mobile_logged_in.png)
Ask Question | ![Desktop ask question wireframe image](assets/wireframes/ask_question_desktop.png) | ![Mobile ask question wireframe image](assets/wireframes/ask_question_mobile.png)
Open Question | ![Desktop open question wireframe image](assets/wireframes/question_dektop.png) | ![Mobile open question wireframe image](assets/wireframes/question_mobile.png)
Leave Reply | ![Desktop leave reply wireframe image](assets/wireframes/leave_reply_desktop.png) | ![Mobile leave reply wireframe image](assets/wireframes/leave_reply_mobile.png)


### Surface

#### Color Scheme

![Color scheme image](assets/readme_files/color_scheme.png)

The colors used in the website are a teal blue color (#3F778D) for secondary buttons, navbar links, as well as for main buttons and links transitions. Charcoal (#253A47) is used for the main text, footer background, main buttons and secondary buttons and links transitions.

A platinum (#E9EDE9) for the navigation bar and card footers background, footer and buttons content. A baby powder color (#FFFFFD) is also used in the main background and cards footer as well as for input fields.

The colors are were chosen keeping in mind simplicity but also providing the website a modern design. This in order to keep the focus on the content but also appealing for the users.


#### Typography

The main font being used in the site is Nunito, with sans-serif as a fallback in case Nunito doesn't get imported correctly. Roboto, with sans-serif as a fallback is used mainly for headings and the logo has been given the Quicksand font, with sans-serif as a fallback.

Nunito and Roboto were chosen after some research on fonts that are better for reading. Specially Nunito which has been used as main font. Quicksand was used for the logo for design purposes.

[Back to top ⇧](#code-buddy)


## Features

[Back to top ⇧](#code-buddy)

## Technologies Used

[Back to top ⇧](#code-buddy)

## Testing

### Testing User Stories

#### As a Site Admin I can create, read, update and delete questions and answers so that I can manage the site content

* An admin site has been provided so that the Site Admin can manage question and replies.

* Question and replies can be created, read, updated and deleted from the site.

* Questions and replies main fields are being displayed for the Site Admin to identify them easily.

* Questions and replies can be filtered and searched to narrow down a specific group.


#### As a Site User I can register an account so that I can create and rate questions and replies

* Account registration has been provided for Site User.

* Registered Site Users are given the possibility to submit questions and replies.

* Registered Site Users are able to edit and delete their own questions.

* Registered Site Users are able to vote upvote and downvote questions and replies.


#### As a Site User I can create new questions so that I can receive help from other users

* An Ask Question page has been provided for registered Site Users.

* A form is available in the Ask Question page for the Site Users to be able to register new questions. 

* An Ask Question button is displayed to the registered Site Users at the top of the questions list to access the Ask Question page.


#### As a Site User I can edit and delete my own questions so that I can manage the questions I created

* Edit and Delete Question pages are provided for registered Site Users.

* A form is available inside those pages for the Site Users to be able to edit or delete a specific question.

* The Edit Question form is prepopulated with the current data for the user to be able to edit the content.

* A Delete Question form is provided for Site Users to confirm the deletion. 

* Edit and Delete button are displayed on those questions the user has created to access the respective page.


#### As a Site User I can reply to questions so that I can help other users to find a solution

* A Leave Reply page has been provided for registered Site Users.

* A form is available in the Leave Reply page for the Site Users to be able to register new replies to the questions. 

* A Leave Reply button is displayed to the registered Site Users under the Question content inside the Question Details page. This button is used to access the Leave Reply page.


#### As a Site User I can edit and delete my own replies so that I can manage the replies I created

* Edit and Delete Reply pages are provided for registered Site Users.

* A form is available inside those pages for the Site Users to be able to edit or delete a specific reply.

* The Edit Reply form is prepopulated with the current data for the user to be able to edit the content.

* A Delete Reply form is provided for Site Users to confirm the deletion. 

* Edit and Delete button are displayed on those replies the user has created to access the respective page.


#### As a Site User I can upvote and downvote questions and answers so that I can give relevance to the content.

* Upvote and downvote buttons are provided for registered Site Users next to each question and reply.

* Registered Site Users can upvote, downvote or remove their votes using those buttons from the Home and Question Detail pages.


#### As a Site User I can view a list of questions so that I can select one to read

* The Home page is a Question List, displaying all existing question to all Site Users.

* Questions are displayed in creation date/time order, showing the newest questions on top. 


#### As a Site User I can search for specific questions so that I can easily find the information I am looking for

* A Question Search field has been provided to all Site Users in the top of all pages.

* This search field allow all Site Users to search questions using keyword(s).

* A Search Results page with a list of questions matching the searched keyword(s) is provided.

* The list gets paginated if the Search Results exceed 10 questions.


#### As a Site User I can view a paginated list of questions so that I can easily select a question to view

* The Question List displayed in the Home page is paginated every 10 questions.

* Navigation buttons are provided on the bottom of each page to navigate easily between pages.


#### As a Site User I can click on a question so that I can read the full question and the replies received

* A Question Detail page is provided for all Site Users to review the full question content.

* The question title in the Question List page is provided as a link so that Site Users can access the Question Detail page for each specific question.


#### As a Site User I can view the replies a question received so that I can find a solutions to the question

* Question's replies are being listed inside the Question Detail page for each specific question under the question content.

 * Replies are being sorted by their rating so that Site Users can find the most relevant replies on top.


#### As a Site User I can view the score on each question so that I can find the most helpful

* The question's rating is being displayed for all Site Users next to each question.


#### As a Site User I can view the score on each reply so that I can find the most helpful

* The reply's rating is being displayed for all Site Users next to each reply.

* Replies are ordered by this rating so Site Users can find the most relevant replies on top


### Code Validation

### Accessibility

### Tools Testing

### Manual Testing

[Back to top ⇧](#code-buddy)

## Deployment

[Back to top ⇧](#code-buddy)

## Finished Product

[Back to top ⇧](#code-buddy)

## Credits

[Back to top ⇧](#code-buddy)

## Acknowledgements

[Back to top ⇧](#code-buddy)