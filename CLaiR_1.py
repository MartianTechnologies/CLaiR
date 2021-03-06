#Train the Agent
python -m spinup.run ppo --exp_name LunarLanderx1 --env LunarLanderContinuous-v2 --clip_ratio 0.2 --hid "[128,64]" --gamma 0.999 --vf_lr 0.0024 --seed 20 --epochs 150 --pi_lr 0.0002 --target_kl 0.005 --data_dir /path --dt

#Test the Agent
python -m spinup.run test_policy /path
