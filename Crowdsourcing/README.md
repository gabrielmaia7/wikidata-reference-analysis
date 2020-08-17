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
        -
