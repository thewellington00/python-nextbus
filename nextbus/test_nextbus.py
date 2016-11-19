"""Tests for nextbus"""
import nextbus
from nextbus.model import Agency, Route

import unittest

class AgencyListTest(unittest.TestCase):
    def test_agencyList(self):
        #agency list should always return a list of agencies
        agencies = nextbus.agency_list()
        self.assertTrue(len(agencies) > 0, "Agencies list should not be empty")
        self.assertTrue(isinstance(agencies[0], Agency), "agency_list not returning a list of Agencies")
            # if willing to break 2.6, can use assertIsInstance instead

    def test_routeList(self):
        #route list should always return a list of routes filtered by agency.
        routes = nextbus.route_list(agency='sf-muni')
        self.assertTrue(len(routes) > 0,
                        "Routes list should not be empty")
        self.assertTrue(isinstance(routes[0], Route),
                        "route_list not returning a list of Routes")
        self.assertTrue("F-Market & Wharves" in [route.title for route in routes],
                        "A route is missing from the route list")
        self.assertFalse("Sandwich" in [route.title for route in routes],
                         "route_list is including multiple agencies")

    def test_routeConfig(self):
        #route config should return a route object by the given route tag
        route = nextbus.route_config(agency='sf-muni', route='1')
        self.assertTrue(route, "Route is empty")
        self.assertTrue(isinstance(route, Route), "route_config is not returning a Route")
        self.assertEqual(route.title, "1-California",
                         "Route title is not right (expected '{0}', got '{1}'".format("1-California", route.title))


