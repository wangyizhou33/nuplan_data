import os
from nuplan.database.nuplan_db_orm.nuplandb_wrapper import NuPlanDBWrapper

NUPLAN_DATA_ROOT = os.getenv("NUPLAN_DATA_ROOT", "./nuplan-v1.1/")
NUPLAN_MAPS_ROOT = os.getenv("NUPLAN_MAPS_ROOT", "./nuplan-maps-v1.0")
NUPLAN_DB_FILES = os.getenv("NUPLAN_DB_FILES", "./nuplan-v1.1/splits/mini")
NUPLAN_MAP_VERSION = os.getenv("NUPLAN_MAP_VERSION", "nuplan-maps-v1.0")


nuplandb_wrapper = NuPlanDBWrapper(
    data_root=NUPLAN_DATA_ROOT,
    map_root=NUPLAN_MAPS_ROOT,
    db_files=NUPLAN_DB_FILES,
    map_version=NUPLAN_MAP_VERSION,
)

log_db_name = "2021.05.12.22.00.38_veh-35_01008_01518"
log_db = nuplandb_wrapper.get_log_db(log_db_name)

lidar_pcs = log_db.lidar_pc
print(f"The number of lidar_pcs in this log file is {len(lidar_pcs)}.")

example_lidar_pc = lidar_pcs[0]
example_ego_pose = example_lidar_pc.ego_pose
print(f"Lidar_pc token: {example_lidar_pc.token}.")
print(f"Ego pose: <{example_ego_pose.x}, {example_ego_pose.y}, {example_ego_pose.z}>.")


print(f"Lidar boxes: {len(example_lidar_pc.lidar_boxes)}.")
# print(f"Lidar box 0 : {example_lidar_pc.lidar_boxes[0]}.")
# print(f"Lidar box 0 : {example_lidar_pc.boxes()[0]}.")

render = False
if render:
    import matplotlib.pyplot as plt

    example_lidar_pc.render(
        log_db,
        render_future_waypoints=True,
        render_map_raster=True,
        render_vector_map=True,
        render_track_color=True,
        render_future_ego_poses=True,
    ).plot()

    plt.show()
