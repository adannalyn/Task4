from collections import defaultdict

def group_by_category(transactions):
    grouped = defaultdict(list)
    for t in transactions:
        grouped[t.category].append(t)
    return grouped

def calculate_totals(transactions):
    totals = {}
    for t in transactions:
        if t.category in totals:
            totals[t.category] += t.amount
        else:
            totals[t.category] = t.amount
    return totals
