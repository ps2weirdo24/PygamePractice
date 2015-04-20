import pygame

pygame.image.get_extended()


class game_map:

	def __init__(self):
		self.layers = 0 #number of total layers in this map
		self.resolution = [] #list for the (width, height) of each tile's pixels
		self.mapsize = [] #list for the (width,heigth) of the map's tiles
		self.filename = "" #string for the file's location
		self.tilesetname = "" #string for the tileset paired with this map
		self.tiledata = []
		

	def load_map(self, input_filename, tileset_filename, output_filename):
		self.outputname = str(output_filename)
		self.filename = input_filename
		map_file = open(input_filename)
		raw_map = map_file.readlines()
		map_file.close()

		self.layers = int(raw_map[0])
		self.resolution = (raw_map[1]).split(",")
		self.mapsize = (raw_map[2]).split(",")
		self.tilesetname = str(tileset_filename)
		self.tiledata = []
		raw_map_trim = raw_map[6:int(len(raw_map)-1)]
		raw_map_3d = []
		for line in raw_map_trim:
			single_tile_data = line.split(",")
			single_tile_data[5] = single_tile_data[5][0]
			raw_map_3d.append(single_tile_data)
		#print raw_map_3d


		tile_source = pygame.image.load(self.tilesetname)

		master_w = int(self.resolution[0]) * int(self.mapsize[0])
		master_h = int(self.resolution[1]) * int(self.mapsize[1])


		self.master_surface = pygame.Surface((master_w,master_h))

		for line in raw_map_3d:
			# line[0] = layer line [1,2] = top,left in tilefile
			# line[3,4] = collum, row in map
			# line[5] = z, extra flag
			wx = int(line[3]) * int(self.resolution[1])
			wy = int(line[4]) * int(self.resolution[1])
			wq = int(line[1])
			ww = int(line[2])
			we = int(self.resolution[1])
			wr = int(self.resolution[1])
			self.master_surface.blit(tile_source, (wx,wy), (wq, ww, we, wr))


		pygame.image.save(self.master_surface, self.outputname)
		print "Map Saved!"










map_file_name1 = "resources/map/map_3/txtmap_3.txt"


myscene1 = game_map()
myscene1.load_map(map_file_name1, "mappic_3.bmp")