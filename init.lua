print("This file will be run at load time!")

local colors = {
	"black", "blue", "blue2", "green", "grey", "lightblue", "lightgreen",
	"orange", "pink", "pink2", "purple", "red", "white", "yellow"
}

for _, color in ipairs(colors) do
	local name = "brick_" .. color
	local nodename = "coloredbricks:" .. name
	local texture = name .. ".png"
	local dye = "dye:" .. color

	core.register_node(nodename, {
		description = color:gsub("^%l", string.upper) .. " bricks",
		tiles = {texture},
		groups = {cracky = 1},
		sounds = default.node_sound_stone_defaults()
	})

	core.register_craft({
		type = "shapeless",
		output = nodename,
		recipe = { "default:brick", dye },
	})
end
