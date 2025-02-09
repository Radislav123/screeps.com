from source.creeps.base import BaseCreep
from source.screeps_api import *


# noinspection DuplicatedCode
if True:
    __pragma__('noalias', 'name')
    __pragma__('noalias', 'undefined')
    __pragma__('noalias', 'Infinity')
    __pragma__('noalias', 'keys')
    __pragma__('noalias', 'get')
    __pragma__('noalias', 'set')
    __pragma__('noalias', 'type')
    __pragma__('noalias', 'update')


class Harvester:
    body = [WORK, CARRY, MOVE, MOVE]

    @classmethod
    def spawn(cls, structure_spawn: StructureSpawn):
        structure_spawn.spawnCreep(cls.body, "Harvester_{}".format(Game.time))
