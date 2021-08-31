import deepchem as dc

featurizer =  dc.feat.MolGraphConvFeaturizer(use_edges=True)
loader = dc.data.SDFLoader(["MOLECULAR_WEIGHT","EXACT_MASS"], featurizer=featurizer, sanitize=True)
dataset = loader.featurize("structures.sdf")

print(dataset)
out-torch = dataset.make_pytorch_dataset()
out_df=dataset.to_dataframe()

print(dataset.ids[0:2])

out_smiles= dataset.ids

out = featurizer.featurize(out_smiles)
