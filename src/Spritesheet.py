# import simplegui
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Spritesheet:
    def __init__(self, filename, frame_size, frame_count, columns=0):
        """
        Parameters:
        - filename: Path to sprite sheet image
        - frame_size: (width, height) of individual frames
        - frame_count: Total frames in sheet
        - columns: Number of columns (0 for horizontal strip)
        """
        self.image = simplegui.load_image(filename)
        self.frame_size = frame_size
        self.frame_count = frame_count
        self.columns = columns
        self.frames = []
        
        # Pre-calculate frame coordinates
        self._generate_frames()

    def _generate_frames(self):
        frame_w, frame_h = self.frame_size
        current_x = 0
        current_y = 0
        
        for _ in range(self.frame_count):
            self.frames.append((
                (current_x + frame_w/2, current_y + frame_h/2),  # Source center
                (frame_w, frame_h)                                # Source size
            ))
            
            if self.columns > 0 and (len(self.frames) % self.columns == 0):
                # Grid layout: move to next row
                current_x = 0
                current_y += frame_h
            else:
                # Horizontal strip
                current_x += frame_w

    def get_frame(self, index):
        """Returns (source_center, source_size) for simplegui's draw_image"""
        if 0 <= index < self.frame_count:
            return self.frames[index]
        return None