# Wikidata Reference Analysis (WdRA)

This repository includes all scripts and data used on my analysis of the quality of references containted in Wikidata statements, as explored in this paper: [insert paper link here]().

## Files and Folders

Here is the description of files and folders as they were created and used for the objective of this analysis.

- **Crowdsourcing**: This folder includes all scripts and data related to the Crowdsourcing campaigns and experiments used in this analysis. More information on it is included inside.
- **data**: This folder holds cached data of the analysis. When running the analysis scripts, resulting tables and results are stored there.
- **wikipedia_paper_images**: This folder contains the images used in the paper.
- **Non-Referenced-Statements-Analysis.ipynb**: This notebook contains an analysis made on the wikidata statements which do not include references.
- **Wikidata-Analysis(-v2).ipynb**:  This notebook contains an analysis made on the wikidata statements which **do** have references. It looks at their subject, property and object types, as well as references urls themselves. It also extracts the Crowdsourcing samples, which we'll then give to the Crowd on MTurk.
- **Wikidata-Parser(-v2).ipynb**: This notebook extracts a random X% (currently set to 20%) of all statements in Wikidata and organises it in SQL tables. This parsing is done faster than using the recommended modules by Wikidata themselves. For this, we open the dump files as bynary data and keep track of reading positions, jumping accross the dumps as quickly as possible (C speed).
- **Wikidata-ref-coverage-stats.ipynb**: This notebook uses the data imported from [Wikidata's statistics](https://wikidata-todo.toolforge.org/stats.php), to show the evolution of the number of references accross the years.
- **Wikidata_Sample_Dataset_For_ML.ipynb**: This notebook (unfinished) is here to create the ML datasets from the crowd annotated data.
- **Wikidata_pilot_analysis.ipynb**: This notebook explores the results from the Crowdsourcing pilots, run before the actual campaigns.
- **iskill.txt**: This text file is for interrupting SQL queries which are taking too long. Altering its contents to 'Yes' stops SQL queries.
- **languages_and_countries.py**: This contains a list of tuples that associates language codes with their full names.
- **samplesize.py**: This contains code to calculate the needed sample size according to original population size, confidence interval and significance values.
- **svlanganswers.ipynb**: This notebook compares and combines the answers to the Swedish language test, as well as Dutch and Japanese, which we have collected from anonymous users from Reddit.

## How to use these files

If you intend on recreating our research, than follow the steps:

1. Download the most current dump from Wikidata. You can find it [here](https://dumps.wikimedia.org/wikidatawiki/entities/). Download *latest-all.json.bz2* and verify what format it follows, which should be documented in [this page](https://www.mediawiki.org/wiki/Wikibase/DataModel/JSON).
2. Run *Wikidata-Parser-v2.ipynb* on the .bz2 file, adapting it to any changes in the JSON format since this experiment was carried. This should extract statements from it and insert them in a tabular format into an SQL database. This should generate three tables:
    - **claims**: Contains individual statement nodes (claims), with subject, predicate and object;
    - **claim_refs**: Contains the connections between statement nodes and reference nodes, when a reference node supports a given statement node;
    - **refs**: Contains individual reference nodes, with their identifier, predicate and supporting information.
3. Run *Wikidata-Analysis-v2.ipynb*, using the parsed SQL databases. This will reveal trends and characteristics in the data for comparison with our results. This might also need adapting.
4. Run the last cells of *Wikidata-Analysis-v2.ipynb* to generate a Crowdsourcing sample of the data. Adapt the code to any changes in format. The code does not create the tables for you, so you'll need to create and use the code to populate them, but their schema should be obvious based on the insert statements included here.
5. Go into the *Crowdsourcing* folder to see the next steps. Going in there, you should have two SQL tables with sampled results:
    - **reference_nodes_to_urls**: A table with URLs extracted from the references, as well as the reference nodes themselves;
    - **reference_urls_parsed**: A table with the URLs parsed and their status code, language and type of content extracted.
