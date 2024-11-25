import pickle 
with open('sfl/data/test_sets/image.pkl', 'rb') as f:
# with open('sfl/data/test_sets/sampled_tc_100e_1a.pkl', 'rb') as f:
    env_instance=pickle.load(f)
    
# print(env_instance)
# print(env_instance.keys())  # Check what keys/attributes are stored in the pickled file
# print("Data keys:", data[0].keys())  # Check what keys/attributes are stored in the pickled file
# env_instance = data["env_instance"]

# print(env_instance['agent_pos'].shape)
# print(env_instance['agent_theta'])
# print(env_instance['map_data'].shape)
# print(env_instance['goal_pos'].shape)
# print(env_instance['rew_lamda'].shape)

print(env_instance.agent_pos.shape)
print(env_instance.agent_theta.shape)
print(env_instance.map_data.shape)
print(env_instance.goal_pos.shape)
print(env_instance.rew_lambda.shape)

# print("Agent Position (start):", env_instance.agent_pos.shape)
# print(env_instance.agent_pos[0])
# print("Agent Theta (orientation):", env_instance.agent_theta.shape)
# print(env_instance.agent_theta[0])
# print("Goal Position:", env_instance.goal_pos.shape)
# print("Map Data (shape):", env_instance.map_data.shape)
# print("Reward Lambda:", env_instance.rew_lambda.shape)
