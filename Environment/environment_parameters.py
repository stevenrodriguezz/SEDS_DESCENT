'''
https://weather.uwyo.edu/cgi-bin/sounding?region=samerf&TYPE=TEXT%3ALIST&YEAR=2023&MONTH=06&FROM=2200&TO=2212&STNM=72364

Link above provides Pressure< Temperature, Height

However Wind U and Wind V are given in degrees and knots respectively when they both should be in m/s

To convert Wind U to m/s 


'''
from rocketpy import Environment

'Lets try using regular inputs from APIs'
'Launch was June 22, 2023 at 3:30pm New Mexico time or 9:30PM UTC'


Launch_Date_2023 = [2023, 6, 22, 12] 
SpacePort_2023_Env = Environment(latitude=32.990254, longitude=-106.974998, elevation=1400)
SpacePort_2023_Env.set_date(Launch_Date_2023 , timezone = "UTC")
SpacePort_2023_Env.set_atmospheric_model('wyoming_sounding' , file = "http://weather.uwyo.edu/cgi-bin/sounding?region=samerf&TYPE=TEXT%3ALIST&YEAR=2023&MONTH=06&FROM=2200&TO=2212&STNM=72364")

SpacePort_2023_Env.info()