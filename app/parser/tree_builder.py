from app.models.node import Node


def build_tree(headings):

    roots = []
    stack = []

    for heading in headings:

        node = Node(
            id=0,
            title=heading["title"],
            level=heading["level"],
            number=heading["number"],
            parent=None
        )

        while stack and stack[-1].level >= node.level:
            stack.pop()

        if stack:
            node.parent = stack[-1]
            stack[-1].children.append(node)
        else:
            roots.append(node)

        stack.append(node)

    return roots