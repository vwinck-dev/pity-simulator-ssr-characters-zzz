import random

def simulate_pulls_for_6_copies(simulations, soft_pity_start, hard_pity, copies_goal):
    total_pulls_list = []

    for _ in range(simulations):
        pulls = 0
        banner_copies = 0
        pity_counter = 0
        guaranteed_banner = False

        while banner_copies < copies_goal:
            pulls += 1
            pity_counter += 1

            # Hard pity
            if pity_counter == hard_pity:
                pity_counter = 0
                if guaranteed_banner or random.random() < 0.5:
                    banner_copies += 1
                    guaranteed_banner = False
                else:
                    guaranteed_banner = True
                continue

            # Soft pity
            if pity_counter >= soft_pity_start:
                chance = (pity_counter - soft_pity_start + 1) / (hard_pity - soft_pity_start + 1)
                if random.random() < chance:
                    pity_counter = 0
                    if guaranteed_banner or random.random() < 0.5:
                        banner_copies += 1
                        guaranteed_banner = False
                    else:
                        guaranteed_banner = True
                    continue

        total_pulls_list.append(pulls)

    avg_pulls = sum(total_pulls_list) / simulations
    print(f"Pulls: {int(avg_pulls)}, Policrome: {int(avg_pulls * 160)}")

if __name__ == "__main__":
    simulations = int(input("Number of simulations (e.g. 99999): "))
    soft_pity_start = int(input("Soft pity starts at pull #: "))
    hard_pity = int(input("Hard pity at pull #: "))
    copies_goal = int(input("How many copies to simulate for (e.g. 6): "))
    simulate_pulls_for_6_copies(simulations, soft_pity_start, hard_pity, copies_goal)
