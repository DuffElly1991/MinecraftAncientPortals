package ellygg.minecraft;

import net.fabricmc.api.ModInitializer;

public class EllyGG implements ModInitializer {
    @Override
    public void onInitialize() {

    }
    /*
        Crafting recipes
            - cobbled deepslate = basalt + cobblestone
                Like this recipe, probably going to keep
                Like adding another use for basalt which doesn't do much given it has a unique method of renewal
                Basalt is also a volcanic rock, and deepslate is found deeper in the world so might be formed through heat and pressure on stone
                Like that recipe is implying that deepslate is significantly denser than cobblestone
                Considered using 'deepslate = basalt + stone', but decided on cobble version because otherwise main use would be to immediately place and then mine

            - netherrack = gravel + magma cream
                Like this recipe and probably going to keep
                Netherrack is weak so didn't want to make out of a durable block like stone
                Wanted a source of heat to create it.
                Gravel and magma cream are both renewable in the nether

            - sand = soul sand + prismarine crystal
                Unsure about recipe, might change
                Like idea of converting soul sand into sand, via "purifying"
                Like idea adding another use for guardian farms, but maybe could find a better fit
                Considered splash potion of healing, but that would be weird as you'd be using something crafted from sand to make more sand
                Might replace with lightning strike interaction like copper has
                    Downside would be that lightning isn't consistently accessible

            - soul soil = soul sand
                Unsure about this recipe, might change
                Wanted easy way to convert soul sand to soul soil
                    Vanilla method is crafting soul campfire with soul sand, placing it, mining it - bad, tedious, probably unintended

            - 8 clay = 8 dirt + water bucket
                Temporary recipe, will be removed with wild update's mud
                Could be significantly faster way of acquiring clay than the vanilla version so not ideal
                Might replace with another temporary method, e.g. an attempt to implement dripstone drying mechanic

            - 8 endstone = 8 granite + milk bucket
                Temporary easter egg like recipe, will not stay
                3 stage crafting needed, not ideal
                Considering instead of crafting recipe using game interaction e.g. lava + water.
                Maybe similar method to basalt creation
                Although this would be a bit weird given that water and lava don't exist naturally in the end
     */
    /*
        Possible recipes / methods to obtain blocks

            cobweb - 9 string - ???
            string - cobweb = 9 string - ???
                Considering adding a method to convert between string and cobweb
                Maybe don't want to add as cobweb isn't generally needed in large quantities
                    and it can be interesting to have items that you need to go out and find before you can use them
                Another possibility would be to make cobweb a rare drop from cave spiders

            gilded blackstone - blackstone + gold ingot
                Possibly don't add method to make gilded blackstone, keep it as a rare/luxury block

            calcite - bone block + block of quartz = 2 calcite
                Not sure if calcite should be renewable or luxury block
                Not used as anything other than decoration

            tuff - ???
                This block is kinda ugly and has no use yet
                Will add crafting method if it becomes useful
    */
}
