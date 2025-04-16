import numpy as np


class DummyMatch:
    def __init__(self, queryIdx, trainIdx, distance):
        self.queryIdx = queryIdx
        self.trainIdx = trainIdx
        self.distance = distance


def match_key_points_numpy(des1: np.ndarray, des2: np.ndarray) -> list:
    diff = des1[:, None, :] - des2[None, :, :]
    dists = np.sqrt(np.sum(diff ** 2, axis=2))

    best_idx1 = np.argmin(dists, axis=1)
    best_idx2 = np.argmin(dists, axis=0)

    matches = []

    for i in range(len(des1)):
        j = best_idx1[i]
        if best_idx2[j] == i:
            distance = dists[i, j]
            matches.append(DummyMatch(i, j, distance))
    
    matches.sort(key=lambda m: m.distance)
    return matches
