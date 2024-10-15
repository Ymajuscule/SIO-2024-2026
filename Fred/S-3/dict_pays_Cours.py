dict_pays = {
    'fr': 'France',
    'pl': 'Pologne',
    'it': 'Italie'
}

print("On a créé le dict", dict_pays)
print("Avec ['it'],    \t on retourne", dict_pays['it'])
print("Avec .get('fr'),\t on retourne", dict_pays.get("fr"))
print("Avec .keys(),   \t on retourne", dict_pays.keys())
print("Avec .values(), \t on retourne", dict_pays.values())
dict_pays['al'] = "Allemagne"
print("Avec .keys(),   \t on retourne", dict_pays.keys())
print("Avec .values(), \t on retourne", dict_pays.values())