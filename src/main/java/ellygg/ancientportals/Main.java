package ellygg.ancientportals;

import net.fabricmc.api.ModInitializer;
import net.kyrptonaught.customportalapi.api.CustomPortalBuilder;
import net.minecraft.block.Blocks;
import net.minecraft.item.Items;
import net.minecraft.util.Identifier;

public class Main implements ModInitializer {
    @Override
    public void onInitialize()
	{
		
		//Create the dimension
		Identifier dimensionIdentifier = createDimension();

		//Create the portal to link up to the created dimension
		createPortal(dimensionIdentifier);
    }

	public Identifier createDimension()
	{
		//to do replace this with link to the actual dimension
		Identifier dimensionIdentifier = new Identifier("ancientportals", "longlostlands_dimension");
		

		return dimensionIdentifier;
	}

	public void createPortal(Identifier destination)
	{
		CustomPortalBuilder.beginPortal()  
        .frameBlock(Blocks.REINFORCED_DEEPSLATE)  
        .lightWithItem(Items.LINGERING_POTION)  
        .destDimID(destination)
        .tintColor(16,64,16)  
        .registerPortal();
	}
}