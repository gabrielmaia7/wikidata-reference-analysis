# Taks Configuration files

These files denote the configurations for running tasks.

## Structure break-down

- "type": The type of task: "authorit" or "relevance";
- "time_thr": The time workers need to spend in each single task of the taskset to not be flagged as spam, e.g. "2500";
- "tasks" : Path to the tasksets file, e.g. "TaskSets/TaskSets_{}_auth.json";
- "html_layout": Path to the HTML template file, e.g. "WikidataReferenceAuthTemplate.html";
- "instructions_project_text_file": Path to the text file for the project description section of the task instructions, e.g. "instructions_project_text.txt";
- "instructions_intro_text_file": Path to the text file for the introduction section of the task instructions, e.g. "instructions_intro_text_auth.txt";
- "instructions_rules_text_file": Path to the text file for the rules section of the task instructions, e.g. "instructions_rules_text_auth.txt";
- "task_attributes": Attributes of the task, as specified by the [MTurk API](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_CreateHITOperation.html):
    - "MaxAssignments": Maximum number of workers who can do this HIT e.g. 5;
    - "LifetimeInSeconds": Number of seconds this HIT will remain available for workers e.g. 604800;
    - "AssignmentDurationInSeconds": Number of seconds a worker can work on this HIT after accepting it e.g. 1800;
    - "Reward": Amount of dollars the worker gets as reward, e.g. "0.5";
    - "Title": A title for your HIT, which will be displayed in the MTurk marketplace e.g. "Checking author and publisher type of websites \[Japanese\]",
    - "Keywords": A set of keywords to be shown alongside your title e.g. "Weblinks, Author type, Publisher type, Information Retrieval, Japanese";
    - "Description": A task description to be shown in the marketplace as well e.g. "Help us by clicking on weblinks and telling us which kind of Author and Publisher they are. You should have reading proficiency in Japanese.",
    - "QualificationRequirements": Requirements for workers to be able to take this HIT. For instructions on how to set up these, look at the [documentation](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html).