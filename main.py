type Edge = tuple[tuple[float, float], tuple[float, float]] # 2 dimensional edge

def dx(edge: Edge):
    return edge[0][0] - edge[1][0]

def dy(edge: Edge):
    return edge[0][1] - edge[1][1]

def lower(edge: Edge, axis: int):
    return min(edge[0], edge[1], key=lambda p: p[axis])[axis]

def upper(edge: Edge, axis: int):
    return max(edge[0], edge[1], key=lambda p: p[axis])[axis]

def hv_intersecting(parallel: Edge, perpendicular: Edge, axis: int):
    return lower(parallel, axis) <= perpendicular[0][axis] <= upper(parallel, axis) and lower(perpendicular, ~axis) <= parallel[0][~axis] <= upper(perpendicular, ~axis)

def edges_intersecting(a: Edge, b: Edge) -> bool:
    delta_a = [dx(a), dy(a)]
    delta_b = [dx(b), dy(b)]

    axis = 0 # set independent axis to x axis

    if delta_a[axis] == 0 or delta_b[axis] == 0:
        if delta_a[~axis] == 0 or delta_b[~axis] == 0:
            return hv_intersecting(a, b, axis ^ int(delta_a[axis] == 0))
        axis = 1

    # gradients
    m_a = delta_a[~axis] / delta_a[axis]
    m_b = delta_b[~axis] / delta_b[axis]

    # intercepts
    c_a = a[0][~axis] - m_a * a[0][axis]
    c_b = b[0][~axis] - m_b * b[0][axis]

    if m_a == m_b:
        return c_a == c_b and lower(a, ~axis) <= upper(b, ~axis) and lower(b, ~axis) <= upper(a, ~axis)
    else:
        n = (c_b - c_a) / (m_a - m_b)
        return lower(a, axis) <= n <= upper(a, axis) and lower(b, axis) <= n <= upper(b, axis)

if __name__ == "__main__":
    edges = []

    for _ in range(2):
        x1, y1, x2, y2 = map(int, input().split())
        edges.append(((x1, y1), (x2, y2)))

    print(edges_intersecting(edges[0], edges[1]))
