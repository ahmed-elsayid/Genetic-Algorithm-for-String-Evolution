import random
import time

keyboard_characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")

def create_population(size, length):
    """Create a population of random strings of given length."""
    return [random.sample(keyboard_characters, length) for _ in range(size)]

def calculate_fitness(population, target):
    """Calculate the fitness of each individual in the population."""
    return [round((1 - sum(1 for char1, char2 in zip(individual, target) if char1 != char2) / len(target)) * 100)
            for individual in population]

def select_parents(population, fitness):
    """Select two parents from the population based on their fitness."""
    return random.choices(population, weights=fitness, k=2)

def crossover(parent1, parent2):
    """Perform crossover between two parents to create a child."""
    center = len(parent1) // 2
    return parent1[0:center] + parent2[center:]

def make_mutation(child, mutation_rate):
    """Introduce mutations in the child with a specified mutation rate."""
    mutation_options = ['mutate', 'no_mutate', 'no_mutate']
    if random.choices(mutation_options, weights=[mutation_rate, (1 - mutation_rate) / 2, (1 - mutation_rate) / 2], k=1)[0] == 'mutate':
        n = random.randint(0, len(child) - 1)
        child[n] = random.choice(keyboard_characters)
    return child

def create_next_generation(population, mutation_rate):
    """Create a new generation by selecting parents, performing crossover, and introducing mutations."""
    fitness = calculate_fitness(population, goal)
    new_generation = []

    for _ in range(len(population)):
        parent1, parent2 = select_parents(population, fitness)
        child = crossover(parent1, parent2)
        mutated_child = make_mutation(child, mutation_rate)
        new_generation.append(mutated_child)

    return new_generation

def check_goal_achieved(generation):
    """Check if any individual in the generation has reached the target fitness."""
    return any(fitness == 100 for fitness in generation)

def main(population_size, mutation_rate, target):
    """Evolve a population towards a target string."""
    population = create_population(population_size, len(target))
    generation_count = 0
    start_time = time.time()

    while True:
        fitness = calculate_fitness(population, target)
        if check_goal_achieved(fitness):
            break
        population = create_next_generation(population, mutation_rate)
        generation_count += 1

    end_time = time.time()
    print(f"Number of generations: {generation_count} | Time taken: {round(end_time - start_time, 3)} seconds")

goal = "hello world"
main(100, 0.1, goal)
