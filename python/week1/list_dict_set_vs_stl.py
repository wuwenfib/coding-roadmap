"""
Python Week1 · 语言核心
===========================================
1. list / dict / set 对应 STL（对比记忆）
2. Pythonic 写法：推导式、解包、enumerate / zip

面向有 C++ 基础的学习者。运行：python list_dict_set_vs_stl.py
"""

# =====================================================================
# 第一部分：容器对照表（C++ STL ←→ Python）
# =====================================================================
#
# | Python  | 底层结构        | 对应 STL                     | 关键差异                       |
# |---------|----------------|------------------------------|--------------------------------|
# | list    | 动态数组        | std::vector<T>               | 可存异构类型；负索引            |
# | dict    | 哈希表          | std::unordered_map<K,V>      | 3.7+ 保持插入顺序               |
# | set     | 哈希表          | std::unordered_set<T>        | 字面量 {1,2,3}                  |
# | tuple   | 不可变数组      | std::tuple / std::pair       | 不可变，可作 dict 的 key        |
# | (无)     | 红黑树          | std::map / std::set          | Python 无内置有序版，用 sorted  |
# | deque   | 双端队列        | std::deque                   | from collections import deque   |
#
# 注意：Python 没有“有序 map/set”内置类型。需要有序时：
#   - 排序遍历：sorted(d.items())
#   - 频繁有序操作：第三方 sortedcontainers


# =====================================================================
# 第二部分：list —— 对应 std::vector
# =====================================================================
def demo_list():
    print("=" * 50, "\nLIST (≈ std::vector)\n", "=" * 50, sep="")

    # 创建
    nums = [3, 1, 4, 1, 5, 9, 2, 6]

    # 访问：支持负索引（C++ 没有）
    print("nums[0] =", nums[0], "| nums[-1] =", nums[-1])  # 第一个 / 最后一个

    # 切片 nums[start:stop:step]（C++ 需手写循环）
    print("nums[1:4]   =", nums[1:4])    # 索引 1,2,3
    print("nums[::-1]  =", nums[::-1])   # 反转
    print("nums[::2]   =", nums[::2])    # 隔一个取一个

    # 常用方法 ←→ vector
    nums.append(10)          # push_back
    nums.insert(0, 99)       # insert(begin(), 99)
    last = nums.pop()        # pop_back（并返回值）
    nums.sort()              # std::sort(v.begin(), v.end())
    print("sorted:", nums, "| popped:", last)

    # in 判断（vector 需 std::find）
    print("4 in nums?", 4 in nums)
    print("len =", len(nums))  # size()


# =====================================================================
# 第三部分：dict —— 对应 std::unordered_map
# =====================================================================
def demo_dict():
    print("\n" + "=" * 50, "\nDICT (≈ std::unordered_map)\n", "=" * 50, sep="")

    age = {"Alice": 30, "Bob": 25}

    # 访问
    print("age['Alice'] =", age["Alice"])        # 不存在会抛 KeyError
    print("age.get('X', 0) =", age.get("X", 0))  # 安全访问，给默认值

    # 插入 / 更新
    age["Carol"] = 28
    age["Bob"] += 1

    # 遍历（C++ 需 it->first / it->second）
    for name, a in age.items():
        print(f"  {name}: {a}")

    print("keys:", list(age.keys()))
    print("values:", list(age.values()))
    print("'Alice' in age?", "Alice" in age)  # 查 key，count()>0

    # setdefault：key 不存在则设默认（类似 map 的 operator[] 自动构造）
    age.setdefault("Dave", 0)

    # collections.Counter / defaultdict 替代手写计数逻辑
    from collections import Counter, defaultdict
    cnt = Counter("banana")                 # {'a':3,'n':2,'b':1}
    print("Counter:", dict(cnt))

    groups = defaultdict(list)              # value 自动初始化为 []
    for w in ["apple", "ant", "bee"]:
        groups[w[0]].append(w)
    print("defaultdict:", dict(groups))


