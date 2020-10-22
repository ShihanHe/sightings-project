# Squirrel Sightings Project
> **Project Name**: Xi Cheng & Shihan He (Section 1) | **Group Member**: Xi Cheng, Shihan He | **UNIs**: [xc2554, sh4087]

## Management Command
We define 2 new commands to import and export the csv file. 

- **Import**: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command.

```bash
$ python manage.py import_squirrel_data /path/to/file.csv
```

- **Export**: A command that can be used to export the data from the 2018 cencus file in CSV format. The file path should be specified at the command line after the name of the management command. 

```bash
$ python manage.py export_squirrel_data /path/to/file.csv
```

## Views
### Map
A view that shows a map that displays the location of the squirrel sightings on an [OpenStreets map](https://www.openstreetmap.org/about/).
-	Located at: /map
-	Methods Supported: GET

### Sightings
A view that lists all squirrel sightings with links to view (and update) each sighting. 
-	Located at: /sightings
-	Methods Supported: GET
-	Fields to show:

### Update
A view to update a particular sighting. 
-	Located at: /sightings/<unique-squirrel-id>
-	Methods Supported: GET & POST

### Add
A view to create a new sighting
-	Located at: /sightings/add
-	Methods Supported: GET & POST

### Stats
A view with general stats about the sightings. 
-	Located at: /sightings/stats
-	Method: GET

## Contributors
**Project Name**: Xi Cheng & Shihan He (Section 1)

**Group Member**: Xi Cheng, Shihan He

**UNIs**: [xc2554, sh4087]
