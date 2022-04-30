## Development Steps

1. Install <b>git</b> on the system.
2. Open shell/command prompt and run following command to clone the project:
    <br>`$ git clone https://github.com/hamzafaisaljarral/ExcelDataEntry`


3. Make sure <b>python3</b> and <b>pip3</b> are installed on the system.
4. Once inside the project's root directory, install requirements using the following command:
    <br>Note: It's recommended to create a virtual environment and install requirements there.
    <br>`$ pip install -r requirements.txt`
    <br> python manage.py makemigrations
    <br> python manage.py migrate

5. Run this command inside the project directory to start the server:
    <br>`$ python3 manage.py runserver 8000`

6<br> To access admin panel :
    <br> python manage.py createsuperuser
    <br>`username: admin`
    <br>`password: admin@123$`
  

## Tests
Following way to run test
- 127.0.0.1:8000   (homepage)
- follow the UI to register and login 
- you will find a way to upload and than second step you can copy paste from your excel in to our form just like in excel it will work
- I Have considered Employee here on my model of which data needed to be maintain from the excel operations
- Employee have two colunms (Empcode,firstname)
- IMPORTANT
- when you are uploading csv make sure table have only two coloumns it will only see values in two coloumns due to model which only have two coloumns in employee empcode and firstname 

#  First Screen Login 

<img width="1079" alt="Screen Shot 2022-04-30 at 3 07 39 PM" src="https://user-images.githubusercontent.com/39766112/166103094-a2d5c9a7-d0e1-4b09-bd5b-b06cf757828b.png">

# Second Screen Register

<img width="1216" alt="Screen Shot 2022-04-30 at 3 11 21 PM" src="https://user-images.githubusercontent.com/39766112/166103139-5be8c7a4-2af9-44d1-820e-19b1ecf1e03b.png">

#Third Screen Home page


<img width="1440" alt="Screen Shot 2022-04-30 at 3 15 25 PM" src="https://user-images.githubusercontent.com/39766112/166103290-e6e808c2-15d4-46c0-abe5-b07fbfb1d8ba.png">


#Fourth Screen


<img width="1339" alt="Screen Shot 2022-04-30 at 3 16 49 PM" src="https://user-images.githubusercontent.com/39766112/166103336-c7eb5016-e411-40d9-be1d-dc999d78cc91.png">

Make Sure the Excel should be like this for this feature 

<img width="786" alt="Screen Shot 2022-04-30 at 3 17 55 PM" src="https://user-images.githubusercontent.com/39766112/166103362-91cbf769-a802-4191-a183-696e4ea828bd.png">

#you can upload you multiple and single csv file here which have same columns like in above image attached.

<img width="1091" alt="Screen Shot 2022-04-30 at 3 18 46 PM" src="https://user-images.githubusercontent.com/39766112/166103393-5d066b89-728d-4d33-acbd-5c3b8632c13f.png">


