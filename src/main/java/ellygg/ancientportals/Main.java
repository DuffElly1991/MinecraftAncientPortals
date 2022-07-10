package ellygg.ancientportals;

import net.fabricmc.api.ModInitializer;
import net.kyrptonaught.customportalapi.api.CustomPortalBuilder;
import net.minecraft.block.Blocks;
import net.minecraft.item.Items;
import net.minecraft.util.Identifier;

public class Main implements ModInitializer {
    @Override
    public void onInitialize() {
		CustomPortalBuilder.beginPortal()  
        .frameBlock(Blocks.REINFORCED_DEEPSLATE)  
        .lightWithItem(Items.LINGERING_POTION)  
        .destDimID(new Identifier("the_end"))
        .tintColor(16,64,16)  
        .registerPortal();
    }
}