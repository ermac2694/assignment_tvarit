To run please follow the below steps:
1. Create a new environment using python3 -m venv <environment_name>
2. Activate the created environment:<br> source <environment_name>/bin/activate
3. Install the required modules:<br> python -m pip install -r requirements.txt
4. Run the server using the command:<br> python app.py
5. Call the API at endpoint: http://127.0.0.1:5000/sum with json inputs

To run the test cases:<br>
python3 test_app.py -v