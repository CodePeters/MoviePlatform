# MoviePlatform
A social sharing movie platform

## _Technology Stack_ 

* Python
* Django  
* SQLite3
* Elasticsearch / Django_elasticsearch_dsl
* HTML/CSS/BOOSTRAP/JS/JQuery/Listjs

## _Installation__
Run `sudo ./install.sh` (install.sh is in django_projects/installation folder)

## _Run_
1. Go to folder `./django_project/MovieRama/` :
2. Start elastic: `./elasticsearch-7.8.0/bin/elasticsearch`
3. `python3 manage.py makemigrations`
4. `python3 manage.py migrate`
5. `python3 manage.py search_index --rebuild`
6. `python3 nanage.py runserver`

Everything is up and running !!!

Log is generated in `./django_project/MovieRama/` folder.

