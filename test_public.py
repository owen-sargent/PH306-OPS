import numpy as np
from astropy import units as u

import assignment


def test_distance_traveled():
    result = assignment.distance_traveled(2.0 * u.m / u.s, 3.0 * u.m / u.s**2, 4.0 * u.s)

    assert isinstance(result, u.Quantity), "distance_traveled must return an astropy Quantity"
    assert result.unit.is_equivalent(u.m), "distance_traveled must return a length"
    assert np.isclose(result, 32.0 * u.m), "distance_traveled returned the wrong value"


def test_kinetic_energy():
    result = assignment.kinetic_energy(2.0 * u.kg, 3.0 * u.m / u.s)

    assert isinstance(result, u.Quantity), "kinetic_energy must return an astropy Quantity"
    assert result.unit.is_equivalent(u.J), "kinetic_energy must return an energy"
    assert np.isclose(result, 9.0 * u.J), "kinetic_energy returned the wrong value"


def test_free_fall_height():
    result = assignment.free_fall_height(100.0 * u.m, 2.0 * u.s)

    assert isinstance(result, u.Quantity), "free_fall_height must return an astropy Quantity"
    assert result.unit.is_equivalent(u.m), "free_fall_height must return a length"
    assert np.isclose(result, 80.38 * u.m), "free_fall_height returned the wrong value"


def test_projectile_range():
    result = assignment.projectile_range(20.0 * u.m / u.s, 45.0 * u.deg)

    assert isinstance(result, u.Quantity), "projectile_range must return an astropy Quantity"
    assert result.unit.is_equivalent(u.m), "projectile_range must return a length"
    assert np.isclose(result, 40.77471967380224 * u.m), "projectile_range returned the wrong value"


def test_quadratic_solver():
    result = assignment.quadratic_solver(1.0, -3.0, 2.0)
    result = tuple(sorted(result))  # Sort the roots for consistent comparison

    assert isinstance(result, tuple), "quadratic_solver must return a tuple"
    assert len(result) == 2, "quadratic_solver must return a tuple of length 2"
    assert np.isclose(result[0], 1.0), "quadratic_solver returned the wrong value for the first root"
    assert np.isclose(result[1], 2.0), "quadratic_solver returned the wrong value for the second root"
