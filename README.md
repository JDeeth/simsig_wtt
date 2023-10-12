# SimSig WTT

Aims are:

- Enter timings for train working with same level of detail as real WTT
- Extract .WTT files for specific SimSig sims along the route

Options:
- Extract spreadsheets compatible with Luke Briner's SimSig Importer instead
  of complete .WTT files

Thoughts:

## TIPLOC
- id
- name

## Network Link
Physical link between two locations. Can skip intermediate locations if not
mandatory timing points. Not defining an operational route between two points,
only defining a physical set of track assets connecting them.
- from TIPLOC
- to TIPLOC
- line code
- line description
start date, end date, initial direction, final direction, distance, DOO pax,
DOO non pax, RETB, zone, reversible line, power type, RA gauge

## Platform
The physical platform
- id
- location TIPLOC
start/end date, usable length, power supply type, DOO pax / non pax

## Platform limit
Section of platform available for services
- platform id
- direction
start/end date, operational length, name, platform limit note

## Timing load
- traction type
- trailing load
- speed
- RA gauge
description, power type, load, limiting speed

## Timing link
- origin TIPLOC
- destination TIPLOC
- timing load
- line code
start/end date, entry speed, exit speed, sectional running time, description

## Vehicle dimensions
- vehicle number
- net weight
- length
- height
- gauge

## Vehicle
- vehicle number
class, power mode, coupling type, GSM-R/ETCS/DAS/ATO fitment, pax facilities,
accessibility, SDO indicator, corridor connectivity, cycle storage

## Unit formation
- unit number
length, height, net weight, max weight, gauge

## Timetable
- timetable name
creation datetime, last file ref, type, version, start/end date

## Schedule
- path id
- action code
- from date
- to date
- days
- bank hol exemption
- train status
- train id
- operator train id
- STP indicator

## Service capability
- service code
- power type
- timing load
- speed
- operating characteristics
- seating class
- sleeper code
- reservations code
- service branding
- catering code
- train category

## Journey leg change
- location TIPLOC
- train id
- operator train id
- UIC train id

## Origin
- location TIPLOC
- departure time
- public departure
- platform
- line code
- activity code
- eng/path/perf allowance

## Destination
- location TIPLOC
- arrival time
- public arrival
- platform
- line code
- activity code

## Intermediate
- location TIPLOC
- arrival time
- public arrival
- departure time
- public departure
- platform
- arrival line code
- departure line code
- activity code
- eng/path/perf allowance

## Path
- operator code
- origin location
- departure time
- destination location
- arrival time
- path id
- train id
- operator train id
- days
- bank hol exemption

## Journey leg
- journey leg id
- action code
- from location
- to location
- line code
- start time
- end time
- entry speed
- exit speed
- eng/path/perf allowance
- adjustment

## Journey capability
- action code
- journey leg fk
- catering/contract/reservations/sleeper code
- operating characteristics
- train class
- train category

