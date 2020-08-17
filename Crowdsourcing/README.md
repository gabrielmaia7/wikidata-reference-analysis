# Crowdsourcing Scripts

This part of the repository stores and documents the scripts and data used on the Crowdsourcing campaigns for the analysis of reference quality in Wikidata.

## Files and Folders

- **config**: This folder contains the configuration files for running the Crowdsourcing campaign. *Please note* that you should also create here two files which are not included in this repository: *amazon_credentials.json*, with your amazon credentials, and *mongodb_credentials*, with either your mongo credentials or a connection string.
    - **final**: Contains the task configuration for the final tasks (the actual tasks done in the campaign);
        - **task_config_authorit**: Contains the configuration for the authoritativeness tasks (see more about the structure in the README that is in the same folder as these files);
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
