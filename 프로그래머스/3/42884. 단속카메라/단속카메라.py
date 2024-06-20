def solution(routes):
    routes.sort(key=lambda x: x[1])

    camera = routes[0][1]
    camera_count = 1

    for route in routes[1:]:
        if route[0] > camera:
            camera = route[1]
            camera_count += 1

    return camera_count