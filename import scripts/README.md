# Importing Data

I wasn't quite able to finish this task, but the idea was to try to set up a pipeline to automate all the refreshing of data in the data files and in the TargetLink database. Ultimately, running the Python scripts will automatically create the TSV files and insert the data into a SQLite database. Many of the tables that are not yet created can be done so through small modifications to the existing Python scripts.

## Primary entities

I have gotten started by adding scripts for the following entity data sources in their own files:

````
HGNC.ipynb
NCBI.ipynb
HPA.ipynb
DrugBank.ipynb
````

## Web scrapes

Many of the file downloads from the data source websites do not include all the interesting information from the site, and so some web scraping is required. There is a `web scraping` directory which holds some scripts which should be run after the original entities are in place, creating secondary data files like `HPO_diseases.tsv` (a scrape of the Human Phenotype Ontology site).

## Database scripts
Lastly, there is also an `ImportSql.sql` file which shows how things like an index or view can be added into the SQLite database once it is created.