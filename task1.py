class TreeStore:
    def __init__(self, items: list):
        self.items = items
        self.tree_parent = {}
        self.create_Tree()

    def getAll(self) -> list[dict]:
        """Возвращает изначальный массив объектов"""
        return self.items

    def getItem(self, id: int):
        """Принимает id элемента и возвращает сам объект элемента"""
        try:
            return self.items[id - 1]
        except:
            return None


    def create_Tree(self):
        """Формируется словарь вида:
            * KEY : id-элемента
            * VALUE: словарь с ключами:
                - parent: id-родителя
                - type: тип элемента
                - child: список id-потомков
            """
        self.tree_parent = {item.get('id'): dict(id=item.get('id'), parent=item.get('parent'), type=item.get('type'),  child=[]) for item in self.items}
        [self.tree_parent[item.get('parent')]['child'].append(item.get('id')) for item in self.items[1:]]

    def getAllParents(self, id: int, __memory__=None) -> list[dict]:
        """
        Возвращает последовательную цепочку словарей родительских элементов до корня дерева
        :param id: ID элемента, для которого ищется цепочка родителей
        :param __memory__: переменнная для хранения промежуточных данных
        """
        if __memory__ is None:
            __memory__ = []
        if (parentId := self.tree_parent[id].get('parent')) == 'root':
            return __memory__
        else:
            __memory__.append(dict(id=parentId, parent=self.tree_parent[parentId].get('parent')))
            if (type_item:=self.tree_parent[parentId].get('type')):
                __memory__[-1].update(dict(type=type_item))
            __memory__ = self.getAllParents(parentId, __memory__)
        return __memory__


    def getChildren(self, id: int) -> list[dict]:
        """
        Возвращает массив дочерних элементов
        :param id: ID элемента, для которого осуществляется поиск потомков
        """
        return [{k: v for k, v in self.tree_parent[childID].items() if k != 'child'}
                for childID in self.tree_parent.get(id).get('child')]


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(items)

for param_test, test in zip([None, 7, 4, 5, 7],
                             [ts.getAll, ts.getItem, ts.getChildren, ts.getChildren, ts.getAllParents]):
    print(f'test: {test.__name__}({param_test if param_test else ""}):\n', test(param_test) if param_test else test(), end='\n'*2)

