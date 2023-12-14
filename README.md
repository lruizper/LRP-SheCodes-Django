# Lanie Ruiz-Perez - She Codes News Project
## About This Project
This repo contains code which was personalised from the SheCodes original template for the django module. This is the state as submitted for the assignment of the django module of the SheCodes Plus Perth cohort in Dec 2023.
The project is a website which allows users to visit a news stories site, create their accounts and log in, submit news stories for other users to see, and view stories by other authors. All of this taking into account the appropiate permissions for logged in users, and making use of predefined django models. 
To achieve this, there are two apps (news and users) which can be found within the folder structure of the repo, following common practice.
A fixtures file is also available in news/fixtures.
## How To Run This Code
As this is a public repo, if you are reading this and are interested in trying it for yourself these are some steps you can follow:
- Clone the repo and open in your local terminal
- Create a virtual environment and install the requirements
- Load the fixtures so you don't land in an empty site
- Navigate to the location of manage.py and run the server
- Follow the link provided which should open your web browser
- Edit the IP address to access the news site by adding `/news` at the end. This should show the news website with some news content and style
- Create an account: To do this add `/users/createaccount` at the end of the original IP address. Fill and submit the form
- Log in: this way you'll be able to access the rest of the functionality of the site as described below

## Database Schema
![ {{ My ERD }} ]( {{ ./relative_path_to_your_entity_relationship_diagram }} )

## Project Features
- [X] Order stories by date
![ A screenshot from the main page displaying four recent stories sorted by published date  ]( images/MainPage_storiesOrderedbymostRecentdate.png)
- [X] Styled "new story" form
![ When a user has logged in, they will be able to see the option to write a new story. This is the screenshot of the styled form ]( images/WriteNewStory_StyledForm.png )
- [x] Story images
![ When the story has an associated image URL with it, it will display in the story card of the main page. If a story does not have an associated image in the database, then it will retreive a random one from picsum site ]( images/StoryImages_inMainPage.png )
- [x] Log-in/log-out
![ Styled form that allows registered users to log in ]( images/LogInForm_styled.png )
- [x] "Account view" page
![ Min viable product of the profile page. A lot of work left to make this page more informative, interactive and styled ]( images/ProfileView.png )
- [x] "Create Account" page
![ A standard form as provided by django and set to custom in user views, styled matching other forms across the site ]( images/CreateAccountForm_styled.png )
- [x] View stories by author
![ If user is logged in, a search box appears in nav which can be used to search authors. If multiple authors are retrieved that match the query str then their stories will appear grouped by author ]( images/SearchResults_storiesbyAuthor.png )
- [x] "Log-in" button only visible when no user is logged in/"Log-out" button only visible when a user *is* logged in
![ When a user is logged in, the header will no longer show the log in button. Instead it will display more information and functionality available only to registered users ]( images/Header_loggedIn.png )
![ When no user is logged in, the only options in nav will be to log in or visit homesite ]( images/Header_NotLoggedIn.png )
- [X] "Create Story" functionality only available when user is logged in
![ An error message lets the user know that they have to register and log in to be able to create and submit a new story]( images/WriteNewStory_accessDenied.png )

## Additional Features:
- [ ] Add the ability to update and delete stories (consider permissions - whoshould be allowed to update or and/or delete stories).
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] Add the ability to “favourite” stories and see a page with your favouritestories.
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] Our form for creating stories requires you to add the publication date,update this to automatically save the publication date as the day thestory was first published (maybe you could then add a field to showwhen the story was updated).
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] Gracefully handle the error where someone tries to create a new story whenthey are not logged in.![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )