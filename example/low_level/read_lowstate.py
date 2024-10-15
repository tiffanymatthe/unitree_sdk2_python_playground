import time
import sys
from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize
from unitree_sdk2py.idl.default import unitree_go_msg_dds__LowCmd_
from unitree_sdk2py.idl.unitree_go.msg.dds_ import LowCmd_

import unitree_legged_const as go2


def LowStateHandler(msg: LowCmd_):
    
    # print front right hip motor states
    print(msg)
    # print("FR_0 motor state: ", msg.motor_state[go2.LegID["FR_0"]])
    # print("IMU state: ", msg.imu_state)
    # print("Battery state: voltage: ", msg.power_v, "current: ", msg.power_a)


if __name__ == "__main__":
    if len(sys.argv)>1:
        ChannelFactoryInitialize(0, sys.argv[1])
    else:
        ChannelFactoryInitialize(0)
    sub = ChannelSubscriber("rt/lowcmd", LowCmd_)
    sub.Init(LowStateHandler, 10)

    while True:
        time.sleep(10.0)
