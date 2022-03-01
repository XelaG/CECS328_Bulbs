import collections
from random import randint

def find_m_min(bulbs):
    m_min = bulbs[0][0]
    if (m_min < 0):
        m_min = m_min * -1
    for i in bulbs:
        for j in i:
            if (j < 0):
                j = j * -1
            if j < m_min:
                m_min = j
    return m_min

def find_m_max(bulbs):
    m_max = bulbs[0][0]
    if (m_max < 0):
        m_max = m_max * -1
    for i in bulbs:
        for j in i:
            if (j < 0):
                j = j * -1
            if j > m_max:
                m_max = j
    return m_max

def create_sets(bulbs, min, max):
    sets = {}
    for i in range(min, max + 1):
        sets[i] = []
    for i in range(len(bulbs)):
        for j in bulbs[i]:
            idx = j
            if (idx < 0):
                idx = idx * -1
            if (j > 0):
                sets[idx].append({
                    'is_red': False,
                    'row_idx': i,
                    'is_row_lit': False
                })
            else:
                sets[idx].append({
                    'is_red': True,
                    'row_idx': i,
                    'is_row_lit': False
                })
    od = collections.OrderedDict(sorted(sets.items()))           
    return od

def print_sets(sets):
    for k, v in sets.items():
        print(k)
        for item in v:
            print(item)

def lit_row(sets, row):
    for k, v in sets.items():
        for item in v:
            if (item['row_idx'] == row):
                item['is_row_lit'] = True
    return sets

def is_any_row_not_lit(sets): 
    for k, v in sets.items():
        for item in v:
            if not item['is_row_lit']: return True
    return False

def lit_them_up(sets):
    result = []
    for k, v in sets.items():
        # print("--------------------------------------")
        # print("Set:", v)
        weight = 0
        for item in v:
            if not item['is_row_lit'] and item['is_red']: weight -= 1
            if not item['is_row_lit'] and not item['is_red']: weight += 1
        # print("Weigth = ", weight)
        if (weight < 0):
            result.append(False)
            for item in v:
                if item['is_red'] and not item['is_row_lit']:
                    sets = lit_row(sets, item['row_idx'])
        else:
            result.append(True)
            for item in v:
                if not item['is_red'] and not item['is_row_lit']:
                    sets = lit_row(sets, item['row_idx'])
    # if is_any_row_not_lit(sets):
        # TODO: Keep track of which wire lit up which row so if a row is not lit we can try to do the inverse and see if it changes (maybe introduce recursion)
    print_sets(sets)
    print("Are any row not lit ?", is_any_row_not_lit(sets))
    print("Result is: ", result)
    print("Result Length is: ", len(result))
    return result

def solve(bulbs):
    m_min = 1
    m_max = find_m_max(bulbs)
    # print("m_min = ", m_min)
    # print("m_max = ", m_max)
    n = len(bulbs)
    sets = create_sets(bulbs, m_min, m_max)
    # print_sets(sets)

    return lit_them_up(sets)

def generate_bulb(max, n):
    bulbs = []
    for i in range(1, n + 1):
        bulbs.append([randint(-max, max), randint(-max, max),randint(-max, max)])
    has_one = False
    has_max = False
    for i in range(len(bulbs)):
        for j in range(len(bulbs[i])):
            if (bulbs[i][j] == 1): 
                has_one = True
            if (bulbs[i][j] == max): 
                has_max = True
            if (bulbs[i][j] == 0):
                while (bulbs[i][j] == 0):
                    bulbs[i][j] = randint(-max, max)
    if not has_one:
        print("Don't have a one")
        bulbs[0][0] = 1
    if not has_max:
        print("Don't have a max")
        bulbs[0][1] = max
    return bulbs

def main():
    bulbs = generate_bulb(150, 100)
    # NEXT LINE MAKE PROGRAM FAIL
    # bulbs = [[137, -127, -102], [118, -60, 103], [-104, -29, 4], [-80, 104, 147], [38, -38, -76], [16, 104, -56], [31, -78, -11], [75, 119, -57], [-12, -40, -21], [34, -7, 16], [-47, -125, 37], [-133, 94, -27], [78, 141, -40], [23, -114, 99], [66, 34, -41], [6, 106, -109], [-80, 50, -78], [-82, 5, -61], [141, -93, -64], [136, 62, 59], [134, 15, -96], [-53, -105, -62], [-144, -95, 143], [118, 42, 1], [39, 42, -82], [121, -87, 34], [53, 70, -105], [-82, 125, -77], [-69, -40, 8], [-117, 24, -144], [12, -119, 53], [-109, 137, 34], [-52, -59, -25], [62, -108, -47], [102, -36, -120], [-53, 70, -45], [-28, 47, -22], [75, 127, 96], [-149, -16, 138], [-105, -29, 111], [3, -67, 96], [58, 13, 30], [-56, 113, 139], [-85, -18, -87], [40, 7, -54], [-140, -52, -134], [105, 137, 21], [133, 101, -89], [5, 16, 76], [-60, 67, 150], [83, -125, 143], [-120, -70, -139], [-86, -21, -102], [-3, 135, 9], [83, -32, -95], [-137, -121, 15], [-145, 57, 45], [-12, -66, -37], [-144, -23, -14], [-28, -137, -106], [-50, 17, -39], [-54, -11, 55], [144, 14, 100], [59, 70, 82], [144, -70, -99], [7, -5, 12], [99, -65, 89], [85, 86, 62], [100, 31, 146], [-121, -128, 136], [-69, 122, 26], [-30, -125, 12], [-126, -108, -139], [-48, 28, -37], [-73, -101, -67], [-113, -99, -138], [84, -2, -33], [146, 149, -139], [139, 142, -51], [28, -5, 143], [-54, 123, -16], [-133, -145, 100], [-119, 42, 103], [103, 73, -66], [-73, 145, -123], [33, 62, -105], [-66, 24, -54], [-91, -12, -75], [84, -41, -81], [77, 51, 117], [-113, 81, -132], [-2, -47, 74], [46, 11, 104], [40, 50, 119], [-94, -142, -44], [-82, 141, -110], [-111, -116, -82], [-140, 34, -115], [109, -43, 26], [-149, 83, 25]]  
    # print("row 35 = ", bulbs[35])
    print(bulbs)
    # bulbs = [[1, -2, 2], [1, 1, 1], [-5, -2, 1], [4, -3, 3]]
    # bulbs = [[-4, -4, -1], [13, -9, -14], [4, -7, -2], [-2, 6, 3], [-6, -8, 11], [-4, -3 -6], [7, 11, -10], [4, -7, 6], [5, 6, 4], [10, 14, -9]]
    solve(bulbs)

main()