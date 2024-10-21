from rocketpy import SolidMotor, Motor


motor_2023 = {
    "thrust_source" : "/home/stevenchurro/SEDS_DESCENT/Files/AeroTech_M1845NT.eng",
    "dry_mass": 2.91, # Mass without propelent
    "dry_inertia" : (0.138, 0.138, 0.006),
    "burn_time" : 4.5,
    "center_of_dry_mass_position" : 0.105, #Without Properlent 0.305
    "grains_center_of_mass_position" : 0.185,
    "grain_number" :3,
    "grain_separation" :5 / 1000,
    "grain_density":1900, #1950 1267
    "grain_outer_radius":0.0415,
    "grain_initial_inner_radius" : 0.01752,
    "grain_initial_height" :0.1524, # Before: 0.0254
    "nozzle_radius":0.0223,
    "throat_radius":0.013,
    "nozzle_position":0,
    "coordinate_system_orientation":"nozzle_to_combustion_chamber"
}

RMS_98_7680 = SolidMotor(**motor_2023)