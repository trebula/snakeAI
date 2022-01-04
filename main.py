import game
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', type=int, default=15, help='size of the board')
    parser.add_argument('--x', type=int, default=int(parser.parse_args().size/2), help='x coordinate of the head', choices=range(parser.parse_args().size))
    parser.add_argument('--y', type=int, default=int(parser.parse_args().size/2), help='y coordinate of the head', choices=range(parser.parse_args().size))
    parser.add_argument('--fps', type=int, default=15, help='frames per second')
    parser.add_argument('--squareSize', type=int, default=50, help='square size')
    parser.add_argument('--length', type=int, default=3, help='length of the snake')
    return parser.parse_args()

params = parse_args()

def main():
    # create game object
    currGame = game.Game(params.size, params.size, params.fps, params.squareSize, (params.x, params.y), params.length)

    # run game
    currGame.run()

if __name__ == '__main__':
    main()