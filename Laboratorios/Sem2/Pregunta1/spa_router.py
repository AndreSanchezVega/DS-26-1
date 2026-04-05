def spa_router(routes, transitions):
    results = []
    for transition in transitions:
        found = False
        transition_parts = transition.strip().split('/')
        
        for path, content in routes:
            path_parts = path.strip().split('/')
            
            if len(path_parts) != len(transition_parts):
                continue
            
            match = True
            params = {}
            
            for p_part, t_part in zip(path_parts, transition_parts):
                if p_part.startswith(':'):
                    params[p_part[1:]] = t_part
                elif p_part != t_part:
                    match = False
                    break
            
            if match:
                result = content
                for param_name, param_value in params.items():
                    result = result.replace('{' + param_name + '}', param_value)
                results.append(result)
                found = True
                break
        
        if not found:
            results.append("404 Not Found")
    
    return results


def main():
    N = int(input())
    routes = []
    for _ in range(N):
        line = input().split()
        path = line[0]
        content = ' '.join(line[1:])
        routes.append((path, content))
    
    M = int(input())
    transitions = []
    for _ in range(M):
        transitions.append(input().strip())
    
    results = spa_router(routes, transitions)
    for r in results:
        print(r)


if __name__ == "__main__":
    main()