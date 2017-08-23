# Author: Robert Bennett
# Description: Draw a series of lines in a drawing app by dragging the mouse around.

import sys, pyautogui, time, drawings

class Main():
	def __init__(self):
		if len(sys.argv) == 2:                                # Check that the user passed exactly 1 command line argument.
			time.sleep(5)                                     # Allow the user 5 seconds to position their mouse.
			self.draw(sys.argv[1])                            # Execute the drawing method with the command line argument.
		else:
			print("Usage: py auto_draw.py <DRAWING-NAME>\n")  # Fail with a useful message.

	def draw(self, drawingName):
		speed = 0.1                                           # Set the duration of each stroke.

		drawing = getattr(drawings, drawingName)              # Retrieve the drawing the user selected.

		x1 = drawing[0][0]
		y1 = drawing[0][1]
		pyautogui.moveRel(x1, y1, speed)                      # Move the mouse to the first point.

		for i in range(1, len(drawing)):                      # Drag the mouse from point to point.
			x2 = drawing[i][0]
			y2 = drawing[i][1]
			pyautogui.dragRel(x2, y2, speed)


if __name__ == "__main__":
	app = Main()
