import pyglet
from f1tenth_player import F1TenthVideoPlayer
import os
import time
SRC_PATH = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SRC_PATH, '..')
MAP_PATH = os.path.join(PROJECT_PATH, 'resources', 'maps', 'Oschersleben')

if __name__ == "__main__":
    # sample_log = os.path.join(PROJECT_PATH, 'resources', 'examples', 'logs', 'multi.jsonl')
    sample_log = "./logs/Round1/match-343588-round-1.jsonl"

    player = F1TenthVideoPlayer(sample_log, MAP_PATH, 2000, 2000)
    pyglet.clock.schedule_interval(player.update, 0.010)
    time.sleep(0.5)
    pyglet.app.run()
