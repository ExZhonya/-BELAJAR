class SearchAlgorithms:
	@staticmethod
	def hash_lookup(dictionary: dict, key):
		return dictionary.get(key, None)

class SortAlgorithm:
	@staticmethod
	def merge_sort(arr: list[tuple[str, str]]) -> list[tuple[str, str]]:
		if len(arr) <= 1:
			return arr

		mid = len(arr) // 2
		left = SortAlgorithm.merge_sort(arr[:mid])
		right = SortAlgorithm.merge_sort(arr[mid:])
		return SortAlgorithm._merge(left, right)

	@staticmethod
	def _merge(left: list, right: list) -> list:
		result = []
		i = j = 0

		while i < len(left) and j < len(right):
			if left[i][0].lower() <= right[j][0].lower():
				result.append(left[i])
				i += 1
			else:
				result.append(right[j])
				j += 1

		result.extend(left[i:])
		result.extend(right[j:])
		return result