from logging.config import fileConfig
import os

colours = ["white",
	"orange",
	"magenta",
	"light_blue",
	"yellow",
	"lime",
	"pink",
	"gray",
	"light_gray",
	"cyan",
	"purple",
	"blue",
	"brown",
	"green",
	"red",
	"black"]

blocks = []
for colour in colours:
	blocks.append(colour + "_stained_glass")
	blocks.append(colour + "_stained_glass_pane")

typeJson = "\"type\": \"minecraft:crafting_shapeless\""

for inputBlock in blocks:
	resultingBlock = ""
	if(inputBlock.endswith("_glass")):
		resultingBlock = "glass"
	elif(inputBlock.endswith("_glass_pane")):
		resultingBlock = "glass_pane"
	fileName = "/home/elly/Documents/VS code/EllyGGMinecraft/bin/main/data/ellygg/recipes/" + resultingBlock + "__from__" + inputBlock + ".json"
	fileContents = "\n".join([
		"{",
		"\t" + typeJson + ",",
		"\t" + "\"ingredients\" : [{",
		"\t\t\"item\": \"minecraft:" + inputBlock + "\"",
		"\t\t}],",
		"\t\"result\": {",
		"\t\t\"item\": \"minecraft:" + resultingBlock + "\",",
		"\t\t\"count\": 1",
		"\t}",
		"}"
		])
	
	if(inputBlock.startswith("black")):
		print(fileContents)
		print(fileName)
	
	file = open(fileName, "w")
	file.write(fileContents)
	file.flush()
	file.close()