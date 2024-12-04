from collections import defaultdict
import heapq

def min_orbs_needed(recipes, target_potion):
    graph = defaultdict(list)
    for recipe in recipes:
        potion, ingredients = recipe.split('=')
        graph[potion].append(ingredients.split('+'))
    
    orb_cost = {}

    def calculate_orbs(potion):
        if potion not in graph:
            return 0
        if potion in orb_cost:
            return orb_cost[potion]
        min_cost = float('inf')
        for ingredients in graph[potion]:
            cost = len(ingredients) - 1
            for ingredient in ingredients:
                cost += calculate_orbs(ingredient)
            min_cost = min(min_cost, cost)
        orb_cost[potion] = min_cost
        return min_cost

    return calculate_orbs(target_potion)

n = int(input())
recipes = [input().strip() for _ in range(n)]
target_potion = input().strip()
print(min_orbs_needed(recipes, target_potion))
