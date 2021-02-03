class Solution:
    def nextEight(self, x, y):
        return [
            (x+1, y+2),
            (x-1, y+2),
            (x+1, y-2),
            (x-1, y-2),
            (x+2, y+1),
            (x+2, y-1),
            (x-2, y+1),
            (x-2, y-1)
        ]

    def minKnightMoves(self, x: int, y: int) -> int:
        def recurse(p, q, x, y, path, travelled, currentMin):
            if p == x and q == y:
                currentMin[0] = min(currentMin[0], path)
            elif abs(p) + abs(q) > 300:
                return
            else:
                for _, (m, n) in enumerate(self.nextEight(p, q)):
                    if f'{m}|{n}' not in travelled and path < currentMin[0]:
                        travelled[f'{m}|{n}'] = True
                        recurse(m, n, x, y, path+1, travelled, currentMin)

        from sys import maxsize
        travelled = {'0|0': True}
        currentMin = [maxsize]
        recurse(0, 0, x, y, 0, travelled, currentMin)

        return currentMin[0]


s = Solution()
# print(s.minKnightMoves(1, 2))
# print(s.minKnightMoves(2, 1))
print(s.nextEight(0, 0))
