# stereographic-projector

This is an web application to visualize different paths through terrain data for robotics. 

Concept: You have terrain and need to find the easiest segment through. Let the user choose the route by clicking points on the graph, then translate elevation gain into power

We can also specify robot speed for each segment of terrain.

dashboard/
    - assets/ has custom sylesheet, static elements
    - layout/ has app components
    - content.py
    - index.py defines dash app

- contains app instance, layout, assets

- requirments.txt has all dependencies

- app.py is entry point that imports everything else and inits server

- project structure from https://www.purfe.com/dash-project-structure-multi-tab-app-with-callbacks-in-different-files/



TO RUN virtual environment

pip install -r requirements.txt

This is a handy trick that creates the requirements.txt file for you!
https://stackoverflow.com/questions/31684375/automatically-create-requirements-txt

pip install pipreqs

pipreqs /path/to/project
