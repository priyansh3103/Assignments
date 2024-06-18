#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo


class TimeSyncNode(Node):

    def __init__(self):
        super().__init__("time_sync")
        self.image_sub_b = self.create_subscription(Image,"/zed_left/zed_node_0/left/B", self.b_callback, 10)
        self.image_sub_d = self.create_subscription(Image,"/zed_right/zed_node_1/left/D", self.d_callback, 10)
        self.camerainfo_sub_a = self.create_subscription(CameraInfo,"/zed_left/zed_node_0/left/A", self.a_callback, 10)
        self.camerainfo_sub_c = self.create_subscription(CameraInfo,"/zed_right/zed_node_1/left/C", self.c_callback, 10)
        self.time_sync_a = self.create_publisher(CameraInfo, "pub_a", 10)
        self.time_sync_b = self.create_publisher(Image, "pub_b", 10)
        self.time_sync_c = self.create_publisher(CameraInfo, "pub_c", 10)
        self.time_sync_d = self.create_publisher(Image, "pub_d", 10)
        self.a_sec = 0
        self.b_sec = 0
        self.c_sec = 0
        self.d_sec = 0
        self.a_nsec = 0
        self.b_nsec = 0
        self.c_nsec = 0
        self.d_nsec = 0
        self.c = CameraInfo()
        self.a = CameraInfo()
        self.b = Image()
        self.d = Image()

    def c_callback(self, cic: CameraInfo):
        self.c_sec = cic.header.stamp.sec
        self.c_nsec = cic.header.stamp.nanosec
        self.c = cic

    def d_callback(self, id: Image):
        self.d_sec = id.header.stamp.sec
        self.d_nsec = id.header.stamp.nanosec
        self.d = id

    def b_callback(self, ib: Image):
        self.b_sec = ib.header.stamp.sec
        self.b_nsec = ib.header.stamp.nanosec
        self.b = ib

    def a_callback(self, cia: CameraInfo):
        self.a_sec = cia.header.stamp.sec
        self.a_nsec = cia.header.stamp.nanosec
        self.a = cia
        if self.c_nsec == self.d_nsec and self.a_nsec == self.b_nsec:
            if self.a_nsec - self.c_nsec <= 30000000:
                self.time_sync_a.publish(self.a)
                self.time_sync_c.publish(self.c)
                self.time_sync_b.publish(self.b)
                self.time_sync_d.publish(self.d)
                self.get_logger().info('seconds: "%s"' % str(self.a_sec))
                self.get_logger().info('nano_a: "%s"' % str(self.a_nsec))
                self.get_logger().info('nano_c: "%s"' % str(self.c_nsec))


def main(args=None):
    rclpy.init(args=args)
    time_sync = TimeSyncNode()
    rclpy.spin(time_sync)
    time_sync.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()