def main():
    N, M, S = map(int, input().split())
    terminal_to_partner = {}
    for _ in range(M):
        p, t = map(int, input().split())
        terminal_to_partner[t] = p

    partner_clients = {}
    for i in range(1, N + 1):
        partner_clients[i] = {}

    for _ in range(S):
        c, t = map(int, input().split())
        if t in terminal_to_partner:
            p = terminal_to_partner[t]
            partner_clients[p][c] = partner_clients[p].get(c, 0) + 1

    for i in range(1, N + 1):
        clients = partner_clients[i]
        if not clients:
            print(f"{i} -1")
        else:
            max_count = max(clients.values())
            best = min(c for c, cnt in clients.items() if cnt == max_count)
            print(f"{i} {best}")

if __name__ == "__main__":
    main()