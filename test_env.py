from environments.my_env import EnvWithGoal
from environments.create_maze_env import create_maze_env

base_env = create_maze_env(env_name='AntSimple', top_down_view=True, show=True)
env = EnvWithGoal(base_env, env_name='AntSimple', render=True, evalmode=True)

state = env.reset()
while True:
    env.set_goal(state[:2])
    next_state, reward, done, info = env.step(env.action_space.sample())
    if done:
        break
    state = next_state
