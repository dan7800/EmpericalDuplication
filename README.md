# Emperical Study: Bug Reports De-Duplication 
Bug reports are important during software development and maintenance process as they provide relevant information that help developers to fix software defects. 
One of the challenges involved in the use of bug trackers is the bug report duplication problem. This is important because the triager needs to spend time in analyzing the bug and identifying if it has been previously reported which ultimately increase the cost of Software Maintenance. In view of this need, this paper focuses on replicate of [Aggarwal et al.](https://bitbucket.org/kaggarwal32/bug-deduping-dataset) study to validate whether the results hold true using more recent datasets.

## Requirements

## Libraries Used

## How to run
### Running the Bug Tracker Issues crawler
To generate new bug report datasets we use the project [bugWebCrawler](https://github.com/dan7800/EmpericalDuplication/tree/master/bugWebCrawler) first . This project uses the library [Scrapy] (https://docs.scrapy.org/en/latest/intro/tutorial.html) which allows extracting information from web pages dinamically.
To run [bugWebCrawler](https://github.com/dan7800/EmpericalDuplication/tree/master/bugWebCrawler)
1. Update the paths for the keys `PROXY_LIST, USER_AGENT_LIST, EXCLUDE_NODES_KEYWORDS` in the `settings.py` file to the corresponding absolute path to each particular file.
2. Navigate to the spiders folder where a particular `.py` file exist for each dataset project, e.g. `eclipse.py` and so on.
3. Update the `year` class attribute with the year in which you want to get bug reports. E.g.
``` year = 2018 ```. This will crawl all the bug reports for Eclipse from 2018-01-01 to 2018-12-01. 
1. Now we can run scrapy in command-line:
    1. First, in the command-line, go to the bugs_spy folder.
    2. Run scrapy:
           
           ```
              scrapy crawl eclipse 
           ```

  
The crawler will generate an xml file with the name of the project, e.g. `eclipse_reports.xml`. In addition to generating the bug report xml file, you may want to sanitize (add proper xml header/bottom) and separate the file into month chunks. 
To do so we use the project [bugXMLSanitizer](https://github.com/dan7800/EmpericalDuplication/tree/master/bugXMLSanitizer). To do so, just open the `main.py` file and pass the absolute path where you have the .xml(s) you want to 'sanitize'. The code will read the [project]reports.xml, create new new xml files for each month and save each bug report into each particular month depending on its creation date.
Using command-line, run: 
```
python3 main.py
```

### Running the Dedupl tool


## About the development

## Authors

Virginia Pujols** - *Initial work* - MS Software Enginering @RIT

## Acknowledgments
* Special thanks to [Aggarwal et al.](https://bitbucket.org/kaggarwal32/bug-deduping-dataset) team for sharing their study approach and answering our questions.
