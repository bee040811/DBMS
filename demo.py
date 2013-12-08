#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    this file is to parse DBpedia data by area to get label and capital
"""
from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF
import sys
import json

def main(argv):
    
#    print sys.argv
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
    SELECT ?label ,?capital
    WHERE { <http://dbpedia.org/resource/%s> rdfs:label ?label;
            dbpedia-owl:capital ?capital
    }
    """ % sys.argv[1])

    sys.argv[2] = sys.argv[2].lower()
    if(sys.argv[2] == "json"):
        # JSON example
        print '\n\n*** JSON Example'
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        print json.dumps(results)
        """
        for result in results["results"]["bindings"]:
            print result["label"]["value"]
            print result["capital"]["value"]
        """
    elif(sys.argv[2] == "xml"):        
        # XML example
        print '\n\n*** XML Example'
        sparql.setReturnFormat(XML)
        results = sparql.query().convert()
        print results.toxml()
    elif(sys.argv[2] == "n3"):        
        # N3 example
        print '\n\n*** N3 Example'
        sparql.setReturnFormat(N3)
        results = sparql.query().convert()
        print results
    elif(sys.argv[2] == "rdf"):        
        # RDF example
        print '\n\n*** RDF Example'
        sparql.setReturnFormat(RDF)
        results = sparql.query().convert()
        print results.serialize()
        
if __name__ == "__main__":
    if(len(sys.argv) < 3) :
        print "please input demo.py 'place' 'convertType'\n"
        print "'place' ex: Chine (first name bigger) \n"
        print "'convertType' ex: json,xml,n3,rdf\n"
    else:    
        main(sys.argv)
