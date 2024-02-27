class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        mem = defaultdict(list)
        costs = {}

        #그래프를 딕셔너리로 저장
        for time in times:
            mem[time[0]].append((time[2], time[1]))

        #우선 순위 큐로 사용할 배열
        heap = []

        heapq.heappush(heap, (0, k))

        while heap:
            cur_cost, cur_node = heapq.heappop(heap)
            if cur_node not in costs:
                costs[cur_node]  = cur_cost
                for next_cost, next_node in mem[cur_node]:
                    heapq.heappush(heap, (cur_cost+next_cost, next_node))

        for i in range(1, n+1):
            if i not in costs:
                return -1

        return max(costs.values())


