from logging.config import fileConfig
import os

#All of the different block colours
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

#Make a list of all of the different blocks we want to un-dye
blocks = []
for colour in colours:
	blocks.append(colour + "_stained_glass")
	blocks.append(colour + "_stained_glass_pane")
	blocks.append(colour + "_terracotta")

#Build the recipe files
for inputBlock in blocks:
	resultingBlock = ""
	if(inputBlock.endswith("_glass")):
		resultingBlock = "glass"
	elif(inputBlock.endswith("_glass_pane")):
		resultingBlock = "glass_pane"
	elif(inputBlock.endswith("_terracotta")):
		resultingBlock = "terracotta"

	fileName = "/home/elly/Documents/VS code/EllyGGMinecraft/src/main/resources/data/ellygg/recipes/" + resultingBlock + "__from__" + inputBlock + ".json"
	fileContents = "\n".join([
		"{",
		"\t\"type\": \"minecraft:crafting_shapeless\",",
		"\t\"group\": \"ellygg_" + resultingBlock + "\",",
		"\t" + "\"ingredients\" : [{",
		"\t\t\"item\": \"minecraft:" + inputBlock + "\"",
		"\t\t}],",
		"\t\"result\": {",
		"\t\t\"item\": \"minecraft:" + resultingBlock + "\",",
		"\t\t\"count\": 1",
		"\t}",
		"}"
		])
	
	# if(inputBlock.startswith("black")):
	# 	print(fileContents)
	# 	print(fileName)
	
	file = open(fileName, "w")
	file.write(fileContents)
	file.flush()
	file.close()

resultingBlocks = ["glass", "glass_pane", "terracotta"]

#Build the advancements to unlock recipes
for resultingBlock in resultingBlocks:
	fileName = "/home/elly/Documents/VS code/EllyGGMinecraft/src/main/resources/data/ellygg/advancements/recipes/" + resultingBlock + ".json"
	fileContents = "\n".join([
		"{",
		"\t\"parent\": \"minecraft:recipes/root\",",
		"\t\"criteria\": {",
		"\t\t\"has_" + resultingBlock + "\": {",
		"\t\t\t\"trigger\": \"minecraft:inventory_changed\",",
		"\t\t\t\"conditions\": {",
		"\t\t\t\t\"items\": [",
		"\t\t\t\t\t{ \"items\": [\"minecraft:" + resultingBlock + "\"] }",
		"\t\t\t\t]",
		"\t\t\t}",
		"\t\t}",
		"\t},",
		"\t\"requirements\": [",
		"\t\t[\"has_" + resultingBlock + "\"]",
		"\t],",
		"\t\"rewards\": {",
		"\t\t\"recipes\": ["
	])

	#Add a list of all recipes for the rewards
	listOfRecipes = []
	for inputBlock in blocks:
		if(inputBlock.endswith(resultingBlock)):
			listOfRecipes.append("\t\t\t\"ellygg:" + resultingBlock + "__from__" + inputBlock + "\"")
	
	finishedRecipes = ",\n".join(listOfRecipes)

	fileContents = "\n".join([
		fileContents,
		finishedRecipes,
		"\t\t]",
		"\t}",
		"}"
	])

	# print(fileContents)
	# print(fileName)

	file = open(fileName, "w")
	file.write(fileContents)
	file.flush()
	file.close()