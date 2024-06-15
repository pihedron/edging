# Pihedron Edging Algorithm

Checking if a pair of polygons are colliding requires checking if at least 1 pair of edges are colliding (edging). This is the only reliable way to handle **concave** polygon collisions.

> [!NOTE]
> The separating axis theorem only works for convex polygons. This algorithm can be used for concave polygons defined by a set of edges.

## Explanation

Edges are line segments that can be defined by 2 distinct points. This algorithm only deals with 2D points for simplicity.

The idea is to find the point at which both line segments intersect, but there is no easy mathematical formula for this that accounts for all edge cases. There is however a formula for finding the intersection of 2 lines using linear algebra.

The process for finding whether the line segments are intersecting is as follows:

1. Treat the line segments as lines.
2. Calculate the gradients.
3. Calculate the axis intercepts.
4. Skip the next step if the edges have the same gradient (parallel or co-linear).
5. Solve for the co-ordinates of the point of intersection.
6. Check if the point rests on both line segments.

The only issue here is dealing with undefined (vertical) gradients. The axes can be swapped if this occurs, but what if 1 line is vertical and the other is horizontal?

This is why we need the `hv_intersecting` function to deal with this edge case separately. It checks whether the line of `a` intersects with the line segment `b` and vice versa.

When both gradients are equal, the line segments are only intersecting if they both have the same axis intercept and their perpendicular shadows intersect.

Knowing either co-ordinate of the point of intersection is enough to check whether the point rests on both line segments because we already know that the point rests on both lines. If the lines have different gradients and the $x$ value of the point of intersection is within the $x$ interval of both line segments, then the line segments are intersecting.
