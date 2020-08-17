# Crowdsourcing Scripts

This part of the repository stores and documents the scripts and data used on the Crowdsourcing campaigns for the analysis of reference quality in Wikidata.

## Files and Folders

- **config**: This folder contains the configuration files for running the Crowdsourcing campaign. *Please note* that you should also create here two files which are not included in this repository: *amazon_credentials.json*, with your amazon credentials, and *mongodb_credentials*, with either your mongo credentials or a connection string.
    - **final**: Contains the task configuration for the final tasks (the actual tasks done in the campaign);
        - **task_config_authorit**: Contains the configuration for the authoritativeness tasks (see more about the structure in the [README that is in the same folder as these files](config/final/README.md));
        - **task_config_relevance**: Contains the configuration for the relevancy tasks;
    - **pilot_config**: Contains the task configuration for the tasks carried in the pilot;
    - **pipeline_test_config**: Contains the task configuration for the tasks carried while testing the pipeline (from Wikidata parsing to task generation and deployment)
    - **banlist.json**: List of WorkerIDs which are suspected to be spammers;
    - **instructions_intro_text_auth.txt**: Contains the text to be shown in the instructions introduction of the authoritativeness task;
    - **instructions_intro_text_rel.txt**: Same as above, but for the relevancy task;
    - **instructions_project_text.txt**: Contains the text to be shown in the instructions, on the project section, of both task types;
    - **instructions_rules_text_auth.txt**: Contains the text to be shown in the instructions, on the rules section, of the authoritativeness task;
    - **instructions_rules_text_rel.txt**: Contains the text to be shown in the instructions, on the rules section, of the relevancy task;
    - **task_content_template.json**: Contains a template for the task configuration files found in **final**, **pilot_config**, and **pipeline_test_config**.
- **data**: Contains the data generated through the Crowdsourcing campaigns, both as part of the task designs and as results
    - **language_data**: Data for the language tests to be randomly shown in the tasks
        - **language_tests.json**: Contains the language tests for all six target languages, with questions, options and answer;
        - **nl_test**: Contains the messages sent to the users of Reddit to ask for the answers to the Dutch test.
    - **pilot_data**: Data used for the pilots of the crowdsourcing campaign
        - **TaskSetsForPilot_auth.json**: Contains the sets of authoritativeness tasks to be sent to the workers. Each MTurk HIT contains one of these tasksets.
        - **TaskSetsForPilot_rel.json**: Contains the sets of relevancy tasks fo be sent to the workers. Each MTurk HIT contains one of these tasksets.
        - **crowdsourcing_sample_pilot_auth.json**: Sample of non-gold-standard individual tasks (not bundled in tasksets yet) to send in the authoritativeness tasks.
        - **crowdsourcing_sample_pilot_auth_gd.json**: Sample of gold-standard individual tasks (not bundled in tasksets yet) to send in the authoritativeness tasks.
        - **crowdsourcing_sample_pilot_rel.json**: Sample of non-gold-standard individual tasks (not bundled in tasksets yet) to send in the relevancy tasks.
        - **crowdsourcing_sample_pilot_rel_gd.json**: Sample of gold-standard individual tasks (not bundled in tasksets yet) to send in the relevancy tasks.
    - **pipeline_test**: Data used for the pipeline test of the crowdsourcing pipeline (Wikidata parsing to tasksets creation and deployment to workers). All data here is for relevancy tasks, as the pipeline is essentially the same for both task types and we thus only tested for relevancy.
        - **TaskSets_\<language\>.json**: Contains the tasksets to be sent to the workers.
        - **sampled_references_\<language\>.json**: Contains the sample of non-gold-standard individual tasks to send to the workers.
        - **sampled_references_\<language\>_gd.json**: Contains the sample of   gold-standard individual tasks to send to the workers.
    - **final**: Data used for the actual crowdsourcing campaign.
        - **TaskSets**: Contains the taskset files to be sent to the workers, for both task types and for all six target languages.
        - **all_aggregated_annotations**: Final and aggregated results from the crowdsourcing campaign, for each target language. Combines the results from the automatic API verifications and the crowdsourcing.
        - **gd_annotations**: The gold-standard sampled references (45 for each target language) with their annotations. These annotations are loose, in the sense that they allow for multiple fitting answers, to account for the degrees of subjectivity that this task entails.
        - **non_gd_annotations_auto_api**: The annotations for the non-gold-standard sampled references which could be automatically checked with an associated API.
        - **non_gd_filtered_sampled_references**: The sampled (but not yet annotated) non-gold-standard references, after we have removed those which can be automatically checked by API calls (hence the 'filtered' name). These are the references which, coupled with those in the **gd_annotations** folder, will be bundled into tasksets and sent to the crowd workers. There is one file for each language-tasktype combination.
        - **gd_format.md**: A markdown file describing the notation and structure used to annotate the gold-standard references.
        - **sampled_references_\<language\>.json**: The file with the sampled non-gold-standard references in that language, taken directly from the **reference_nodes_to_urls** and **reference_urls_parsed** tables created during the Wikidata Analysis phase.
        - **sampled_references_\<language\>_gd.json**: The file with the sampled gold-standard references in that language. This was taken after sampling the non-gold-standard references and then splitting the file into non-gold-standard and gold-standard portions. These files were then put into the **gd_annotations** folder and manually annotated.
