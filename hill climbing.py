import random
import string

def generate_random_solution(ans):
    l = len(ans)
    return [random.choice(string.printable) for _ in range(l)]

def mutate(soln):
    ind = random.randint(0, len(soln) - 1)
    soln[ind] = random.choice(string.printable)
    return soln

def evaluate(solution, answer):
    diff = 0
    for i in range(len(solution)):
        diff += abs(ord(answer[i]) - ord(solution[i]))
    return diff

def simplehillclimbing():
    answer = input("Enter target string: ")
    best = generate_random_solution(answer)
    best_score = evaluate(best, answer)
    iterations = 0
    max_iterations = 100000

    while best_score != 0 and iterations < max_iterations:
        print("Score:", best_score, "String:", ''.join(best))
        new_soln = mutate(best.copy())
        score = evaluate(new_soln, answer)

        if score < best_score:
            best = new_soln
            best_score = score

        iterations += 1

    if best_score == 0:
        print("\nTarget Found:", ''.join(best))
    else:
        print("\nStopped after max iterations.")
        print("Best found:", ''.join(best))

simplehillclimbing()