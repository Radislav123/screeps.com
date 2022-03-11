
1) необходимо прописывать полный путь импорта
```python
# noinspection PyUnresolvedReferences
from source.creeps.base import BaseCreep
```
2) `__pragma__('noalias', ...)` обязательны, без них Transcrypt неправильно конвертирует
   (получается что-то вроде `py_keys` вместо `keys`)
```python
from source.screeps_api import __pragma__

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
```
