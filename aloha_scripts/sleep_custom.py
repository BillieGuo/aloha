from interbotix_xs_modules.arm import InterbotixManipulatorXS
from robot_utils import move_arms, torque_on

def main():
    puppet_bot_left = InterbotixManipulatorXS(robot_model="wx250s", group_name="arm", gripper_name="gripper", robot_name=f'puppet_left', init_node=True)
    puppet_bot_right = InterbotixManipulatorXS(robot_model="wx250s", group_name="arm", gripper_name="gripper", robot_name=f'puppet_right', init_node=False)
    master_bot_left = InterbotixManipulatorXS(robot_model="vx300s", group_name="arm", gripper_name="gripper", robot_name=f'master_left', init_node=False)
    master_bot_right = InterbotixManipulatorXS(robot_model="wx250s", group_name="arm", gripper_name="gripper", robot_name=f'master_right', init_node=False)

    all_bots = [puppet_bot_left, puppet_bot_right, master_bot_right, master_bot_left]
    for bot in all_bots:
        torque_on(bot)

    puppet_sleep_position = (0, -1.9, 1.55, 0.12, 0.65, 0)
    master_sleep_position = (0, -1.1, 1.24, 0, -0.24, 0)
    sleep_position = [0, -1.88, 1.55, 0, 0.8, 0]
    move_arms(all_bots, [sleep_position] * 4, move_time=4)

if __name__ == '__main__':
    main()
