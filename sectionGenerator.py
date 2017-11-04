import numpy as np

def CHS(r, t, n):
    points = []
    facets = []
    holes = [(0,0)]

    for i in range(n):
        theta = i * 2 * np.pi * 1.0 / n

        x_out = r * np.cos(theta)
        y_out = r * np.sin(theta)

        x_in = (r - t) * np.cos(theta)
        y_in = (r - t) * np.sin(theta)

        points.append((x_out, y_out))
        points.append((x_in, y_in))

        if i != n - 1:
            facets.append((i * 2, i * 2 + 2))
            facets.append((i * 2 + 1, i * 2 + 3))
        else:
            facets.append((i * 2, 0))
            facets.append((i * 2 + 1, 1))

    return (points, facets, holes)

def RHS(d, b, t, r_out, n_r):
    points = []
    facets = []
    holes = [(b * 0.5, d * 0.5)]
    r_in = r_out - t

    # bottom left radius
    for i in range(n_r):
        theta = np.pi + i * 1.0 / (n_r - 1) * np.pi * 0.5

        x_out = r_out + r_out * np.cos(theta)
        y_out = r_out + r_out * np.sin(theta)
        x_in = r_out + r_in * np.cos(theta)
        y_in = r_out + r_in * np.sin(theta)

        points.append((x_out, y_out))
        points.append((x_in, y_in))

    # bottom right radius
    for i in range(n_r):
        theta = 3.0 / 2 * np.pi + i * 1.0 / (n_r - 1) * np.pi * 0.5

        x_out = b - r_out + r_out * np.cos(theta)
        y_out = r_out + r_out * np.sin(theta)
        x_in = b - r_out + r_in * np.cos(theta)
        y_in = r_out + r_in * np.sin(theta)

        points.append((x_out, y_out))
        points.append((x_in, y_in))

    # top right radius
    for i in range(n_r):
        theta = i * 1.0 / (n_r - 1) * np.pi * 0.5

        x_out = b - r_out + r_out * np.cos(theta)
        y_out = d - r_out + r_out * np.sin(theta)
        x_in = b - r_out + r_in * np.cos(theta)
        y_in = d - r_out + r_in * np.sin(theta)

        points.append((x_out, y_out))
        points.append((x_in, y_in))

    # top left radius
    for i in range(n_r):
        theta = np.pi * 0.5 + i * 1.0 / (n_r - 1) * np.pi * 0.5

        x_out = r_out + r_out * np.cos(theta)
        y_out = d - r_out + r_out * np.sin(theta)
        x_in = r_out + r_in * np.cos(theta)
        y_in = d - r_out + r_in * np.sin(theta)

        points.append((x_out, y_out))
        points.append((x_in, y_in))

    for i in range(len(points) / 2):
        if i != len(points) / 2 - 1:
            facets.append((i * 2, i * 2 + 2))
            facets.append((i * 2 + 1, i * 2 + 3))
        else:
            facets.append((i * 2, 0))
            facets.append((i * 2 + 1, 1))

    return (points, facets, holes)

def ISection(d, b, tf, tw, r, n_r):
    points = []
    facets = []
    holes = []

    points.append((0, 0))
    points.append((b, 0))
    points.append((b, tf))

    # bottom right radius
    for i in range(n_r):
        theta = 3.0 / 2 * np.pi * (1 - i * 1.0 / (n_r - 1) * 1.0 / 3)

        x = b * 0.5 + tw * 0.5 + r + r * np.cos(theta)
        y = tf + r + r * np.sin(theta)

        points.append((x, y))

    # top right radius
    for i in range(n_r):
        theta = np.pi * (1 - i * 1.0 / (n_r - 1) * 0.5)

        x = b * 0.5 + tw * 0.5 + r + r * np.cos(theta)
        y = d - tf - r + r * np.sin(theta)

        points.append((x, y))

    points.append((b, d - tf))
    points.append((b, d))
    points.append((0, d))
    points.append((0, d - tf))

    # top left radius
    for i in range(n_r):
        theta = np.pi * 0.5 * (1 - i * 1.0 / (n_r - 1))

        x = b * 0.5 - tw * 0.5 - r + r * np.cos(theta)
        y = d - tf - r + r * np.sin(theta)

        points.append((x, y))

    # bottom left radius
    for i in range(n_r):
        theta = -np.pi * i * 1.0 / (n_r - 1) * 0.5

        x = b * 0.5 - tw * 0.5 - r + r * np.cos(theta)
        y = tf + r + r * np.sin(theta)

        points.append((x, y))

    points.append((0, tf))

    for i in range(len(points)):
        if i != len(points) - 1:
            facets.append((i, i + 1))
        else:
            facets.append((len(points) - 1, 0))

    return (points, facets, holes)
