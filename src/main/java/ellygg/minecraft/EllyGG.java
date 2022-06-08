package ellygg.minecraft;

import net.fabricmc.api.ModInitializer;

public class EllyGG implements ModInitializer {
    @Override
    public void onInitialize() {

    }
    /*
		Build:
			./gradlew build
		Finish mod:
			/home/elly/Documents/VS code/EllyGGMinecraft/bin/main/
			copy all into zip, rename to jar
	*/

	/*
		TO DO LIST
			- cobbled deepslate
				Do this like carpet mod, water + lava recipe but deep in the world
					-- Maybe have a check for carpet and if it is present use carpet implementation instead of mine
			- renewable sand source
				From villager trade?
				Purifying soul sand?
					-- with lightning like what happens with copper
					-- using dripstone like what happens with clay
					-- using water like concrete
				Recipe that is made from quartz?


		IDEAS LIST
			Un-dye blocks using cauldron to craft instead of standard crafting

			cobweb - 9 string - ???
            string - cobweb = 9 string - ???
                Considering adding a method to convert between string and cobweb
                Maybe don't want to add as cobweb isn't generally needed in large quantities
                    and it can be interesting to have items that you need to go out and find before you can use them
                Another possibility would be to make cobweb a rare drop from cave spiders

            calcite - bone block + block of quartz = 2 calcite
                Not sure if calcite should be a renewable block or a luxury / status block

            tuff - ???
                This block is kinda ugly and has no use yet
                Maybe add crafting method if it becomes useful


		RULED OUT LIST
			Don't add method to make gilded blackstone renewable, keep it as a rare/luxury block
	*/
	/*
		CRAFTING RECIPES:
            - soul soil <====> soul sand
                Easy way to convert between soul sand to soul soil
                    - Vanilla method is crafting soul campfire with soul sand, placing it and mining it to get soul soil
					  I think this is bad because it is tedious and kinda pointless
			
			- Recipes to un-dye blocks
				-- stained glass -> glass
				-- stained glass pane -> glass pane

            - netherrack = gravel + magma cream
                Unsure about this recipe and probably going to keep for now
                Netherrack is weak so didn't want to make out of a durable block like stone
                Wanted a source of heat to create it.
                Gravel and magma cream are both renewable in the nether
				Something like stone generation would be ideal
					Could consider making with flowing lava touching flowing lava.  Would need to not be able to replace lava source blocks

    */
}