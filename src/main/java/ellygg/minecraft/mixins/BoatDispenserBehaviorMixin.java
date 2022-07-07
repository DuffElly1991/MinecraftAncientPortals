package ellygg.minecraft.mixins;

import net.minecraft.block.DispenserBlock;
import net.minecraft.block.dispenser.ItemDispenserBehavior;
import net.minecraft.block.dispenser.BoatDispenserBehavior;
import net.minecraft.entity.vehicle.BoatEntity;
import net.minecraft.entity.vehicle.ChestBoatEntity;
import net.minecraft.item.ItemStack;
import net.minecraft.server.world.ServerWorld;
import net.minecraft.tag.FluidTags;
import net.minecraft.util.math.BlockPointer;
import net.minecraft.util.math.BlockPos;
import net.minecraft.util.math.Direction;

import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;

@Mixin(BoatDispenserBehavior.class)
class BoatDispenserBehaviorMixin extends ItemDispenserBehavior
{
	@Shadow ItemDispenserBehavior itemDispenser;
	@Shadow BoatEntity.Type boatType;
    @Shadow boolean chest;

	@Override
    public ItemStack dispenseSilently(BlockPointer pointer, ItemStack stack)
	{
        Direction direction = pointer.getBlockState().get(DispenserBlock.FACING);
        ServerWorld world = pointer.getWorld();

        double x = pointer.getX() + (double)((float)direction.getOffsetX() * 1.5f);
        double y = pointer.getY() + (double)((float)direction.getOffsetY() * 1f -0.5f);
        double z = pointer.getZ() + (double)((float)direction.getOffsetZ() * 1.5f);

		BlockPos blockPos = pointer.getPos().offset(direction);

        double inWaterOffset;
        if (world.getFluidState(blockPos).isIn(FluidTags.WATER))
		{
            inWaterOffset = 0.525f;
        }
		else if (world.getBlockState(blockPos).isAir() && world.getFluidState(blockPos.down()).isIn(FluidTags.WATER))
		{
            inWaterOffset = -0.475f;
        }
		else if (world.getBlockState(blockPos).isAir())
		{
            inWaterOffset = 0f;
        }
		else
		{
            return this.itemDispenser.dispense(pointer, stack);
        }
        BoatEntity boatEntity = this.chest ? new ChestBoatEntity(world, x, y + inWaterOffset, z) : new BoatEntity(world, x, y + inWaterOffset, z);
        boatEntity.setBoatType(this.boatType);
        boatEntity.setYaw(direction.asRotation());
        world.spawnEntity(boatEntity);
        stack.decrement(1);
        return stack;
    }
}