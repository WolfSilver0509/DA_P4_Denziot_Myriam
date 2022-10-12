
def joueur():
  db = TinyDB('db.json')
  
  joueurs = db.table('joueurs')

  insert = joueurs.insert()

  return
  joueurs 

  # print(joueurs.all())

  #joueurs.insert({'nom': "nom_de_famille"})


