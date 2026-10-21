class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        people = zip(heights, names)
        sorted_people = sorted(people, reverse=True)
        return [name for _, name in sorted_people]
