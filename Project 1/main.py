
from typing import *
from dataclasses import dataclass
import unittest
import math

# Ps: Create a model for climate of the Earth
# Create a Data Class for GlobeRect, which includes lower and upper latitude  and western and eastern longitude
@dataclass(Frozen=True)
class GlobeRect:
    lat_upper = float
    lat_lower = float
    long_west = float
    long_east = float


# Create a Data Class for Region, which contains GlobeRect describing the area, name, and terrain
@dataclass(Frozen=True)
class Region:
    GlobeRect = GlobeRect
    name = str
    terrain = str


# Create a class for RegionCondition, which has a region, a year, a population, and rate of greenhouse emissions
@dataclass(Frozen=True)
class RegionCondition:
    Region = Region
    year = int
    population = int
    gas_emission = float


r_ex1: RegionCondition = RegionCondition(Region(GlobeRect(35.54,35.12,-120.4, -120.8), "SLO", "mountain"),2023,47545,917700)
r_ex2: RegionCondition = RegionCondition(Region(GlobeRect(34.4,33.3,-119.78,-117.8), "LA", "ocean"),2023,38490000,44000000)
r_ex3: RegionCondition = RegionCondition(Region(GlobeRect(45.3,40.6,-74.09, -73.9), "NYC", "other"),2023,8800000,49600000)
r_ex4: RegionCondition = RegionCondition(Region(GlobeRect(20.18,18.06,-156.57,-154.5),"Hawaii", "ocean"),2023,198000,19600000)

example_regions = [r_ex1, r_ex2, r_ex3, r_ex4]


# Ps: returns tons of CO2 emitted per person living in a region per year
def emissions_per_capita(regioncondition: RegionCondition) -> float:
    emissions_per_capita = regioncondition.gas_emission / regioncondition.population
    return emissions_per_capita


# Ps: returns area of described part of globe in square km
def region_area(globerect: GlobeRect) -> int:
    # return GlobeRect.lat_upper, GlobeRect.lat_lower, GlobeRect.long_west, GlobeRect.long_east
    R = 6371
    lat_upper_rad = math.radians(globerect.lat_upper)
    lat_lower_rad = math.radians(globerect.lat_lower)
    long_west_rad = math.radians(globerect.long_west)
    long_east_rad = math.radians(globerect.long_east)

    dlong = long_east_rad - long_west_rad
    A = math.sin(
        (lat_lower_rad - lat_upper_rad) / 2 ** 2 + math.cos(lat_upper_rad) * math.cos(lat_lower_rad) * math.sin(
            dlong / 2) ** 2)
    C = 2 * math.atan2(math.sqrt(A), math.sqrt(1 - A))
    E = C - math.pi

    region_area = R ** 2 * E
    return region_area


# Ps: returns CO2 emissions per square km for the region
def emissions_per_square_km(regioncondition: RegionCondition) -> int:
    return regioncondition.gas_emission / region_area(regioncondition.Region.GlobeRect)


# Ps: returns name of region that has the most people per sq km from a list of RegionConditions
def densest(region_list: List) -> str:
    mostPeoplePerKm = 0
    mostPeopleName = ""
    for region in region_list:
        peopleInRegion = region.population
        area = region_area(region.Region.GlobeRect)
        popPerSqrkm = peopleInRegion / area
        if popPerSqrkm > mostPeoplePerKm:
            mostPeoplePerKm = popPerSqrkm
            mostPeopleName = region.Region.name

        return mostPeopleName

#Trace Table
#mostpeopleInRegion = 0
#mostPeopleName = ""
#peopleInRegion = 47545
#area = 0.168
#mostPeoplePerKm = 47545
#mostPeopleName = "SLO"

# Ps: accepts RegionCondition and a number of years and returns a new RegionCondition that estimates condition of region
def project_condition(projectRegion: RegionCondition) -> int:
    if projectRegion.Region.terrain == "ocean":
        return projectRegion.Region.terrain * 1.001
    else:
        if projectRegion.Region.terrain == "mountain":
            return projectRegion.Region.terrain * 1.005
        else:
            if projectRegion.Region.terrain == "forest":
                return projectRegion.Region.terrain * .999
            else:
                if projectRegion.Region.terrain == "other":
                    return projectRegion.Region.terrain * 1.003

# put all test cases in the "Tests" class.
class Tests(unittest.TestCase):
    def emissions_per_capita_test(self):
        self.assertEqual(emissions_per_capita(r_ex1),0.005)
    def region_area_test(self):
        self.assertEqual(region_area(r_ex1),0.168)
    def emissions_per_square_km_tes(self):
        self.assertEqual(emissions_per_square_km(r_ex1),283005)
    def densest(self):
        self.assertEqual(densest(r_ex1),"SLO")




if (__name__ == '__main__'):
    unittest.main()

