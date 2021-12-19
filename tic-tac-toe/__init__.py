from .tic_tac_toe import TicTacToe
from .q_learning import QLeaning

def main():
    tictactoe = TicTacToe()
    tictactoe.reset()
    # check_env(tictactoc,warn=False)
    model = QLeaning()
    q_table = model.learn(tictactoe)
    state = tictactoe.reset()
    for i in range(100):
        action = model.predict(tictactoe, state, q_table)
        obs, reward, done, info = tictactoe.step(action)
        print('reward=', reward, 'done=', done)
        tictactoe.render()

if  __name__ == "__main__":
    main()
