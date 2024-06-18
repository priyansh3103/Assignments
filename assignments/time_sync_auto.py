#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo
from message_filters import ApproximateTimeSynchronizer, Subscriber
import sensor_msgs
import sensor_msgs.msg


class TimeSyncNode(Node):

    def __init__(self):
        super().__init__("time_sync_auto")
        self.suba = Subscriber(self,sensor_msgs.msg.CameraInfo, "/zed_left/zed_node_0/left/A")
        self.subb = Subscriber(self, sensor_msgs.msg.Image, "/zed_left/zed_node_0/left/B")
        self.subc = Subscriber(self, sensor_msgs.msg.CameraInfo, "/zed_right/zed_node_1/left/C")
        self.subd = Subscriber(self, sensor_msgs.msg.Image, "/zed_right/zed_node_1/left/D")
        self.approx_time_sync = ApproximateTimeSynchronizer([self.suba,self.subb,self.subc,self.subd],10,0.03)
        self.approx_time_sync.registerCallback(self.auto_pub)
        self.time_sync_a = self.create_publisher(CameraInfo, "pub_a", 10)
        self.time_sync_b = self.create_publisher(Image, "pub_b", 10)
        self.time_sync_c = self.create_publisher(CameraInfo, "pub_c", 10)
        self.time_sync_d = self.create_publisher(Image, "pub_d", 10)

    def auto_pub(self,msg1, msg2, msg3, msg4):

        self.time_sync_a.publish(msg1)
        self.time_sync_b.publish(msg2)
        self.time_sync_c.publish(msg3)
        self.time_sync_d.publish(msg4)

def main(args=None):
    rclpy.init(args=args)
    time_sync = TimeSyncNode()
    rclpy.spin(time_sync)
    time_sync.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
        