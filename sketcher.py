import error_loc

err_line = error_loc.locate()


#identify the first function/primitive in that line

def block_name_checker(err_line):
#for primitives
	line_code = ((numbered_bt[line].lstrip('\t')).rstrip(':')) #cleaning the line

	#split into names of blocks 

	primitives=line_code[1]

	#for functions
	line_code = ((numbered_bt[line].lstrip('\tfunction')).rstrip(':')).split(" ") #cleaning the line
	func = line_code[1]

	#find list of instructions from blocks currently displayed and their connecting block names
	instr_list = LearnBlock.scene.getListInstructions()

	#detect block with erroneous primitive/ function


	b_list = self.scene.dicBlockItem


	for i in b_list.values():
		if (i.name == name):
			list_right = #list of blocks to the right of i by iterating through instr_list
			for other_blocks in line_code:
				#check if other_blocks in list_right
			if #all other_blocks in list_right:
				#repeat for [prev_line]
				#repeat for [next_line]
			#if all conditions true:
				i.file=#<error_block_image_of_same_shape>
				#reload_scene()


