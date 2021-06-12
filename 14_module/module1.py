import sys
bmodule = sys.builtin_module_names
print(bmodule)

dir(__builtins__)

# module 참조 : import
import random
import random as rd   # 별칭
from random import randint   # 이 경우 . 없이 바로 randint만 사용해도 됨
from random import randint as rd   # 별칭

random.randint(1, 10)
rd.randint(1, 10)
print(randint(1, 10))   # 이와 같이!