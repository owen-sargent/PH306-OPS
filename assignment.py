"""Starter file for the PH 306 warm-up assignment.

Complete the TODOs in this file. The public tests and CodeGrade checks
import these functions directly from ``assignment.py``.
"""

# Numerical Imports
import numpy as np
from astropy import units as u
from astropy.units import Quantity as Q


# --- Constants --- #
EARTH_GRAVITY = u.Quantity(9.81, u.m / u.s**2)  # Earth's gravitational acceleration


# --- Functions to Implement --- #
@u.quantity_input(v0="speed", a="acceleration", t="time")
def distance_traveled(v0: Q[u.m/u.s], a: Q[u.m/u.s**2], t: Q[u.s]) -> Q[u.m]:
    """Return the displacement for constant acceleration.

    Parameters
    ----------
    v0 : Quantity['speed']
        Initial velocity of the object.
    a : Quantity['acceleration']
        Constant acceleration of the object.
    t : Quantity['time']
        Elapsed time over which the object moves.

    Returns
    -------
    Quantity['length']
        Displacement computed from $v_0 t + \frac{1}{2} a t^2$.
    """
    raise NotImplementedError("Implement distance_traveled")


def kinetic_energy(m: Q[u.kg], v: Q[u.m/u.s]) -> Q[u.J]:
    """Return the kinetic energy of an object.
    """
    raise NotImplementedError("Implement kinetic_energy")


def free_fall_height(
    y0: Q[u.m],
    t: Q[u.s],
    v0: Q[u.m/u.s] = u.Quantity(0.0, u.m / u.s),
    g: Q[u.m/u.s**2] = EARTH_GRAVITY,
) -> Q[u.m]:
    """Return the height of an object in vertical motion.
    """
    raise NotImplementedError("Implement free_fall_height")



def projectile_range(v0, th0, g = EARTH_GRAVITY):
    """Return the ideal range of a projectile launched and landing at the same height.
    """
    raise NotImplementedError("Implement projectile_range")


def quadratic_solver(a: float, b, c) -> tuple[float, float]:
    """Return the two roots of a quadratic equation.
    """
    raise NotImplementedError("Implement quadratic_solver")
