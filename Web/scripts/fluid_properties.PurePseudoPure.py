from CPWeb.BibtexTools import getCitationOrAlternative, getBibtexParser
import CoolProp
import os.path
import CoolProp

web_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
root_dir = os.path.abspath(os.path.join(web_dir, '..')) 
csvfile = os.path.join(web_dir,'fluid_properties','PurePseudoPure.csv')

class Dossier:
    def __init__(self):
        self.data = {}
    def add(self, key, value):
        if key not in self.data:
            self.data[key] = []
        self.data[key].append(value)

d = Dossier()

from pybtex.database.input import bibtex
parser = bibtex.Parser()
bibdata = parser.parse_file(os.path.join(root_dir,"CoolPropBibTeXLibrary.bib"))

bibtexer = getBibtexParser()

bibtex_map = {'EOS': 'EOS',
              'CP0': ':math:`c_{p0}`',
              'CONDUCTIVITY': ':math:`\lambda`',
              'VISCOSITY': ':math:`\eta`',
              'MELTING_LINE': 'melt'}
bibtex_keys = ['EOS','CP0','CONDUCTIVITY','VISCOSITY','MELTING_LINE']
for fluid in CoolProp.__fluids__:
    d.add('name', fluid)
    for key in bibtex_keys:
        try:
            # get the item
            s = CoolProp.CoolProp.get_BibTeXKey(fluid,key)
            if s.strip() and s.strip() not in bibdata.entries.keys():
                print 'problem', fluid, key, '\t\t\t\t', "|"+s+'|'
                d.add(key, '')
            else:
                d.add(key, s)
        except ValueError as E:
            d.add(key, '')
            
import pandas
df = pandas.DataFrame(d.data)
df = df.sort(['name'], ascending = [1])

def build_citation(key):
    if not key:
        return ''
    else:
        return ':cite:`'+key+'`'

def fluid_reference(fluid):
    return fluid

# Write the table
with open(csvfile,'w') as fp:
    rowdata = ["Name"] + [bibtex_map[key] for key in bibtex_keys]
    fp.write(','.join(rowdata)+'\n')
    for index, row in df.iterrows():
        rowdata = [fluid_reference(row['name'])] + [build_citation(row[key]) for key in bibtex_keys]
        fp.write(','.join(rowdata)+'\n')
        

