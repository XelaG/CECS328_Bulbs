import collections

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
    for i in range(min, max):
        sets[i] = []
    for i in range(len(bulbs)):
        for j in bulbs[i]:
            idx = j
            if (idx < 0):
                idx = idx * -1
            if idx in sets:
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
            else:
                if (j > 0):
                    sets[idx] = [{
                        'is_red': False,
                        'row_idx': i,
                        'is_row_lit': False
                    }]
                else:
                    sets[idx] = [{
                        'is_red': True,
                        'row_idx': i,
                        'is_row_lit': False
                    }]
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
                if item['is_red']:
                    sets = lit_row(sets, item['row_idx'])
        else:
            result.append(True)
            for item in v:
                if not item['is_red']:
                    sets = lit_row(sets, item['row_idx'])
    # print_sets(sets)
    # print(result)
    return result

def solve(bulbs):
    m_min = find_m_min(bulbs)
    m_max = find_m_max(bulbs)
    n = len(bulbs)
    sets = create_sets(bulbs, m_min, m_max)
    # print_sets(sets)

    return lit_them_up(sets)

# def main():
#     bulbs = [[-4, -4, -1], [13, -9, -14], [4, -7, -2], [-2, 6, 3], [-6, -8, 11], [-4, -3 -6], [7, 11, -10], [4, -7, 6], [5, 6, 4], [10, 14, -9]]
#     solve(bulbs)

# main()