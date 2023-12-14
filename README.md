# Lanie Ruiz-Perez - She Codes News Project
## About This Project
This repo contains code which was personalised from the SheCodes original template for the django module. This is the state as submitted for the assignment of the django module of the SheCodes Plus Perth cohort in Dec 2023.
The project is a website which allows users to visit a news stories site, create accounts, submit stories, and view stories by other authors. All of this taking into account the appropiate permissions for logeed in users and makin use of predefined models. 
To achieve this, there are two apps (news and users).
A fixtures file is available in news/fixtures.
## How To Run This Code
{{Give a quick step-by-step guide on how to download and run your codebase.It's ok to assume the reader is another developer here, so don't feel like youhave to explain what a virtual environment is, etc.Give directions like "clone the repo to your local machine", "create a virtualenvironment", "migrate the database", etc.
When you need to specify terminal commands, you can surround them withbackticks, like so: `python manage.py runserver`. This formats them ascode in the markdown document. (The backtick key is to the left of thenumber 1 at the top of your keyboard.)
}}
As this is a public repo, if you are reading this and are interested in trying it for yourself these are some steps you can follow:
- Clone the repo and open in your local terminal
- Create a virtual environment and install the requirements
- Load the fixtures so you don't land in an empty site
- Navigate to the location of manage.py and run the server
- Follow the link provided which should open your web browser
- Edit the IP address to access the news site by adding `/news` at the end. This should show the news website with some news content and style
- Create an account: To do this add `/users/createaccount` at the end of the original IP address. Fill and submit the form
- Log in to be able to access the rest of the functionality of the site as described below

## Database Schema
![ {{ My ERD }} ]( {{ ./relative_path_to_your_entity_relationship_diagram }} )

## Project Features
- [ ] Order stories by date
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] Styled "new story" form
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] Story images
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] Log-in/log-out
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] "Account view" page
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] "Create Account" page
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] View stories by author
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] "Log-in" button only visible when no user is logged in/"Log-out" buttononly visible when a user *is* logged in
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] "Create Story" functionality only available when user is logged in
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
## Additional Features:
- [ ] Add categories to the stories and allow the user to search for stories bycategory.
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] Add the ability to update and delete stories (consider permissions - whoshould be allowed to update or and/or delete stories).
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] Add the ability to “favourite” stories and see a page with your favouritestories.
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] Our form for creating stories requires you to add the publication date,update this to automatically save the publication date as the day thestory was first published (maybe you could then add a field to showwhen the story was updated).
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
- [ ] Gracefully handle the error where someone tries to create a new story whenthey are not logged in.![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )