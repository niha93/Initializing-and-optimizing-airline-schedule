# Scheduling Analytics
## Creating-and-optimizing-Airline-Schedule

A new startup airline is needing help with creating and optimizing a flight schedule. They have hired you as a
data scientist to create and optimize a flight schedule. The airlines will be all business class and cater to
business travel. All aircraft are configured exactly the same and can fly any route in the system
interchangeably. The airline will serve Dallas Love Field (DAL), Austin Bergstrom (AUS), and Houston Hobby
(HOU).

We have leased 6 aircraft. For sake of simplicity, we will assume all aircraft are configured exactly the same
and can fly any route in the system and we will assume the “tail numbers” are as follows:
Aircraft “Tail Numbers” - T1,T2,T3,T4,T5,T6

All of the airports are on the same time zone. We will use a 4 digit military time format to represent times,
with examples as shown below. Hint: for calculations involving time, it will be helpful to use an epoch of
midnight and calculate the minutes since midnight = (hour * 60) + minutes, but the flight schedule should be
printed in military time. To convert minutes since midnight to military time, hour = minutes since midnight div
60, minutes = minutes since midnight mod 60.

### Due to noise restrictions:
• flights cannot have a departure time of 0559 or earlier
• flights can have a departure time of exactly 0600
• flights can have an arrival time of exactly 2200
• flights cannot have an arrival time of 2201 or later

Flight Times are as follows (assume same flight time either direction, presented in “half alpha” order). Flights
must be scheduled for exactly their flight time (no more, no less).
Airport Airport Flight Time in Minutes
AUS DAL 50
AUS HOU 45
DAL HOU 65


### Number of Gates and Minimum Ground Time at Airports
We have secured gates at all airports. Each airport has a minimum ground time as follows. These are
minimum times. Aircraft may be on the ground longer if designed.
Airport Number of Gates Minimum Ground Time in Minutes
AUS 1 25
DAL 2 30
HOU 3 35

### Optimization Goals
Our optimization goals are to maximize the number of flights, utilize aircraft as evenly as possible, and utilize
gates at airports as evenly as possible, and distribute flights among all 6 markets.
