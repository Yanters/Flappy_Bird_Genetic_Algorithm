import components.pipe as pipe

class Pipes:
    def __init__(self):
        self.pipes = []

    def add_pipe(self,win_width,pipe_width,pipe_min_y,pipe_max_y,pipe_speed,pipe_gap_min,pipe_gap_max):
        self.pipes.append(pipe.Pipe(win_width + pipe_width, pipe_min_y, pipe_max_y,
                                     pipe_speed, pipe_gap_min, pipe_gap_max))
        
    def draw(self, window):
        for pipe in self.pipes:
           pipe.draw(window)
           pipe.update()

    def remove_pipes_passed(self):
        for pipe in self.pipes:
            if pipe.x < 0 - pipe.top_pipe_img.get_width()/2:
                self.pipes.remove(pipe)

    def get_pipes(self):
        return self.pipes
    def get_pipe(self,index):
        return self.pipes[index]
    
    def clear_pipes(self):
        self.pipes.clear()

        