"""Starter file for the PH 306 warm-up assignment.

Complete the TODOs in this file. The public tests and CodeGrade checks
import these functions directly from ``assignment.py``.
change to commit
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
    v0 : Quantity
        Initial velocity of the object (speed).
    a : Quantity
        Constant acceleration of the object (acceleration).
    t : Quantity
        Elapsed time over which the object moves (time).

    Returns
    -------
    Quantity['length']
        Displacement computed from $v_0 t + \frac{1}{2} a t^2$.
    """
    return v0*t + 0.5*a*t**2


def kinetic_energy(m: Q[u.kg], v: Q[u.m/u.s]) -> Q[u.J]:
    """Return the kinetic energy of an object.

    Parameters
    ----------
    m : Quantity
        Mass of the object.
    v : Quantity
        Velocity of the object.

    Returns
    -------
    Quantity
        Kinetic energy of the object.
    """
    return 0.5*m*v**2


def free_fall_height(
    y0: Q[u.m],
    t: Q[u.s],
    v0: Q[u.m/u.s] = u.Quantity(0.0, u.m / u.s),
    g: Q[u.m/u.s**2] = EARTH_GRAVITY,
) -> Q[u.m]:
    """Return the height of an object in vertical motion.

    Parameters
    ----------
    y0 : Quantity
        Intial height of the object.
    t : Quantity
        Time of flight for object.
    v0 : Quantity
        Intial velocity of the object.
    g : Quantity
        Acceleration of the object due to gravity.

    Returns
    -------
    Quantity['height']
        Height of the object as a function of time.
    """
    return y0+v0*t-0.5*g*t**2


def projectile_range(
        v0: Q[u.m/u.s],
        th0: Q[u.deg],
        g: Q[u.m/u.s**2] = EARTH_GRAVITY
        ) -> Q[u.m]:
    """Return the ideal range of a projectile launched and landing at the same height.

    Parameters
    ----------
    v0 : Quantity
        Intial velocity of the object.
    th0 : Quantity
        The angle the object was launched in degrees.
    g : Quantity, optional
        Acceleration of the object due to gravity.

    Returns
    -------
    Quantity
        The horizontal distance traveled.
    """
    return (v0**2*np.sin(2*th0))/g


def quadratic_solver(
        a: float,
        b: float,
        c: float) -> tuple[float, float]:
    """Return the two roots of a quadratic equation.

    Parameters
    ----------
    a : Quantity
        Constant related to the second degree term in a second degree polynomial.
    b : Quantity
        Constant related to the first degree term.
    c : Quantity
        Constant related to the zeroth degree term.

    Returns
    -------
    Quantity
        The value(s) where a parabola intersect the x-axis.
    """
    return (-b+np.sqrt(b**2-4*a*c))/2*a, (-b-np.sqrt(b**2-4*a*c))/2*a
