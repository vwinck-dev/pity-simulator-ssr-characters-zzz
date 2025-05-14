import random

def simulate_zzz_pulls_for_6_copies(simulations=99999):
    total_pulls_list = []

    for _ in range(simulations):
        pulls = 0
        banner_copies = 0
        pity_counter = 0
        guaranteed_banner = False

        while banner_copies < 6:
            pulls += 1
            pity_counter += 1

            base_chance = 0.006

            # Hard pity
            if pity_counter == 90:
                pity_counter = 0
                if guaranteed_banner or random.random() < 0.5:
                    banner_copies += 1
                    guaranteed_banner = False
                else:
                    guaranteed_banner = True
                continue

            # Soft pity starts to scale from 75 to 90
            if pity_counter >= 75:
                soft_chance = base_chance + ((pity_counter - 74) * ((1.0 - base_chance) / 16))
            else:
                soft_chance = base_chance

            if random.random() < soft_chance:
                pity_counter = 0
                if guaranteed_banner or random.random() < 0.5:
                    banner_copies += 1
                    guaranteed_banner = False
                else:
                    guaranteed_banner = True

        total_pulls_list.append(pulls)

    avg_pulls = sum(total_pulls_list) / simulations
    print(f"[ZZZ] Pulls: {int(avg_pulls)}, Policrome: {int(avg_pulls * 160)}")

simulate_zzz_pulls_for_6_copies()
