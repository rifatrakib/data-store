# data-store
Python API server for supporting scraping and data collection with required authentication and authorization provided by multiple data formats and processing as required.

Use the files stored inside `raw-data` directory to populate the database tables which are generated using the models from each of the apps. This can be done by using the `admin_only` routes available in the `views.py` scripts from each of the apps. Then the public routes will return the data as HTML, JSON (GeoJSON when applicable) and XML format. Please keep in mind not to use the admin_only routes more than once.

To get started, run `pip install -r requirements.txt` in your terminal which will install all necessary python modules. Use a `.env` file to store certain key-value pairs that are used for the project (you can find which variables are needed from the `settings.py` and the `manage.py` scripts).
