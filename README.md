# surveyAPI-django


## Functionality for the system administrator:
1) authorization in the system (without registration)
2) Add/modify/delete surveys. Attributes of the survey: name, start date, end date, description. The "start date" field cannot be changed after the creation of the survey
3) adding/editing/deleting questions in the survey. Question attributes: question text, question type (text answer, single-choice answer, multiple-choice answer)


## Functionality for users of the system:
1) receiving the list of active surveys
2) taking the survey: surveys can be taken anonymously, a numeric user ID is sent to the API as the user's identifier, which is used to store the user's answers to the questions; one user can take part in any number of surveys
3) receiving surveys completed by the user with details on the answers (what is selected) by unique user ID

## Installation:
1) Clone the repository.
2) Create virtual environment, login into it.
3) Install the dependencies: 


        pip install -r requirements.txt


4) Do the migrations:


        python manage.py makemigrations


        python manage.py migrate


5) Create a superuser:


        python manage.py createsuperuser


6) Run the test server:


        python manage.py runserver
      
    
    
# API


## Surveys (POST)
Rights: Admin<br/>
URL: /api/surveys/<br/>
QUERY PARAMETERS: name, dateEnd, desc


## Update/delete surveys (PUT, DELETE)
Rights: Admin<br/>
URL: /api/surveys/<survey_id>/


## Create questions (POST)
Rights: Admin<br/>
URL: /api/questions/<br/>
QUERY PARAMETERS: text, type, survey


## Update/delete questions (PUT, DELETE)
Rights: Admin<br/>
URL: /api/questions/<question_id>/

## Adding and viewing answer choices to a question (POST, GET)
Rights: Admin<br/>
URL: /api/choices/<br/>
QUERY PARAMETERS: text


## Get survey and it's questions, return questions of the exact survey (GET)
URL: /api/surveys/&lt;id>/questions


## Answer exact question (POST)
URL: /api/surveys/&lt;id>/questions/&lt;question_pk>/answers


## Get user surveys (GET)
URL: /api/UserSurveys


## Get active surveys (GET)
URL: /api/ActiveSurveys