# =====================================================================
# 第四部分：set —— 对应 std::unordered_set
# =====================================================================
def demo_set():
    print("\n" + "=" * 50, "\nSET (≈ std::unordered_set)\n", "=" * 50, sep="")

    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    print("a | b (并集 union):", a | b)
    print("a & b (交集 intersection):", a & b)
    print("a - b (差集 difference):", a - b)
    print("a ^ b (对称差):", a ^ b)

    a.add(99)
    a.discard(99)            # 不存在也不报错（remove 会报错）
    print("3 in a?", 3 in a)  # O(1)，比 list 的 in（O(n)）快

    # 去重经典用法
    dup = [1, 1, 2, 3, 3, 3]
    print("去重:", list(set(dup)))

    # 空 set 必须用 set()，{} 是空 dict！
    empty = set()
    print("空 set 类型:", type(empty).__name__)


# =====================================================================
# 第五部分：Pythonic 写法
# =====================================================================
def demo_pythonic():
    print("\n" + "=" * 50, "\nPYTHONIC 写法\n", "=" * 50, sep="")

    # ---- 5.1 推导式 (comprehension) ----
    # 列表推导式 = map + filter 的简洁形式
    squares = [x * x for x in range(6)]                 # 平方
    evens = [x for x in range(10) if x % 2 == 0]        # 带过滤
    matrix = [[i * j for j in range(3)] for i in range(3)]  # 嵌套
    print("squares:", squares)
    print("evens:", evens)
    print("matrix:", matrix)

    # 字典推导式
    sq_map = {x: x * x for x in range(5)}
    print("dict 推导:", sq_map)

    # 集合推导式
    s = {x % 3 for x in range(10)}
    print("set 推导:", s)

    # 生成器表达式（惰性求值，省内存）—— 用 () 而非 []
    total = sum(x * x for x in range(1000))
    print("生成器求和:", total)

    # ---- 5.2 解包 (unpacking) ----
    a, b, c = 1, 2, 3                      # 多变量赋值
    a, b = b, a                            # 交换，无需临时变量
    print("交换后 a,b =", a, b)

    first, *rest = [1, 2, 3, 4, 5]         # * 收集剩余
    print("first:", first, "| rest:", rest)

    *init, last = [1, 2, 3, 4]
    print("init:", init, "| last:", last)

    # 合并字典 / 列表（解包）
    d1, d2 = {"x": 1}, {"y": 2}
    merged = {**d1, **d2}                   # {'x':1,'y':2}
    combined = [*[1, 2], *[3, 4]]           # [1,2,3,4]
    print("merged:", merged, "| combined:", combined)

    # 函数传参解包
    def add(x, y, z):
        return x + y + z
    args = (1, 2, 3)
    print("解包传参 add(*args):", add(*args))

    # ---- 5.3 enumerate：带索引遍历 ----
    # 替代 C++ 的 for(int i=0; i<v.size(); ++i)
    fruits = ["apple", "banana", "cherry"]
    for i, fruit in enumerate(fruits):
        print(f"  [{i}] {fruit}")
    # 自定义起始索引
    for i, fruit in enumerate(fruits, start=1):
        print(f"  第{i}个: {fruit}")

    # ---- 5.4 zip：并行遍历多个序列 ----
    names = ["Alice", "Bob", "Carol"]
    ages = [30, 25, 28]
    for name, age in zip(names, ages):
        print(f"  {name} is {age}")

    # zip 构造 dict
    name_age = dict(zip(names, ages))
    print("zip→dict:", name_age)

    # zip(*matrix) 实现转置
    m = [[1, 2, 3], [4, 5, 6]]
    transposed = list(zip(*m))
    print("转置:", transposed)


# =====================================================================
# 小结：何时用哪个容器
# =====================================================================
# - 有序、可重复、按位置访问        → list
# - 键值映射、快速查找              → dict
# - 去重、集合运算、成员判断        → set
# - 不可变、作为 key、固定字段      → tuple
#
# 性能记忆：
#   list  的 in        → O(n)
#   dict/set 的 in     → O(1)（哈希）
#   需要频繁成员判断时，用 set 而非 list！


if __name__ == "__main__":
    demo_list()
    demo_dict()
    demo_set()
    demo_pythonic()