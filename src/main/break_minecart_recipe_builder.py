from logging.config import fileConfig
import os

#Different item types
items = [
	"chest",
	"hopper",
	"tnt",
	"furnace"
]

for resultingItem in items:
	remainderItem = "minecart"
	inputItem = resultingItem + "_minecart"

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

	# if(resultingItem == "chest"):
	# 	print(fileName)
	# 	print(fileContents)

	file = open(fileName, "w")
	file.write(fileContents)
	file.flush()
	file.close()

	

	fileName = "/home/elly/Documents/VS code/EllyGGMinecraft/src/main/resources/data/ellygg/advancements/recipes/" + resultingItem + "__from__" + inputItem + ".json"

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
		"\t\t\t\"ellygg:" + resultingItem + "__from__" + inputItem + "\"",
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