# TargetLink prototype
 Database of genes, drug targets, associated diseases, protein interactions, and other relationships

The site was created in Django, so the first step you will probably need to do is install Django

````
python -m pip install Django
````
 
## Files and Folder structure
The `manage.py` file is Django's command line utility for administrative tasks. For example, if you want to start the development web server, you would run the following:

````
python .\manage.py runserver
````

You shouldn't need to modify `manage.py` at all.

There are three top level folders in the repository, `website`, `search`, and `import scripts`

`website/settings.py`: This is probably the only file under `website` that you might want to modify. The location of the database file is specified here. Currently, it is set to `../TargetLink.db`, which is one level up from the root directory of this repo. The reason for that is that it was too large to upload to Github.

`search\models.py`: This file was auto-generated from the database schema. Additional models were created by hand for the database views. More info on how this was done can be found [here](https://docs.djangoproject.com/en/3.2/howto/legacy-databases/).

`search/views.py`: This file is the back-end logic for the main views, currently called `index` (the landing page) and `gene_details` (what happens when the user highlights a particular gene)

`templates/search/index.html`: This file contains the HTML of the front end, with Django template code and javascript interspersed.

`import scripts`: This folder, not involved in the actual website, contains Python scripts for automatically creating TSV files and inserting the data into a SQLite database. It is not currently complete but should be easy to add to by copying and modifying the existing scripts.
