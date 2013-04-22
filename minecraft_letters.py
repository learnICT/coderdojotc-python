# Written by Jessica Zehavi for CoderDojo Twin Cities - www.coderdojotc.org
def write ( minecraft, text, material ):
	letters  =  { 'A' : [[1,0,0,1],[1,0,0,1],[1,1,1,1],[1,0,0,1],[0,1,1,0]],
			      'B' : [[1,1,1,0],[1,0,0,1],[1,1,1,0],[1,0,0,1],[1,1,1,0]],
			      'C' : [[0,1,1,0],[1,0,0,1],[1,0,0,0],[1,0,0,1],[0,1,1,0]],
			      'D' : [[1,1,1,0],[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,1,1,0]],
			      'E' : [[1,1,1,1],[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,1,1,1]],
			      'F' : [[1,1,1,1],[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]],
			      'G' : [[1,1,1,0],[1,0,0,1],[1,0,0,0],[1,0,1,1],[0,1,1,0]],
			      'H' : [[1,0,0,1],[1,0,0,1],[1,1,1,1],[1,0,0,1],[1,0,0,1]],
			      'I' : [[1,1,1],[0,1,0],[0,1,0],[0,1,0],[1,1,1]],
			      'J' : [[0,1,1,0],[1,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]],
			      'K' : [[1,0,0,1],[1,0,1,0],[1,1,0,0],[1,0,1,0],[1,0,0,1]],
			      'L' : [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]],
			      'M' : [[1,0,0,0,1],[1,0,0,0,1],[1,0,1,0,1],[1,1,0,1,1],[1,0,0,0,1]],
			      'N' : [[1,0,0,0,1],[1,0,0,1,1],[1,0,1,0,1],[1,1,0,0,1],[1,0,0,0,1]],
			      'O' : [[0,1,1,0],[1,0,0,1],[1,0,0,1],[1,0,0,1],[0,1,1,0]],
			      'P' : [[1,0,0,0],[1,0,0,0],[1,1,1,1],[1,0,0,1],[1,1,1,1]],
			      'Q' : [[0,0,1,1],[0,1,1,0],[1,0,0,1],[1,0,0,1],[0,1,1,0]],
			      'R' : [[1,0,0,1],[1,0,1,0],[1,1,1,1],[1,0,0,1],[1,1,1,1]],
			      'S' : [[1,1,1,0],[0,0,0,1],[0,1,1,0],[1,0,0,0],[0,1,1,1]],
			      'T' : [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[1,1,1]], 
			      'U' : [[0,1,1,0],[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,0,0,1]],
			      'V' : [[0,0,1,0,0],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1],[1,0,0,0,1]],
			      'W' : [[0,1,0,1,0],[1,0,1,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,0,0,0,1]],
			      'X' : [[1,0,0,0,1],[0,1,0,1,0],[0,0,1,0,0],[0,1,0,1,0],[1,0,0,0,1]],
			      'Y' : [[0,0,1,0,0],[0,0,1,0,0],[0,1,0,1,0],[1,0,0,0,1],[1,0,0,0,1]],
			      'Z' : [[1,1,1,1,1],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[1,1,1,1,1]],
			      ' ' : [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]}

	# Get the player's current position
	pos       =  minecraft.player.getPos()
	row       =  0
	kearning  =  0

	for letter in text.upper():

		print letter

		while row < len( letters[letter] ):

			col  =  0

			while col < len( letters[letter][0] ):

				# If a block should be printed in that row/column for a 
				# given letter, print it
				if letters[letter][row][col]:
					minecraft.setBlock( pos.x - col - kearning, pos.y + row + 1, pos.z, material )

				col  =  col + 1
			row  =  row + 1

		# Reset the row and col for each letter
		row     =  0

		# Adjust the spacing based on how big the letter is since this is 
		# not a fixed width font
		kearning  =  kearning + len( letters[letter][0] ) + 1
