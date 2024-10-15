from rocketpy import Environment,Rocket, Motor, SolidMotor, Flight

COORDINATE_ORIENTATION = "nose_to_tail"

rocket_2023_params = {
    "radius": 0.0785,
    "mass": 21,
    "inertia": (6.321, 6.321, 0.064),
    "power_off_drag": "/home/stevenchurro/SEDS_DESCENT/powerOffDragCurve.csv",  # Right click file and click Copy Path and insert here
    "power_on_drag": "/home/stevenchurro/SEDS_DESCENT/powerOnDragCurve.csv",
    "center_of_mass_without_motor": 1.46,
    "coordinate_system_orientation": COORDINATE_ORIENTATION
}

#Parameters to initialize an instance of the class Rocket called Rocket 2023
""" radius = 0.0785
mass = 21
inertia = (6.321, 6.321, 0.064)
power_off_drag = "/home/stevenchurro/SEDS_DESCENT/powerOffDragCurve.csv" #Right click file and click Copy Path and insert here
power_on_drag = "/home/stevenchurro/SEDS_DESCENT/powerOnDragCurve.csv"
center_of_mass_without_motor = 1.46
coordinate_system_orientation_NT = "nose_to_tail" # Can be either nose to tail 
coordinate_system_orientation_TN = "tail_to_nose" # or vice versa """

Rocket_2023 = Rocket(**rocket_2023_params)

#Parameters for add_nose method of Rocket class

length_nose = 0.889
kind_nose = "Von Karman"
position_nose = 0
#Other parameters are optional
bluffness_nose = 0
power_nose = None #Factor that controls the bluntness of the nose cone shape when using a 'powerseries' nose cone kind.
name_nose = "Nose Cone"
base_radius_nose = None

NoseCone_2023 = Rocket_2023.add_nose(
    length = length_nose,
    kind = kind_nose,
    position = position_nose
)

#Parameters for add_trapezoidal_fins method of Rocket class

num_of_fins = 3
root_chord_fins = 0.356
tip_chord_fins = 0.075
span_fins = 0.153
position_fins = 2.739
cant_angle_fins = 0.0
sweep_length_fins = None
sweep_angle_fins = None
radius_fins = None
airfoil_fins = None 
name_fins = "SEDS 2023 Fins"



TrapezoidalFins_2023 = Rocket_2023.add_trapezoidal_fins(
    n = num_of_fins,
    root_chord = root_chord_fins,
    tip_chord = tip_chord_fins,
    span = span_fins,
    position = position_fins,
    cant_angle = cant_angle_fins
)

#Parameters for add_parachute method of Rocket class
name_main = "main"
cd_s_main = 10
trigger_main = 304
sampling_rate_main = 105 
lag_main = 1.5
noise_main = (0, 8.3, 0.5)

name_drogue = "drogue"
cd_s_drogue = 0.8
trigger_drogue = "apogee"
sampling_rate_drogue = 105 
lag_drogue = 1.5
noise_drogue = (0, 8.3, 0.5)



Main_Parachute_2023 = Rocket_2023.add_parachute(
    name = name_main,
    cd_s = cd_s_main,
    trigger = trigger_main, 
    sampling_rate= sampling_rate_main, 
    lag= lag_main, 
    noise= noise_main
)

Drogue_Parachute_2023 = Rocket_2023.add_parachute(
    name = name_drogue,
    cd_s = cd_s_drogue,
    trigger = trigger_drogue, 
    sampling_rate= sampling_rate_drogue, 
    lag= lag_drogue, 
    noise= noise_drogue
)

