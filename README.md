# Coronavirus Visualisation Dashboard

## University of Birmingham Data Analytics Bootcamp: Project 3

The World Health Organisation boasts an extensive dataset containing Coronavirus data from across the world. The aim of this project was to create interactive visualisations with this data at hand.

The project itself demonstrates usage of SQL, Flask, HTML & Javascript.

### The Data

The Data was collected in csv form from the [WHO Coronavirus Dashboard](https://covid19.who.int/info?openIndex=2) & subsequently cleaned using [a python script](https://github.com/Csepato/Project3-group-4/blob/main/JF-file-cleanse.ipynb). The cleaned data was then stored in a Postgres database, which you can create with [this script](https://github.com/Csepato/Project3-group-4/blob/main/table-creation.sql).

### The Visualisations

The dashboard is built with a total of six HTML pages, with visualisations using plotly & leaflet:

 - [Landing page](https://csepato.github.io/project3-group-4/templates/index.html)
 - [Mapped country statistics](https://csepato.github.io/project3-group-4/templates/visualisation-1/visualisation-1.html)
 - [Daily cases/deaths in 2021](https://csepato.github.io/project3-group-4/templates/visualisation-3/visualisation-3.html)
 - [Highest number of cases/deaths/vaccinations](https://csepato.github.io/project3-group-4/templates/visualisation-2/visualisation-2.html)
 - [Contributors page](https://csepato.github.io/project3-group-4/templates/contributors.html)
 - Link to [API](https://github.com/Csepato/Project3-group-4/blob/main/app.py) (created with Flask)
