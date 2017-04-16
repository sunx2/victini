
import sqlite3
import random
#modules imported
conn=sqlite3.connect("Pokemon")
c=conn.cursor()
class pokemon():
	def on_register_user(username):
		try:
			user=c.execute("SELECT * FROM Pokemon WHERE Name = '"+username+"'")
			user.fetchone()[1]==username
			return True
		except:
			user = c.execute("INSERT INTO Pokemon (Name) VALUES ('"+username+"')")
			conn.commit()
			return False
	def on_pokemon_register(username,pokemonname,slot): 
		try:
			user=c.execute("UPDATE Pokemon SET Pokemon"+slot+"='"+pokemonname+"' WHERE Name='"+username+"'")
			conn.commit()
			return True
		except:
			print("some error occured")
	def on_nickname_register(username,nickname):
		try:
			user=c.execute("UPDATE Pokemon SET Nickname='"+nickname+"' WHERE Name='"+username+"'")
			conn.commit()
			return True
		except:
			return False
	def on_show_pokemon_list(username):
		try:
			c.execute("SELECT * FROM Pokemon WHERE Name='"+username+"'")
			pokelist=c.fetchone()
			pokeit=[pokelist[1],pokelist[3],pokelist[4],pokelist[5]]
			return pokeit
		except:
			print("error occured")
			return False
	def on_win(username):
		try:
			c.execute("UPDATE Pokemon set Win = Win + 1 WHERE Name='"+username+"'")
			conn.commit()
			return True
		except:
			print("error in win block")
			return False
	def on_encounter():
		c.execute("SELECT Pokemon FROM Details")
		a=c.fetchall()
		pokemonlist=[]
		for item in a:
			pokemonlist=pokemonlist+[item[0]]
		return random.choice(pokemonlist)
	def on_stats(username):
		try:
			c.execute("SELECT * FROM Pokemon WHERE Name='"+username+"'")
			pokelist=c.fetchone()
			pokeit=[pokelist[0],pokelist[1],pokelist[2],pokelist[6],pokelist[7]]
			return pokeit
		except:
			print("not found error")
			return False
	def on_pokemon_type_compare(pokeone,poketwo):
		c.execute("SELECT * FROM Details WHERE Pokemon='"+pokeone+"'")
		one=c.fetchone()[5]
		c.execute("SELECT * FROM Details WHERE Pokemon='"+poketwo+"'")
		two=c.fetchone()[5]
		
		if one=="Fire" and two in ("Fire","Grass","Normal","Bug","Ice"):
			return True
		elif one=="Water" and two in ("Water","Fire","Rock","Ground"):
			return True
		elif one=="Grass" and two in ("Water","Ground","Rock","Normal"):
			return True
		elif one=="Ground" and two in ("Ground","Rock","Bird"):
			return True
		elif one=="Bird" and two in ("Grass","Bug"):
			return True
		elif one=="Rock" and two in ("Grass","Bug"):
			return True
		elif one=="Ice" and two in ("Grass","Bug","Dragon"):
			return True
		elif one=="Dragon" and two in ("Grass","Water","Dragon"):
			return True
		elif one=="Fighting" and two in ("Fighting","Ground","Rock","Dark"):
			return True
		elif one=="Ghost" and two in ("Ghost","Psycic"):
			return True
		elif one=="Psycic" and two in ("Fighting"):
			return True
		elif one=="Dark" and two in ("Ghost","Psycic"):
			return True
		else:
			return False
		
	def on_pokemon_attck_compare(pokeone,poketwo):
		c.execute("SELECT * FROM Details WHERE Pokemon='"+pokeone+"'")
		one=c.fetchone()[3]
		c.execute("SELECT * FROM Details WHERE Pokemon='"+poketwo+"'")
		two=c.fetchone()[3]
		if one>two:
			return True
		else:
			return False
	def on_pokemon_defense_compare(pokeone,poketwo):
		c.execute("SELECT * FROM Details WHERE Pokemon='"+pokeone+"'")
		one=c.fetchone()[4]
		c.execute("SELECT * FROM Details WHERE Pokemon='"+poketwo+"'")
		two=c.fetchone()[4]
		if one>two:
			return True
		else:
			return False
	def on_battle(pokeone,poketwo):
		cmpone=pokemon.on_pokemon_attck_compare(pokeone,poketwo)
		cmptwo=pokemon.on_pokemon_defense_compare(pokeone,poketwo)
		cmpthree=pokemon.on_pokemon_type_compare(pokeone,poketwo)
		if cmpone and cmptwo and cmpthree:
			return True
		elif cmpone and cmptwo or cmpthree:
			return True
		elif cmpone or cmptwo and cmpthree:
			return True
		else:
			return False

if __name__=="__main__":
	print(pokemon.on_encounter())
	a=input("pokeonne: ")
	b=input("poketwo:  ")
	print(pokemon.on_battle(a,b))

