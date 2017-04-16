from flask import Flask
import discord
import asyncio
from discord.ext import commands
import os
import victini
#now for the flask
app = Flask(__name__)
#flask events
@app.route("/")
def vict():
	description="Victini . Your Own Personal Pokemon Game"
	bot=commands.Bot(command_prefix='v!', description=description)
	@bot.event
	async def on_ready():
		print("ready")
	@bot.command(pass_context=True,description="Register For Pokemon Adventure Bot Victini")
	async def catch(ctx,slot):
		try:
			poke=victini.pokemon.on_encounter()
			victini.pokemon.on_pokemon_register(ctx.message.author.name,poke,slot)
			await bot.say(":arrow_forward: "+ctx.message.author.name+" Caught a **"+poke+"** in Pokeball "+slot)
			return
		except:
			await bot.say("arrow_forward: Error ! Please use correct syntex ex . !pokemon catch 2  \n here two is the number of pokeball u want to replace")
			return
	@bot.command(pass_context=True,description="View your pokemon list")
	async def list(ctx,word):
		try:
			a=victini.pokemon.on_show_pokemon_list(word)
			await bot.say(":arrow_forward: "+word+" have pokemon : **"+a[1]+"** , **"+a[2]+"** , **"+a[3]+"**")
			return
		except:
			a=victini.pokemon.on_show_pokemon_list(ctx.message.author.name)
			await bot.say(":arrow_forward: "+ctx.message.author.name+" have pokemon : **"+a[1]+"** , **"+a[2]+"** , **"+a[3]+"**")
			return
	@bot.command(pass_context=True,description="Register for Victini")
	async def reg(ctx):
		a=victini.pokemon.on_register_user(ctx.message.author.name)
		if a == True:
			await bot.say(":x: You have already registered .")
			return False
		else:
			await bot.say(":white_check_mark: "+ctx.message.author.name+" Succesfully Registered !")
	@bot.command(pass_context=True,description="Set your nickname !")
	async def nick(ctx,word):
		a=victini.pokemon.on_nickname_register(ctx.message.author.name,word)
		if a == True:
			return await bot.say(":white_check_mark: "+ctx.message.author.mention+" Nickname changed to "+word,delete_after=5)
		else:
			return await bot.say(":x: Please register first")
	@bot.command(pass_context=True,description="See your states")
	async def stats(ctx,word):
		try:
			a=victini.pokemon.on_stats(word)
			await bot.say(":arrow_forward: "+" Trainer : **"+word+"** \n```ID = "+str(a[0])+"\n Nickname = "+str(a[2])+"\n Total battle = "+str(a[4])+"\n Total win = "+str(a[3])+"\n ```",delete_after=10)
			return
		except:
			a=victini.pokemon.on_stats(ctx.message.author.name)
			await bot.say(":arrow_forward: "+" Trainer : **"+a[1]+"** \n```ID = "+str(a[0])+"\n Nickname = "+a[2]+"\n Total battle = "+str(a[4])+"\n Total win = "+str(a[3])+"\n ```",delete_after=10)
			return
	@bot.command(pass_context=True,description="Battle against one another pokemon")
	async def battle(ctx,username):
		challeng=username.replace("<","").replace("@","").title()
		challenger=''.join([i for i in challeng if not i.isdigit()])
		trainer=ctx.message.author.name.title()
		if trainer==challenger:
			await bot.say(":interrobang:  You cant battle with yourself",delete_after=5)
			return
		else:
			pass
		try:
			plist=victini.pokemon.on_show_pokemon_list(trainer)
			clist=victini.pokemon.on_show_pokemon_list(challenger)
		except:
			await bot.say(":interrobang: Name Not Found",delete_after=5)
		if clist==False:
			await bot.say(":interrobang: Name Not Found",delete_after=5)
			return
		else:
			pass
		win=[]
		lose=[]
		tp=0
		cp=0
		try:
			if victini.pokemon.on_battle(plist[1],clist[1]):
				tp=tp+1
				win=win+[plist[1]]
				lose=lose+[clist[1]]
			else:
				cp=cp+1
				win=win+[clist[1]]
				lose=lose+[plist[1]]
			if victini.pokemon.on_battle(plist[2],clist[2]):
				tp=tp+1
				win=win+[plist[2]]
				lose=lose+[clist[2]]
			else:
				cp=cp+1
				win=win+[clist[2]]
				lose=lose+[plist[2]]
			if victini.pokemon.on_battle(plist[3],clist[3]):
				tp=tp+1
				win=win+[plist[3]]
				lose=lose+[clist[3]]
			else:
				cp=cp+1
				win=win+[clist[3]]
				lose=lose+[plist[3]]
			if tp>cp:
				wintext=trainer
				losetext=challenger
				victini.pokemon.on_win(trainer)
			else:
				wintext=challenger
				losetext=trainer
				victini.pokemon.on_win(challenger)
			texttosend="**"+wintext+"** defeated "+losetext
			battledetails="```"+win[0]+" defeated "+lose[0]+"\n"+win[1]+" defeated "+lose[1]+"\n"+win[2]+" defeated "+lose[2]+"\n"+"```"
			await bot.say(":heart: "+texttosend+"\n"+battledetails)
		except:
			await bot.say(":interrobang: You and Your opponent Must have 3 pokemons for this \n Also you have to enter correct Name",delete_after=5)
			
			
				
	@bot.command(description="Help for Victini")
	async def howto():
		text="**Rules**\n start by v!reg and \n then catch three pokemon using v!catch 1 , 2 , 3 respectively \n set a nickname using v!nickname nickname ... then u  can start exploring \n```\n v!reg : To register for Victini \n v! catch 1,2,3 : Catch a pokemon in pokeball 1 or 2 or 3 \n v!stats me or username: View your trainer states \n v!list me or username : View your pokemon list \n v!nickname yourname : To update your nickname \n```"
		await bot.whisper(text)
		return
	bot.run("TOKEN")
	return "Hello world / just for fun"

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

