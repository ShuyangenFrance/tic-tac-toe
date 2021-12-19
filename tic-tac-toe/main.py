
tictactoe=TicTacToe()
tictactoe.reset()
#check_env(tictactoc,warn=False)
model = QLeaning()
q_table=model.learn(tictactoe)
state= tictactoe.reset()
for i in range(20):
    action= model.predict(tictactoe,state,q_table)
    obs, reward, done, info = tictactoe.step(action)
    print('reward=', reward, 'done=', done)
    tictactoe.render()