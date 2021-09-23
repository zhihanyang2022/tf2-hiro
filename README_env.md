# Create custom environment

## Structure

On a high leve, the main environment resides within my_env.py. It's 
base env is a antmaze env used to compute the movement of the agent. T
The wrapper serves the function of providing goal and computing the 
reward.

To understand, see this

```python
base_env = create_maze_env(env_name='AntSimple',)
env = EnvWithGoal(base_env, env_name='AntSimple')
```

First, we need to create a base_env

create_maze_env instantiates AntMazeEnv, passing in the env_name to
be used by `construct_maze` in `maze_env_utils.py` (so we need to modify that so that 
the maze structure corresponding to the env_name is available)

EnvWithGoal need goal sample fn and reward function, both of
which can be changed in `my_env.py`