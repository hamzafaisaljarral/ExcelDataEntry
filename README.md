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