- **imgs**: Images used in the Crowdsourcing tasks, for examples. We uploaded these into imgur and linked imgur hyperlinks in the tasks' html codes.
- **Add_fields_to_final_annotation_sets.ipynb**: This notebook adds some additional fields to the final annotation sets found in **data/final/all_aggregated_annotations**. The reason for this is that, when generating the task sets, putting them into the HTMLs and collecting the results, some information, such as how the URL was obtained (direct url link, external identifier, wikipedia import, etc) was lost. We use this to recover it.
- **Automated_verification_APIs-\<language\>.ipynb**: These notebooks take the non-gold-standard sampled references found in **data/final** (those named sampled_references_\<language\>.json) and filter out those references which can be automatically checked via APIs. It then checks them. The checked references are then put into **non_gd_annotations_auto_api** and the ones which can not be automatically checked are put into **non_gd_filtered_sampled_references**.
- **Crowd_Results_Analysis.ipynb**: This notebook takes the results of the crowdsourced annotations and analyses it. It calculates agreement scores, analyses distributions and draws insights from the results.
- **ExperimentRunner.ipynb**: This notebook is the one which unites the tasksets, the language tests, the task configuration files and the HTML templates and launches the tasks on MTurk, as well as registering them into the MongoDB database. It can also abort tasks and delete them.
- **GenerateTaskSets.ipynb**: This notebook takes the sampled references from the **reference_nodes_to_urls** and **reference_urls_parsed** tables and, joinning these two tables, produces the gold-standard and non-gold-standard partitioned samples for the **sampled_references_\<language\>.json** and **sampled_references_\<language\>_gd.json** files. After *annotating the gold standards** and *filtering out the API-checked references*, this notebook also generates the tasksets to be sent to the crowd.
- **WikidataReferenceAuthTemplate.html**: This file is the template for the authoritativeness task. It is filled during the execution of **ExperimentRunner.ipynb** to contain the tasksets and language tests corresponding of each HIT, based on the contents of the task configuration file used by the ExperimentRunner.
- **WikidataReferenceAuthMockup.html**: This is an example of **WikidataReferenceAuthTemplate.html** filled with some values taken from the sample. This is made available to test the assembled tasks.
- **WikidataReferenceReleTemplate.html**: This file is the template for the relevancy task. It is filled during the execution of **ExperimentRunner.ipynb** to contain the tasksets and language tests corresponding of each HIT, based on the contents of the task configuration file used by the ExperimentRunner.
- **WikidataReferenceReleMockup.html**: This is an example of **WikidataReferenceReleTemplate.html** filled with some values taken from the sample. This is made available to test the assembled tasks.
- **Wikidata_Samples_Final_Annotations_Analysis.ipynb**: This notebook contains the *final analysis* of the results gathered from both the crowd and automatic API checks.
- **fleis.py**: Script which computes Fleiss' Kappa, an inter-rater aggreement measure.
- **krippendorff_alpha.py**: Script which computes Krippendorff's Alpha, another inter-rater agreement measure.
- **mockup.pdf**: This file holds the mockup used to design the tasks. Made with Balsamiq.
- **mturk.py**: This script is a module which contains all the necessary interfacing with MTurk, done via its API and the botocore3 module.
- **update_db.py**: This script is a python routine which keeps track of HITs as they are resolved by workers and updates the MongoDB database used to track their status. See inside the script instructions on using it.

## Using these files

1. After having created and populated both **reference_nodes_to_urls** and **reference_urls_parsed** tables with samples, follow the instructions and run the notebook **GenerateTaskSets**, which will create the tasksets for running the HITs. This will require:
    1. Assembling the tables into the reference samples ready to be sent to workers;
    2. Splitting the samples into gold standard and non gold standard;
    3. Filtering the non gold standards based on whether or not we can check them with APIs, using the **Automated_verification_APIs-\<language\>.ipynb** notebooks;
    4. Label the filtered non gold standard as being the samples for the *relevancy* task, and creating a copy of it for the *authoritativeness* tasks, with the difference being that for the *authoritativeness* tasks we'll remove all references using Wikipedia (because they bloat the sample and we already know their authoritativeness classification)
    5. Annotate the gold standards;
    6. Generate the tasksets;
2. Make sure the HTMLs are working properly by checking for errors using the Mockups. Any needed changes must be done in the templates.
3. Write the task configurations for the tasks about to be run, as well as modifying any needed text file used.
4. Use the **ExperimentRunner** notebook to then launch the tasks.
5. Use the **update_db.py** script to keep track of the status of the HITs.
6. Use the **Crowd_Results_Analysis.ipynb** notebook to analyse the results from the crowd.
7. Use the **Wikidata_Samples_Final_Annotations_Analysis.ipynb** notebook to analyse final results from both crowd and APIs.