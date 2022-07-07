from logging.config import fileConfig
import os

#Different item types
items = [
	"chest"
]

#Different boat types
boats = [
	"oak",
	"spruce",
	"birch",
	"jungle",
	"acacia",
	"dark_oak",
	"mangrove"
]

for resultingItem in items:
#{
	listOfRecipes = []
	for boat in boats:
#	{
		remainderItem = boat + "_boat"
		inputItem = boat + "_chest_boat"
		
		fileName = "/home/elly/Documents/VS code/EllyGGMinecraft/src/main/resources/data/ellygg/recipes/" + resultingItem + "__from__" + inputItem + ".json"

		fileContents = "\n".join([
			"{",
			"\t\"type\": \"minecraft:crafting_shapeless\",",
			"\t\"group\": \"ellygg_" + resultingItem + "\",",
			"\t" + "\"ingredients\" : [{",
			"\t\t\"item\": \"minecraft:" + inputItem + "\",",
 			"\t\t\"remainder\": { \"item\": \"minecraft:" + remainderItem + "\" }",
			"\t\t}],",
			"\t\"result\": {",
			"\t\t\"item\": \"minecraft:" + resultingItem + "\",",
			"\t\t\"count\": 1",
			"\t}",
			"}"
			])

		# if(boat == "oak"):
		# 	print(fileName)
		# 	print(fileContents)

		file = open(fileName, "w")
		file.write(fileContents)
		file.flush()
		file.close()
#	}

		listOfRecipes.append("\t\t\t\"ellygg:" + resultingItem + "__from__" + inputItem + "\"")


	#Add a list of all recipes for the rewards
	finishedRecipes = ",\n".join(listOfRecipes)

	fileName = "/home/elly/Documents/VS code/EllyGGMinecraft/src/main/resources/data/ellygg/advancements/recipes/" + resultingItem + "__from__" + resultingItem + "_boat" + ".json"

	fileContents = "\n".join([
		"{",
		"\t\"parent\": \"minecraft:recipes/root\",",
		"\t\"criteria\": {",
		"\t\t\"has_" + resultingItem + "\": {",
		"\t\t\t\"trigger\": \"minecraft:inventory_changed\",",
		"\t\t\t\"conditions\": {",
		"\t\t\t\t\"items\": [",
		"\t\t\t\t\t{ \"items\": [\"minecraft:" + resultingItem + "\"] }",
		"\t\t\t\t]",
		"\t\t\t}",
		"\t\t}",
		"\t},",
		"\t\"requirements\": [",
		"\t\t[\"has_" + resultingItem + "\"]",
		"\t],",
		"\t\"rewards\": {",
		"\t\t\"recipes\": [",
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
#}