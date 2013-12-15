#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
    class dbpediaArea and method 
    method :
        getDataByArea(area,type)
"""
from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF
import sys
import json

class DbpediaArea:

    def getDataByArea(self,area,type):
        """
            coordinate 
            abstract
            label
            capital
        """
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setQuery("""
        SELECT ?label ,?capital ,?abstract, ?coordinate
        WHERE { 
                <http://dbpedia.org/resource/%s> 
                rdfs:label ?label;
                dbpedia-owl:abstract ?abstract;
                grs:point ?coordinate;
                dbpedia-owl:capital ?capital
        }
        """ % area)

        type = type.lower()
        if(type == "json"):
            # JSON example
            print '\n\n*** JSON Example'
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()
            results = json.loads(json.dumps(results,ensure_ascii=False ,encoding='utf-8'))
            data = {}
            for result in results['results']['bindings']:
                for index in result:
                    if (index not in data):
                        if(index == 'abstract'):
                            if (result[index]['xml:lang']=="zh") :
                                data[index] = {}
                                data[index]['value'] = result[index]['value']
                        elif (index == 'label' or index == "coordinate" or index == "capital"):
                            data[index] = {}
                            data[index]['value'] = result[index]['value']
            return json.dumps(data,ensure_ascii=False , encoding='utf-8')
            """
            for result in results["results"]["bindings"]:
                print result["label"]["value"]
                print result["capital"]["value"]
            """
        elif(type == "xml"):        
            # XML example
            print '\n\n*** XML Example'
            sparql.setReturnFormat(XML)
            results = sparql.query().convert()
            return results.toxml()
        elif(type == "n3"):        
            # N3 example
            print '\n\n*** N3 Example'
            sparql.setReturnFormat(N3)
            results = sparql.query().convert()
            return results
        elif(type == "rdf"):        
            # RDF example
            print '\n\n*** RDF Example'
            sparql.setReturnFormat(RDF)
            results = sparql.query().convert()
            return results.serialize()
