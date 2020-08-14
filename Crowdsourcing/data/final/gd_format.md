# Annotating Golden data

## Format

For each object in the sampled_references_$lan_gd.json files, change the g_id field from 0 to the following:

```
"g_id": {
    "relevance": {
        "is_present": A list of numbers, from 0 to 1, 0 if it is not present, 1 if it is.
        "difficulty": A list of numbers from 0 to 4, with 0 to 4 simbolizing possible difficulty answers as seen below. Can also be just -1 if it does not matter.
        "reason": A list of numbers from 0 to 6, with 0 to 6 simbolizing possible reason answers as seen below. Can also be just -1 if it does not matter.
    },
    "authorit":{
        "author": A list of numbers from 0 to 2 simbolizing the author type as seen below.
        "publisher": A list of numbers from 0 to 4 simbolizing the publisher type as seen below.
        "sub_publisher": A list of numbers from 0 to the amount of subpublisher types for this publisher type, simbolizing the subpublisher type as seen below. It can also be -1 if it doesn't matter or if the publisher has no subtypes.
    }
}
```

## Values

### "relevance/difficulty"

0. I had to navigate the website and use the additional information or infer the statement using my common sense;
1. I had to navigate the website and use the additional information to find it;
2. I had to navigate the website to find it;
3. I did not need to navigate the website but had to read through the content to find it;
4. I did not need to navigate the website or read through much content to find it. 

### "relevance/reason"

0. The page was not available (for example, 404 error);
1. My browser or antivirus stopped me, claiming the page presented security risks;
2. I was required to provide a login and password to access the page, but don’t have them;
3. I was required to pay for access to the page, and I am not inclined to do so;
4. I feel like only people familiar with a specific domain would understand the information inthe page;
5. None of the above, but the subject and/or the predicate were not mentioned in the page;
6. None of the above, the subject and predicate were mentioned in the page, but the object was different.

### "authorit/author"

0. Individual;
1. Organization;
2. Collective;

### "authorit/publisher" and "authorit/sub_publisher"

0. Academic and scientific organizations;
    0. Academic and research institutions;
    1. Academic publishers;
    2. Other academic organizations.
1. Companies and non-academic/scientific organizations;
    0. Vendors and e-commerce companies;
    1. Political or religious organisations;
    2. Cultural institutions;
    3. Other types of company.
2. Government agencies and authorities;
3. News and media outlets;
    0. Traditional news and media(e.g. news agencies, broad-casters);
    1. Non-traditional news and media(e.g. online magazines, platforms tocollaboratively create news).
4. Self-published sources.