import deepchem as dc
dc.__version__
from deepchem.utils.save import load_from_disk
import deepchem.utils.data_utils

dataset_file= "structure links.csv"
dataset = load_from_disk(dataset_file)
print("Columns: %s" % str(dataset.columns.values))
print("Rows: %s" % str(dataset.shape[0]))

import rdkit
from rdkit import Chem
from rdkit.Chem import Draw
from itertools import islice

import pandas as pd
my_csv = pd.read_csv('structure links.csv')
smiles1 = my_csv.SMILES


featurizer = dc.feat.ConvMolFeaturizer(per_atom_fragmentation=True)
out = featurizer.featurize(smiles1)
out.__sizeof__()

# Parameters
#     ----------
#     master_atom: Boolean
#       if true create a fake atom with bonds to every other atom.
#       the initialization is the mean of the other atom features in
#       the molecule.  This technique is briefly discussed in
#       Neural Message Passing for Quantum Chemistry
#       https://arxiv.org/pdf/1704.01212.pdf
#     use_chirality: Boolean
#       if true then make the resulting atom features aware of the
#       chirality of the molecules in question
#     atom_properties: list of string or None
#       properties in the RDKit Mol object to use as additional
#       atom-level features in the larger molecular feature.  If None,
#       then no atom-level properties are used.  Properties should be in the
#       RDKit mol object should be in the form
#       atom XXXXXXXX NAME
#       where XXXXXXXX is a zero-padded 8 digit number coresponding to the
#       zero-indexed atom index of each atom and NAME is the name of the property
#       provided in atom_properties.  So "atom 00000000 sasa" would be the
#       name of the molecule level property in mol where the solvent
#       accessible surface area of atom 0 would be stored.
#     per_atom_fragmentation: Boolean
#       If True, then multiple "atom-depleted" versions of each molecule will be created (using featurize() method). 
#       For each molecule, atoms are removed one at a time and the resulting molecule is featurized. 
#       The result is a list of ConvMol objects,
#       one with each heavy atom removed. This is useful for subsequent model interpretation: finding atoms
#       favorable/unfavorable for (modelled) activity. This option is typically used in combination
#       with a FlatteningTransformer to split the lists into separate samples.
#     Since ConvMol is an object and not a numpy array, need to set dtype to
#     object.

# type(out[0])
# out[0].num_node_features
# out[0].num_edge_features



##################### TEST ###################

# molecules = [Chem.MolFromSmiles(smiles)
#              for smiles in islice(dataset['SMILES'],len(dataset))]
# # Draw.MolsToGridImage(molecules[0:8])

# temp1 = [Chem.rdmolfiles.MolToSmiles([Chem.MolFromSmiles(smiles)
#                                       for smiles in islice(dataset['SMILES'],len(dataset))])]
# temp2 = [Chem.MolToSmiles(mols)
#              for mols in islice(molecules,len(molecules))]

# featurizer = dc.feat.MolGraphConvFeaturizer(use_edges=True)
# out = featurizer.featurize(smiles)



