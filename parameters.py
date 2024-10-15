from rocketpy import Environment,Rocket, Motor, SolidMotor, Flight

COORDINATE_ORIENTATION = "nose_to_tail"

#Parameters to initialize an instance of the class Rocket called Rocket 2023
rocket_2023_params = {
    "radius": 0.0785,
    "mass": 21,
    "inertia": (6.321, 6.321, 0.064),
    "power_off_drag": "/home/stevenchurro/SEDS_DESCENT/powerOffDragCurve.csv",  # Right click file and click Copy Path and insert here
    "power_on_drag": "/home/stevenchurro/SEDS_DESCENT/powerOnDragCurve.csv",
    "center_of_mass_without_motor": 1.46,
    "coordinate_system_orientation": COORDINATE_ORIENTATION
}

#Parameters for add_nose method of Rocket class
nose_2023_params = {
"length" : 0.889,
"kind" : "Von Karman",
"position" : 0,
#Other parameters are optional
"bluffness" : 0,
"power" : None, #Factor that controls the bluntness of the nose cone shape when using a 'powerseries' nose cone kind.
"name" : "Nose Cone",
"base_radius" : None
}


#Parameters for add_trapezoidal_fins method of Rocket class
fins_2023_params = {
    "n" : 3, 
    "root_chord" : 0.356,
    "tip_chord" : 0.075,
    "span" : 0.153,
    "position" : 2.739,
    "cant_angle" : 0.0,
    "sweep_length" : None,
    "sweep_angle" : None,
    "radius" : None,
    "airfoil" : None ,
    "name" : "SEDS 2023 Fins"
}

#Parameters for add_parachute method of Rocket class

main_chute_params = {
    "name" : "main",
    "cd_s" : 10,
    "trigger" : 304,
    "sampling_rate" : 105 ,
    "lag" : 1.5,
    "noise" : (0, 8.3, 0.5)
}

drogue_chute_params = {
    "name" : "drogue",
    "cd_s" : 0.8,
    "trigger" : "apogee",
    "sampling_rate" : 105 ,
    "lag" : 1.5,
    "noise" : (0, 8.3, 0.5)
}




Rocket_2023 = Rocket(**rocket_2023_params)
NoseCone_2023 = Rocket_2023.add_nose(**nose_2023_params)
TrapezoidalFins_2023 = Rocket_2023.add_trapezoidal_fins(**fins_2023_params)
Main_Parachute_2023 = Rocket_2023.add_parachute(**main_chute_params)
Drogue_Parachute_2023 = Rocket_2023.add_parachute(**drogue_chute_params)

