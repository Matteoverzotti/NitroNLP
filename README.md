# NitroNLP

 This is the code used for the [NitroNLP Hackaton](https://www.nitronlp.rocks/) by team **#3FF500**.

It is mostly based on the [SpaCy model for Romanian](https://spacy.io/models/ro).

# File descriptions

```
NitroNLP
│   README.md
│   main.ipynb           # main program
│   requirements.txt     # requirements 
│   documentation.txt    # documentation    
│   submission.csv       # our final submission    
└─── Data
│   │   tag_to_id.json   # json file that converts from labels to id"s
│   │   test.csv         # csv file with test data 
│   │   test.json        # json file with test data
│   │   train.csv        # csv file with train data
│   │   train.json       # json file with train data
│   
└───Workshops            # Submodule with all workshops data
    └
```

# Data Format

The dataset is a list of instances. The following in an instance of the training dataset:

```json
{
    "ner_tags": ["O", "GPE", "O", "O", "O", "O", "O", "O", "LOC", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "PERSON", "O", "O", "O", "O", "PERSON", "O", "O", "O", "O", "O", "O", "O", "O", "O", "PERSON", "O", "O", "O", "O", "O", "O", "O", "PERSON", "O", "PERSON", "O", "PERSON", "O", "O", "PERSON", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],

    "ner_ids": [0, 3, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    
    "tokens": ["În", "România", ",", "ca", "de", "altfel", "în", "întreaga", "Europă", ",", "stand", "up", "-ul", "este", "forma", "de", "divertisment", "cea", "mai", "îndrăgită", "de", "tineri", "în", "acest", "moment", ",", "comediantii", "reușind", "să", "umple", "săli", "care", "erau", "destinate", "mai", "degrabă", "artiștilor", "din", "zona", "muzicii", "pop", "rock", ",", "iar", "Badea", ",", "Bordea", "și", "Micutzu", "sunt", "printre", "cei", "care", "au", "contribuit", "direct", "la", "succesul", "acestei", "forme", "de", "divertisment", "în", "țara", "noastră", "."],

    "space_after": [True, False, True, True, True, True, True, True, False, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False]
}
```

# Data Fields

The fields of each training example are: 
* `tokens` are the words of the sentence;
* `ner_tags` are the string tags assigned to each token;
* `ner_ids` are the integer encoding of each tag;
* `space_after` is used to help if there is a need to detokenize the dataset. A true value means that there is a space after the token on that respective position.

# Labels
The corpus was annotated with the following classes:

* `PERSON` - proper nouns, including common nouns or pronouns if they refer to a person. (e.g. 'sister')

* `GPE` - geo political entity, like a city or a country; has to have a governance form

* `LOC` - location, like a sea, continent, region, road, address, etc.

* `ORG` - organization

* `LANGUAGE` - language (e.g. Romanian, French, etc.)

* `NAT_REL_POL` - national, religious or political organizations

* `DATETIME` - a time and date in any format, including references to time (e.g. 'yesterday')

* `PERIOD` - a period that is precisely bounded by two date times

* `QUANTITY` - a quantity that is not numerical; it has a unit of measure

* `MONEY` - a monetary value, numeric or otherwise

* `NUMERIC` - a simple numeric value, represented as digits or words

* `ORDINAL` - an ordinal value like 'first', 'third', etc.

* `FACILITY` - a named place that is easily recognizable

* `WORK_OF_ART` - a work of art like a named TV show, painting, etc.

* `EVENT` - a named recognizable or periodic major eventdaca nu iti da codul

* `O` - other, none of the above classes

In order to test locally, make sure you meet the `requirements.txt` and just run `main.ipynb`.