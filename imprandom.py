#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import urandom


def _choice(poss):
    '''
    Return the index of the value randomly selected.
    '''
    tot = len(poss)
    rand = urandom(tot)
    rand_choice = int.from_bytes(rand, 'big') % tot

    return rand_choice


def choice(poss):
    '''
    Return the value randomly selected.
    '''
    return poss[_choice(poss)]


def _sample(population, sample_size):
    '''
    Select a sample of size sample_size of the population.
    This function modify the population. Selected values are removed from the
    population.
    '''
    res = []
    for i in range(sample_size):
        ind_choice = _choice(population)
        # L'echange permet une execution en temps constant alors qu'un
        # remove aurait été en O(n)
        tmp = population[-1]
        population[-1] = population[ind_choice]
        population[ind_choice] = tmp
        res.append(population.pop())

    return res


def sample(population, sample_size):
    '''
    Select a sample of size sample_size of the population.
    This function do not modify the population.
    '''

    selected = _sample(population, sample_size)
    population += selected

    return selected


def shuffle(population):
    '''
    This function shuffle the list in parameter, no value is returned.
    '''
    sample(population, len(population))


def ponderate_choice(weight, poss):
    '''
    Not tested.
    '''
    tot = sum(weight)
    rand = urandom(tot)
    rand_choice = int.from_bytes(rand, 'big') % tot + 1
    ind_choice = 0
    actual_sum = weight[0]
    while rand_choice - actual_sum > 0:
        ind_choice += 1
        actual_sum += weight[ind_choice]

    return poss[ind_choice]


def main():
    pass


if __name__ == "__main__":
    main()
