from typing import List, Optional
import gym

env = gym.make("CartPole-v0")

env.reset()
env.render()