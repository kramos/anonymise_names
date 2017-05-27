# Overview
Uses the [Natural Language Toolkit](http://www.nltk.org/_modules/nltk/tag/stanford.html) to take text and remove names and her/his.

Could be used to anonymise conference presentations.


# Usage
```
$ docker run --rm anonymise_names  "How Alice and her team made production better"

How PERSON and their team made production better
```
