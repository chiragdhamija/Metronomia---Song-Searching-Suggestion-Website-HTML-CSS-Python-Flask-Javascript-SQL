# Documentation for Metronomia

Metronomia is a music database site where a variety of music from various different artists can be accessed and played.

The origial folder contains all the html and python pages and required to run Metronomia. In its current version, Metronomia runs online on the local port by accessing the locally stored html files. Hence, it it important that the relative positions of the files not be changed.

## Project Directory Structure

In the parent directory there are two files, labelled ASSUMPTIONS.md and README.md, and a folder, labelled src.

The README.md file contains the documentation about the project. Make sure it is read completely before proceeding.

The ASSUMPTIONS.md file contains all the necessary assumptions taken during the making of this project.

The src folder contains two more folders, labelled templates and static in it and the playlist.py python file, this file will start the flask server and provide the link to the local port once it is run.

The templates folder contains all the html pages required for the website.

The home page file is labelled as index.html contains the information for the home page.

The file labelled about.html contains information for the about page of the website.

The file labelled artists.html contains information for the artists page of the website.

The file labelled spotlight.html contains information for the artist spotlight page of the website.

The file labelled search.html contains information for the search page of the website.

The file labelled spotlight.html contains information for the artist spotlight page of the website.

The file labelled search.html contains information for the search page of the website where users can search for songs and provided that there is an internet connection, songs coresponding to the search query will be returned.

The file labelled playlist.html contains information for the user's playlist that is stored in a database locally.

Then, there are a number of files with names starting with artist, followed by a number and then -albums.html, these files contain the information for the pages corresponding to the various artists featured on the website. Here, the number represents the number of the artist.

Then, there are a number of files with names starting with album, followed by a number and then -songs.html, these files contain the information for the pages corresponding to the various albums featured on the website. Here, the number is always a two digit number where the first digit represents the artist and the second digit represents the number of the song. On this page, there is an add to playlist button which will add the desired song to the user's own playlist stored on a database locally.

The folder labelled static contains a CSS file labelled index.css and another older labelled assets that contains all the images and icons used in the website.

## In-website Navigation

Our names in the footer are clickable links linking to the about page.

In the about page, the logo is disolayed up front and the description follows later.

## How to Properly Run Metronomia

First, clone the phase 3 branch repository onto your machine, then run the playlist.py file present in the src directory, this will provide the link to the local port that hosts the website, then copy and paste the link in your browser and enjoy!
