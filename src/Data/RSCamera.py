import pyrealsense2 as rs


class RSCamera:
    def __init__(self, serial, name="cam01", fps=15):
        # Configure depth and color streams

        self.__config__ = rs.config()
        self.__config__.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, fps)
        self.__config__.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
        self.name = name
        self.__config__.enable_device(str(serial))
        self.__pipeline__ = rs.pipeline()

    def start(self):
        try:
            # Start streaming
            self.__pipeline__.start(self.__config__)
            return True
        except Exception as e:
            print(e)
            return False

    def get_frame(self):
        try:
            # Wait for a coherent pair of frames: depth and color
            frames = self.__pipeline__.wait_for_frames()

            depth_frame = frames.get_depth_frame()
            color_frame = frames.get_color_frame()

            if not depth_frame or not color_frame:
                return None
            else:
                return color_frame, depth_frame
        except Exception as e:
            print(e)
            return None

    # Stop streaming
    def stop(self):
        self.__pipeline__.stop()

    def get_profile_intrinsics(self, profile):
        return rs.video_stream_profile(profile).get_intrinsics()

    def pointcloud(self):
        return rs.pointcloud()

    def deproject_pixel_to_point(self, intrinsics, x, y, d):
        return rs.rs2_deproject_pixel_to_point(intrinsics, [x, y], d)


def _search(_dict, searchFor):
    for k, values in _dict.items():
        for v in values.values():
            if searchFor == v:
                return k
    return None


def config_devices():
    devices = []
    cams = {'top': {'serial': 839112060624, 'available': False},
            'back': {'serial': 844212071705, 'available': False}}

    print(cams)
    context = rs.context()
    for dev in context.devices:
        serial_number = int(dev.get_info(rs.camera_info.serial_number))
        key = _search(cams, serial_number)
        if key is not None:
            cams[key]["available"] = True
    print(cams)
    for k, v in cams.items():
        if v["available"]:
            try:
                new_cam = RSCamera(name=k, serial=v["serial"])
                devices.append(new_cam)
                print("everything were fine.")
            except:
                print("there are problems creating the camera pipeline")
    cams = {}
    return devices
