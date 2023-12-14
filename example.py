#!/usr/bin/python
# -*- coding: utf-8 -*-
import traffic_config
import traffic
import tools
import common_types

import time


def run_traffic(config_manager, with_external_decision=False):

    # Initialization of all required objects

    ego = traffic.ControllableEgo(config_manager,
                                  with_external_decision)
    traffic_lib = traffic.Traffic(config_manager)
    visualizer = tools.Visualizer(config_manager, False)
    # Here we want each traffic light to stay green for 20 seconds
    controller_scheduler = traffic.ControllerScheduler(config_manager,
            20)

    vehicles = []

    is_running = True
    is_paused = False

    update_visualizer = True
    update_visualizer_fps_frame_limit = 25
    update_visualizer_frame_counter = 0

    while is_running:
        is_paused = visualizer.is_paused()
        if not is_paused:
            start_time = time.time()
            # Set to keep decision if we want external control

            if with_external_decision is True:
                ego.set_decision(traffic.Decision.KEEP)

            [light_states_simulation, light_states_visualizer] = \
                controller_scheduler.update()
            ego_state = ego.drive(vehicles, light_states_simulation)
            vehicles = traffic_lib.sync([ego_state],
                    light_states_simulation)
            vehicles.append(ego_state)

        # Update visualzer at 25 FPS

        if update_visualizer:
            # smoothed fps calculation can be sent here to visualizer
            # this will give accurate calculation RT factor
            is_running = visualizer.update(config_manager.fps,
                    vehicles, light_states_visualizer)
            update_visualizer = False

        if update_visualizer_frame_counter \
            == update_visualizer_fps_frame_limit:
            update_visualizer = True
            update_visualizer_frame_counter = 0

        update_visualizer_frame_counter += 1


