import ontology as Ontology
import re


class OntologyTemplateMethod:
    ontologyObject = ''

    # parameterized constructor
    def __init__(self, ontology_path, ontology_namespace):
        self.ontologyObject = Ontology.Ontology(ontology_path, ontology_namespace)

    def printAll(self):
        all = self.ontologyObject.getAllClasses()
        count = 0
        for i in all:
            print(i)
            numbers = re.findall(r'\d+', i)
            if (numbers):
                FMAID = numbers[0]
                print(FMAID)
                print(self.getOne(FMAID))
            else:
                count+=1
        print(count)

    def getOne(self, FMAID):
        data = {}
        data["label"] = self.ontologyObject.label(FMAID)
        data["ancestors"] = self.ontologyObject.directAncestors(FMAID)
        data["properties"] = self.ontologyObject.properties(FMAID)
        data["subclasses"] = self.ontologyObject.subclasses(FMAID)
        return data
