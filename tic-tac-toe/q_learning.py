import numpy as np
import random
class QLeaning:

    def __init__(self,alpha = 0.1,gamma = 0.6,epsilon = 0.1,epochs=5000):
        self.alpha=alpha
        self.gamma=gamma
        self.epsilon=epsilon
        self.epochs=epochs

    def state_to_number(self, state):
        state = state.reshape(9)
        number = 0
        for i, num in enumerate(state):
            number += num * 3 ** (len(state) - i - 1)
        return int(number)

    def number_to_state(self,number):
        state = np.zeros(9)
        nums = []
        while number:
            number, r = divmod(number, 3)
            nums.append(r)
        state[len(state) - len(nums):] = np.array(nums)[::-1]
        return state.reshape((3, 3))

    def q_table(self,env):
        q_table=np.zeros((3**9, env.action_space.n))
        return q_table

    def learn(self,env):
        if env.env_name=="tictactoe":
            self.q_table = self.q_table(env)
            for i in range(self.epochs):
                state = env.reset()

                epochs, penalties, reward, = 0, 0, 0
                done = False

                while done !=True:
                    if random.uniform(0, 1) < self.epsilon:
                        action = env.action_space.sample()  # Explore action space
                        #forbiden ilegal action
                        while state[int(action / 3)][action % 3] !=0:
                            action=env.action_space.sample()
                    else:
                        action_value_list=self.q_table[self.state_to_number(state)]
                        for action,action_value in enumerate(action_value_list):
                            if state[int(action / 3)][action % 3]!=0:
                                action_value_list[action]=np.nan
                        action = np.nanargmax(action_value_list)  # Exploit learned values
                    next_state, reward, done, info = env.step(action)
                    old_value = self.q_table[self.state_to_number(state), action]
                    next_max = np.nanmax(self.q_table[self.state_to_number(next_state)])
                    new_value = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * next_max)
                    self.q_table[self.state_to_number(state), action] = new_value
                    state = next_state

                    epochs += 1
        return self.q_table


    def predict(self,env,state,q_table, deterministic=True):
        if self.state_to_number(state)==0:
            action=env.action_space.sample()
        else:
            action_value_list = self.q_table[self.state_to_number(state)]
            for action, action_value in enumerate(action_value_list):
                if state[int(action / 3)][action % 3] != 0:
                    action_value_list[action] =np.nan
            action = np.nanargmax(action_value_list)
            if (~deterministic) & (random.uniform(0, 1) < env.epsilon):
                action = env.action_space.sample()
                while state[int(action / 3)][action % 3] != 0:
                    action = env.action_space.sample()
        return action