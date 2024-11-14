from typing import List

class Solution:
    def findRestaurant(list1, list2):
        index_map = {restaurant: index for index, restaurant in enumerate(list1)}
        min_sum = float('inf')
        result = []

        for index2, restaurant in enumerate(list2):
            if restaurant in index_map:
                index_sum = index_map[restaurant] + index2
                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [restaurant]
                elif index_sum == min_sum:
                    result.append(restaurant)

        return result

# Example usage
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(findRestaurant(list1, list2))  # Output: ["Shogun"]

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]
print(findRestaurant(list1, list2))  # Output: ["Shogun"]

list1 = ["happy", "sad", "good"]
list2 = ["sad", "happy", "good"]
print(findRestaurant(list1, list2))  # Output: ["sad", "happy"]
