import heapq

def solution(tickets):
    answer = []
    
    mem = {}
    for t in tickets:
        mem[t[0]] = -1
        mem[t[1]] = -1
    
    def dfs(cur, tickets):
        
        if len(tickets) == 0:
            heapq.heappush(answer, cur[:])
        
        for i in range(len(tickets)):
            if (cur and tickets[i][0] == cur[-1]) or (not cur and tickets[i][0] == "ICN"):
                if cur and tickets[i][0] == cur[-1]:
                    cur.append(tickets[i][1])
                elif not cur and tickets[i][0] == "ICN":
                    cur.append("ICN")
                    cur.append(tickets[i][1])
                
                c_tickets = tickets[:]
                c_tickets.pop(i)
                dfs(cur, c_tickets)
                     
                if len(cur) > 2:
                    cur.pop()
                else:
                    cur.pop()
                    cur.pop()
                
                
    dfs([], tickets)
    return heapq.heappop(answer)