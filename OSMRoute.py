import json
import os


def hack_route(P1=[46.740733, -19.170705], P2=[47.555450, -18.915429]):
    """
    executes a curl command to retrieve an osm (car) route
    stores the result in an output.json file
    parses it to get the locations

    params: P1: first point of the route
    params: P2: second point of the route

    returns:
        xlon, ylat: list of longitudes and latitudes

    """

    cmd = (
        """curl "https://router.project-osrm.org/route/v1/driving/%s,%s;%s,%s?steps=true" > output.json """
        % (P1[0], P1[1], P2[0], P2[1])
    )

    os.system(cmd)

    f = open("output.json")
    lines = f.readlines()
    i = 0
    xlon = []
    ylat = []
    for line in lines:
        data = line.split(",")
        for i in range(len(data)):
            if "location" in data[i]:
                # print(data[i], data[i + 1])
                lon = float(data[i].split("[")[1])
                lat = float(data[i + 1].split("]")[0])
                if lon not in xlon and lat not in ylat:
                    xlon.append(lon)
                    ylat.append(lat)

    return xlon, ylat


if __name__ == "__main__":
    x, y = hack_route()
    print(x, y)
