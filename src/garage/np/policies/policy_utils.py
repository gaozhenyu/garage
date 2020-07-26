"""Module for utility functions commonly used by policies."""

import numpy as np


def flatten_if_unflattened(observation_space, observation):
    """Flattens observation to a numpy.ndarray if it is not.

    Args:
        observation_space(akro.Space): The observation space that
            observation comes from.
        observation(observation_space.dtype): The observations to be flattened
            if necessary.

    Returns:
        np.ndarray: Flattened observations.
    """
    if not isinstance(observation, np.ndarray):
        observation = (observation_space.flatten(observation))
    return observation


def flatten_n_if_unflattened(observation_space, observations):
    """Flattens a batch of observations to a numpy.ndarray if it is not.

    Args:
        observation_space(akro.Space): The observation space that
            observations comes from.
        observations(observation_space.dtype): The observations to be flattened
            if necessary.

    Returns:
        np.ndarray: Flattened observations.
    """
    if isinstance(observations, list):
        if isinstance(observations[0], np.ndarray):
            return observations
    if not isinstance(observations, np.ndarray):
        observations = (observation_space.flatten_n(observations))
    return observations
