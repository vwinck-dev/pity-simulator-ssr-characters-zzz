import random

def simulate_pulls_for_6_copies(simulations=99999):
    total_pulls_list = []

    for _ in range(simulations):
        pulls = 0
        banner_copies = 0
        pity_counter = 0
        guaranteed_banner = False

        while banner_copies < 6:
            pulls += 1
            pity_counter += 1

            # Hard pity to 90 pulls
            if pity_counter == 90:
                pity_counter = 0
                if guaranteed_banner or random.random() < 0.5:
                    banner_copies += 1
                    guaranteed_banner = False
                else:
                    guaranteed_banner = True
                continue

            # Soft pity before 75
            if pity_counter >= 75:
                chance = (pity_counter - 74) / 16  # escala até 100% no 90
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

simulate_pulls_for_6_copies()
