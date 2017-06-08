import numpy as np

from foolbox.attacks import SaliencyMapAttack as Attack


def test_attack(bn_adversarial):
    adv = bn_adversarial
    attack = Attack()
    attack(adv)
    assert adv.get() is None
    assert adv.best_distance().value() == np.inf


def test_targeted_attack(bn_targeted_adversarial):
    adv = bn_targeted_adversarial
    attack = Attack()
    attack(adv)
    assert adv.get() is not None
    assert adv.best_distance().value() < np.inf


def test_targeted_attack_slow(bn_targeted_adversarial):
    adv = bn_targeted_adversarial
    attack = Attack()
    attack(adv, fast=False)
    assert adv.get() is not None
    assert adv.best_distance().value() < np.inf


def test_targeted_attack_max(bn_targeted_adversarial):
    adv = bn_targeted_adversarial
    attack = Attack()
    attack(adv, max_perturbations_per_pixel=1)
    assert adv.get() is not None
    assert adv.best_distance().value() < np.inf