import random


# -------------------------
# GENE
# -------------------------
class Gene:
    def __init__(self, value=None):
        self.value = value if value is not None else random.randint(0, 1)

    def mutate(self):
        # flip 0 ↔ 1
        self.value = 1 - self.value


# -------------------------
# CHROMOSOME
# -------------------------
class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]

    def mutate(self):
        # each gene has 50% chance to flip
        for gene in self.genes:
            if random.random() < 0.5:
                gene.mutate()

    def is_all_ones(self):
        return all(gene.value == 1 for gene in self.genes)


# -------------------------
# DNA
# -------------------------
class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]

    def mutate(self):
        # each chromosome mutates with probability 50%
        for chromo in self.chromosomes:
            if random.random() < 0.5:
                chromo.mutate()

    def is_perfect(self):
        return all(chromo.is_all_ones() for chromo in self.chromosomes)


# -------------------------
# ORGANISM
# -------------------------
class Organism:
    def __init__(self, environment=0.1):
        self.dna = DNA()
        self.environment = environment

    def mutate(self):
        # environment = probability of mutation
        if random.random() < self.environment:
            self.dna.mutate()


# -------------------------
# SIMULATION
# -------------------------
def simulate(population_size=20, environment=0.1):
    organisms = [Organism(environment) for _ in range(population_size)]
    generations = 0

    while True:
        generations += 1

        for org in organisms:
            org.mutate()

            if org.dna.is_perfect():
                print("🎉 Perfect DNA found!")
                print(f"Generations: {generations}")
                return generations


# Run simulation
simulate()