# data-store
Python API server for supporting scraping and data collection with required authentication and authorization provided by multiple data formats and processing as required.

Use the files stored inside `raw-data` directory to populate the database tables which are generated using the models from each of the apps. This can be done by using the `admin_only` routes available in the `views.py` scripts from each of the apps. Then the public routes will return the data as HTML, JSON (GeoJSON when applicable) and XML format.
