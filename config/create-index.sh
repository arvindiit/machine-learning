#!/bin/sh

ES_HOST=http://172.17.0.2:9200

curl -s -XPOST $ES_HOST/newsarticle-classification -d @schema-newsarticle-classification.json
