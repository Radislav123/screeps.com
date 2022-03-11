from source.screeps_api import *
from source.creeps import harvester

# These are currently required for Transcrypt in order to use the following names in JavaScript.
# Without the 'noalias' pragma, each of the following would be translated into something like 'py_Infinity' or
#  'py_keys' in the output file.
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


def main():
    """Main game logic loop."""

    # Run each creep
    print("total creeps: {}".format(len(Game.creeps)))
    for name in Object.keys(Game.creeps):
        creep = Game.creeps[name]
        print("creep: {}".format(creep.name))

    # Run each spawn
    for name in Object.keys(Game.spawns):
        structure_spawn = Game.spawns[name]
        if not structure_spawn.spawning and structure_spawn.room.energyAvailable >= len(harvester.Harvester.body * 50):
            harvester.Harvester.spawn(structure_spawn)
        else:
            print(Game.time)


module.exports.loop = main
