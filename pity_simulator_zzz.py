import random

def simulate_zzz_pulls(simulations, copies_goal, base_rate, soft_pity_start, hard_pity):
    total_pulls_list = []
    total_a_units = []
    total_banner_a = []
    total_banner_b = []
    total_generic_a = []

    for _ in range(simulations):
        pulls = 0
        banner_copies = 0
        pity_counter = 0
        guaranteed_banner = False

        a_pull_counter = 0  # counts how many pulls since last A-type unit
        a_units = 0
        banner_a = 0
        banner_b = 0
        generic_a = 0

        while banner_copies < copies_goal:
            pulls += 1
            pity_counter += 1
            a_pull_counter += 1

            # --- Handle A-type unit every 10 pulls ---
            if random.random() < 0.072:
                # Got A-unit early
                a_units += 1
                a_pull_counter = 0
                if random.random() < 0.5:
                    # From banner
                    if random.random() < 0.5:
                        banner_a += 1
                    else:
                        banner_b += 1
                else:
                    # Generic off-banner A
                    generic_a += 1

            elif a_pull_counter == 10:
                # Guaranteed A-unit
                a_units += 1
                a_pull_counter = 0
                if random.random() < 0.5:
                    # From banner
                    if random.random() < 0.5:
                        banner_a += 1
                    else:
                        banner_b += 1
                else:
                    # Generic off-banner A
                    generic_a += 1


            # --- Handle SSR pulls (banner logic) ---
            # Hard pity
            if pity_counter == hard_pity:
                pity_counter = 0
                if guaranteed_banner or random.random() < 0.5:
                    # Got banner SSR
                    banner_copies += 1
                    guaranteed_banner = False
                else:
                    # Lost 50/50
                    guaranteed_banner = True
                continue

            # Soft pity scaling
            if pity_counter >= soft_pity_start:
                
                # Calculate soft pity chance

                # Soft pity chance increases linearly from base_rate to 1.0
                soft_chance = base_rate + ((pity_counter - soft_pity_start + 1) * ((1.0 - base_rate) / (hard_pity - soft_pity_start + 1)))
            else:
                soft_chance = base_rate

            # Attempt SSR pull
            if random.random() < soft_chance:
                pity_counter = 0
                if guaranteed_banner or random.random() < 0.5:
                    banner_copies += 1
                    guaranteed_banner = False
                else:
                    guaranteed_banner = True

        total_pulls_list.append(pulls)
        total_a_units.append(a_units)
        total_banner_a.append(banner_a)
        total_banner_b.append(banner_b)
        total_generic_a.append(a_units - banner_a - banner_b)

    # Final stats
    avg_pulls = sum(total_pulls_list) / simulations
    avg_a = sum(total_a_units) / simulations
    avg_banner_a = sum(total_banner_a) / simulations
    avg_banner_b = sum(total_banner_b) / simulations
    avg_generic_a = sum(total_generic_a) / simulations

    print(f"[ZZZ] Pulls: {int(avg_pulls)}, Policrome: {int(avg_pulls * 160)}")
    print(f"Average A-type characters: {int(avg_a)}")
    print(f"  ↳ From Banner: A = {int(avg_banner_a)}, B = {int(avg_banner_b)}")
    print(f"  ↳ Off-Banner Generics: {int(avg_generic_a)}")

if __name__ == "__main__":
    # User input
    simulations = int(input("Number of simulations (e.g. 99999): "))
    base_rate = float(input("Base SSR chance (e.g. 0.006 for 0.6%): "))
    soft_pity_start = int(input("Soft pity starts at pull #: "))
    hard_pity = int(input("Hard pity at pull #: "))
    copies_goal = int(input("How many banner copies to simulate for (e.g. 6): "))

    simulate_zzz_pulls(simulations, copies_goal, base_rate, soft_pity_start, hard_pity)
