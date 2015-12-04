from __future__ import print_function

import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Descriptors

def example_mol():
	mol = Chem.MolFromSmiles('CCC(=O)C(O)=O')
	return mol

def hydrogen_from_carbon(mol, atom):
	"""Return a proton bonded to atom"""
	foundH = None
	hCount = 0
	for bond in atom.GetBonds():
		assert isinstance(bond, rdkit.Chem.rdchem.Bond)
		atom1 = bond.GetBeginAtom()
		if atom1.GetAtomicNum() == 1:
			foundH = atom1
			hCount += 1
		atom2 = bond.GetEndAtom()
		if atom2.GetAtomicNum() == 1:
			foundH = atom2
			hCount += 1
	assert foundH is not None
	assert 1 <= hCount <= 3

	return foundH

def get_sphere(atom, start, end=None):
	"""
	Return all atoms in the start:end sphere starting from (centered at) atom

	Examples:
	(atom, 1): 1st sphere ie. immediate neighbours only
	(atom, 5) or (atom, 5, 5): 5th sphere only
	(atom, 5, 6): 5th + 6th spheres
	"""
	if end is None:
		end = start
	end += 1

	excluded = [atom]
	def already_excluded(a):
		for other in excluded:
			if a.GetIdx() == other.GetIdx():
				return True
		return False
	last_sphere = [atom]
	for i in range(start - 1):
		neighbours = [a.GetNeighbors() for a in last_sphere]
		neighbours = [a for b in neighbours for a in b]
		last_sphere = [n for n in neighbours if not already_excluded(n)]
		excluded += last_sphere

	included = []
	def already_included(a):
		for other in included:
			if a.GetIdx() == other.GetIdx():
				return True
		return False
	for i in range(start, end):
		neighbours = [a.GetNeighbors() for a in last_sphere]
		neighbours = [a for b in neighbours for a in b]
		last_sphere = [n for n in neighbours if (not already_excluded(n)) and (not already_included(n))]
		included += last_sphere

	return included

def gasteiger_charges(atoms):
	return [float(atom.GetProp('_GasteigerCharge')) for atom in atoms]

def min_max_avg_charge(atoms):
	charges = gasteiger_charges(atoms)
	return [min(charges), max(charges), sum(charges)/len(charges)]

def get_gasteiger_features(atom):
	features = []
	features += [atom.GetProp('_GasteigerCharge')]

	for sphere_num in [1,2,3,4]:
		sphere = get_sphere(atom, sphere_num)
		features += min_max_avg_charge(sphere)

	return features

def num_C(atoms):
	return len([atom for atom in atoms if atom.GetAtomicNum() == 6])
def num_N(atoms):
	return len([atom for atom in atoms if atom.GetAtomicNum() == 7])
def num_O(atoms):
	return len([atom for atom in atoms if atom.GetAtomicNum() == 8])
def num_F(atoms):
	return len([atom for atom in atoms if atom.GetAtomicNum() == 9])
def num_S(atoms):
	return len([atom for atom in atoms if atom.GetAtomicNum() == 16])
def num_Cl(atoms):
	return len([atom for atom in atoms if atom.GetAtomicNum() == 17])
def num_Br(atoms):
	return len([atom for atom in atoms if atom.GetAtomicNum() == 35])
def num_I(atoms):
	return len([atom for atom in atoms if atom.GetAtomicNum() == 53])
def num_aromatic(atoms):
	return len([atom for atom in atoms if atom.GetIsAromatic()])
def num_in_ring(atoms):
	return len([atom for atom in atoms if atom.IsInRing()])

def get_topological_features(atom):
	features = []

	for sphere_num in [1,2,3,4]:
		sphere = get_sphere(atom, sphere_num)
		for scalar_func in [num_C, num_N, num_O, num_F, num_S, num_Cl, num_Br, num_I, num_aromatic, num_in_ring]:
			features.append(scalar_func(sphere))

	return features

def features_for_atom(mol, atom_index):
	mol = Chem.AddHs(mol)
	assert isinstance(mol, rdkit.Chem.rdchem.Mol)
	atom = mol.GetAtomWithIdx(atom_index)
	assert isinstance(atom, rdkit.Chem.rdchem.Atom)
	AllChem.ComputeGasteigerCharges(mol)

	atom = hydrogen_from_carbon(mol, atom)

	gasteiger_features = get_gasteiger_features(atom)
	topological_features = get_topological_features(atom)

	print(len(gasteiger_features + topological_features),'features so far')

if __name__ == '__main__':
	mol = example_mol()
	features_for_atom(mol,1)
