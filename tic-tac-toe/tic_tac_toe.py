import gym
from gym import spaces
import numpy as np

class TicTacToe(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(TicTacToe, self).__init__()
        self.env_name='tictactoe'
        self.states = np.zeros((3,3))
        self.counter = 0
        self.done = 0
        self.reward = 0
        self.action_space=spaces.Discrete(9)
        self.observation_space=spaces.Box(low=0,high=2, shape=(3,3))


    def reset(self):
        self.states=np.zeros((3,3))
        self.counter = 0
        self.done = 0
        self.reward = 0
        return np.array(self.states)

    def check(self):
        if self.counter < 5: #game is not over
            return 0
        for i in range(3):
            if ((self.states[i][0] != 0) & (self.states[i][0] == self.states[i][1]) & (
                    self.states[i][1] == self.states[i][2]) & (self.states[i][2] == self.states[i][0])):
                if self.states[i][0] == 1:
                    return 1
                if self.states[i][0] == 2:
                    return 2
            if ((self.states[0][i] != 0) & (self.states[0][i] == self.states[1][i]) & (
                    self.states[1][i] == self.states[2][i]) & (self.states[2][i] == self.states[0][i])):
                if self.states[i][0] == 1:
                    return 1
                if self.states[i][0] == 2:
                    return 2
        if ((self.states[0][0] != 0) & (self.states[0][0] == self.states[1][1]) & (
                self.states[1][1] == self.states[2][2]) & (self.states[2][2] == self.states[0][0])):
            if self.states[i][0] == 1:
                return 1
            if self.states[i][0] == 2:
                return 2

    def step(self, action):
        if self.done == 1:
            print("Game over")
        elif self.states[int(action / 3)][action % 3] != 0:
            print("Invalid step")
        else:
            if (self.counter % 2 == 0):
                self.states[int(action / 3)][action % 3] = 1
            else:
                self.states[int(action / 3)][action % 3] = 2
            self.counter += 1
            if (self.counter == 9):
                self.done = 1
            win = self.check()
            if win == 1:
                self.reward += 100
                self.done = 1
                print(" wins.", sep="", end="\n")
            elif win == 2:
                self.reward -= -100
                self.done = 1
                print(" loses.", sep="", end="\n")
            else:
                self.reward = 0
        info={}
        return self.states,self.reward, bool(self.done), info

    def render(self):
        for i in range(3):
            for j in range(3):
                if self.states[i][j]==0:
                    print("-", end=" ")
                elif self.states[i][j]==1:
                    print("o",end=" ")
                elif self.states[i][j]==2:
                    print("x",end=" ")
            print("")




