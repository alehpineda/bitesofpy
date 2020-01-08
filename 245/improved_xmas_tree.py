STAR = "+"
LEAF = "*"
TRUNK = "|"


def generate_improved_xmas_tree(rows=10):
    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
       for given rows of leafs (default 10).
       For more information see the test and the bite description"""
    xmas = []
    max_leafs = rows * 2
    xmas.append(STAR.center(max_leafs))

    for row in range(1, max_leafs+1, 2):
        leaf_row = LEAF * row
        xmas.append(leaf_row.center(max_leafs))

    trunk_width = max_leafs // 2 + 1 if rows % 2 == 0 else max_leafs // 2

    for _ in range(2):
        trunk_row = TRUNK * trunk_width
        xmas.append(trunk_row.center(max_leafs))

    return '\n'.join(xmas)