if __name__ == '__main__':

    #  Let's start from the beggining
    #  We only give the required variable called map path
    #  This is the only required variable all others can take on default value

    # Note Close the current window or press q to quit and
    # let the next window start

    map_file_path = \
        'maps/A10-IN-1-19KM_HW_AC_DE_BER_RELEASE_20210510.xodr'
    config_manager = \
        traffic_config.TrafficConfigManager(map_path=map_file_path)
    run_traffic(config_manager)


    # Rates based spawner is useful for replicating real world
    # traffic flows such as for a map you know the flow rate
    # at the edges of the map.
    # When we want to observe how the the traffic behaves at junctions
    # intersections and around traffic lights and more importantly 
    # how it changes with adjustments to these things
    # Change the traffic amount to a more substantial amount
    
    config_manager.traffic_amount = 500
    config_manager.spawner_strategy = \
        traffic_config.SpawnerStrategy.SPAWN_RATES
    odr_lane = common_types.OpenDriveRoadInfo(road_id=268,
            lane_id=-2, lane_section=0)
    config_manager.spawn_points = [[odr_lane, 1800]]
    run_traffic(config_manager)

    # We can make a copy and change sensor range
    # and change the traffic amount as well
    # Press S to visualize the sensor range in visualizer
    # Also reset spawner strategy to what we were using previously

    config_manager.spawner_strategy = \
        traffic_config.SpawnerStrategy.SPAWN_AROUND_EGO_VISION
    config_manager_copy = config_manager.copy()
    config_manager_copy.ego_sensor_range = 50
    config_manager_copy.traffic_amount = 50
    run_traffic(config_manager_copy)

    # Now let's try to play around with road user profiles
    # By default we have the following configuration
    # The profiles have a lot configuration parameters
    # We will describe the type and it's percentage only here
    # to in order to simplify things
    # (Car, 0.0) -> Ego Profile, The first profile must always be ego
    # (Car, 0.85) -> Car Profile with percentage 0.85
    # (Bus, 0.03) -> Bus Profile with percentage 0.03
    # (Truck, 0.1) -> Truck Profile with percentage 0.1
    # (Motrocycle, 0.02) -> Motorcycle Profile with percentage 0.02
    # The configuration described above defines a simulation in which
    # we will roughly observe the above percentages of vehicle types
    # as seen.
    # Note we can have multiple profiles of the same type and any other
    # mix possible. The only caveat is the percentage other than ego
    # should sum to 1.0
    #
    # Let's create a traffic simulation with only buses
    # InputRoadUserProfile is the object used to define a road user profile
    # If you know the parameters you can construct the whole object to your
    # liking however if you don't have accurate values for a given profile
    # We have given the option to specify the type of profile that you want
    # We will construct the complete configuration just from the RoadUserType

    roaduser_bus = \
        traffic_config.InputRoadUserProfile(traffic_config.RoadUserType.BUS)
    roaduser_bus_long = \
        traffic_config.InputRoadUserProfile(traffic_config.RoadUserType.BUS)
    
    # Let's change the length of the bus to 15 meters instead of the default
    roaduser_bus_long.length = 15

    # Get the roaduser_profiles which are already present in
    # TrafficConfigManager object and take the ego profile from
    # that i.e the first object from the list and than again 0
    # object as the objects of list are of type
    # Tuple[InputRoadUserProfile, Percentage]

    ego_profile = config_manager.roaduser_profiles[0][0]

    # Now construct the road user profiles with 50 percent default bus profiles
    # and 50 percent buses with adjusted length 15 meters.

    config_manager.roaduser_profiles = [[ego_profile, 0.0],
            [roaduser_bus, 0.5], [roaduser_bus_long, 0.5]]
    run_traffic(config_manager)

    # Each vehicle profile has associated driver profiles as well
    # By default only one driver profile is pushed with 1.0 percentage
    # More can be pushed as well if needed if user wants same vehicle profile
    # with different types of driver driving them
    # let's change the default moderate profile to an aggressive one
    # So we will see more aggressive values for each of the road users
    # In this configuration, We will set all vehicle profiles to cars

    roaduser_car = \
        traffic_config.InputRoadUserProfile(traffic_config.RoadUserType.CAR)

    # Change the driver profile to generate more aggressive drivers
    # Change the driver profile target speed to 40 Km/h so they will
    # drive more slowly
    
    driver_profile = roaduser_car.driver_profiles[0][0]
    driver_profile.p1 = 0.0
    driver_profile.p2 = 0.0
    driver_profile.p3 = 0.0
    driver_profile.p4 = 1.0
    driver_profile.target_speed = 40
    roaduser_car.driver_profiles = [[driver_profile, 1.0]]

    config_manager.roaduser_profiles = [[ego_profile, 0.0],
            [roaduser_car, 1.0]]
   
    # We will also run the ego with external decision
    # We will enforce it keep in the current lane
    # Other decisions are also available like left and right
    # If the decision is not possible it will be ignored
    # and the result will be returnd in the set_decision()
    # function, this is acheived by passing True as second
    # parameter and than handled inside run_traffic() function
    # with the ControllableEgo object

    run_traffic(config_manager, True)

    # Let's change map to an urban one with traffic lights to
    # see the traffic lights in action

    config_manager.map_path = \
        'maps/BMW-RA+JT-Headquater-11KM_UR_AC_DE_MUN_RELEASE_20210901.xodr'

    # Let's change it to pedestrians and cars

    roaduser_pedestrian = \
        traffic_config.InputRoadUserProfile(
                       traffic_config.RoadUserType.PEDESTRIAN)

    config_manager.roaduser_profiles = [[ego_profile, 0.0],
            [roaduser_car, 0.4], [roaduser_pedestrian, 0.6]]

    # Change the spawner to spawn everywhere

    config_manager.spawner_strategy = \
        traffic_config.SpawnerStrategy.SPAWN_EVERYWHERE

    # Increase the traffic amount to fill out the map

    config_manager.traffic_amount = 400

    run_traffic(config_manager)

    # We have tried to explain some of the available options in this example
    # please use the help(module) help(class) command to see detailed
    # explanation of the options available
    # If any confusions don't hesitate to post on the github repo

