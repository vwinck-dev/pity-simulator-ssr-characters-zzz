import random

def simulate_zzz_pulls(simulations, copies_goal, base_rate, base_rate_a, soft_pity_start, hard_pity):
    total_pulls_list = []
    total_a_units = []
    total_banner_a = []
    total_banner_b = []
    total_generic_a = []

    for i in range(simulations):
        if i % (simulations // 10) == 0:
            print(f"Simulation {i}/{simulations}...")

        pulls = 0
        banner_copies = 0
        pity_counter = 0
        guaranteed_banner = False

        a_pull_counter = 0
        a_units = 0
        banner_a = 0
        banner_b = 0
        generic_a = 0

        while banner_copies < copies_goal:
            pulls += 1
            pity_counter += 1
            a_pull_counter += 1

            if random.random() < base_rate_a:
                a_units += 1
                a_pull_counter = 0
                if random.random() < 0.5:
                    if random.random() < 0.5:
                        banner_a += 1
                    else:
                        banner_b += 1
                else:
                    generic_a += 1
            elif a_pull_counter == 10:
                a_units += 1
                a_pull_counter = 0
                if random.random() < 0.5:
                    if random.random() < 0.5:
                        banner_a += 1
                    else:
                        banner_b += 1
                else:
                    generic_a += 1

            if pity_counter == hard_pity:
                pity_counter = 0
                if guaranteed_banner or random.random() < 0.5:
                    banner_copies += 1
                    guaranteed_banner = False
                else:
                    guaranteed_banner = True
                continue

            if pity_counter >= soft_pity_start:
                soft_chance = base_rate + ((pity_counter - soft_pity_start + 1) * ((1.0 - base_rate) / (hard_pity - soft_pity_start + 1)))
            else:
                soft_chance = base_rate

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

    avg_pulls = sum(total_pulls_list) / simulations
    avg_a = sum(total_a_units) / simulations
    avg_banner_a = sum(total_banner_a) / simulations
    avg_banner_b = sum(total_banner_b) / simulations
    avg_generic_a = sum(total_generic_a) / simulations
    
    print(f"[ZZZ] Average Pulls: {int(round(avg_pulls))}  |  Average Policrome: {int(round(avg_pulls * 160))}")
    print(f"Average A-type units: {int(round(avg_a))}")
    print(f"  ↳ Banner A: {int(round(avg_banner_a))}")
    print(f"  ↳ Banner B: {int(round(avg_banner_b))}")
    print(f"  ↳ Off-Banner: {int(round(avg_generic_a))}")

if __name__ == "__main__":
    def get_input(prompt, cast_func, default):
        val = input(f"{prompt} (ENTER = {default}): ").strip()
        return cast_func(val) if val else default

    print("ZZZ Gacha Simulator (with automatic defaults!)")
    simulations = get_input("Number of simulations", int, 10000)
    base_rate = get_input("Base SSR rate (e.g., 0.006)", float, 0.006)
    base_rate_a = get_input("Base A-type character rate (e.g., 0.072)", float, 0.072)
    soft_pity_start = get_input("Soft pity starts at which pull? (e.g., 75)", int, 75)
    hard_pity = get_input("Hard pity at which pull? (e.g., 90)", int, 90)
    copies_goal = get_input("How many banner copies? (e.g., 6)", int, 6)

    simulate_zzz_pulls(simulations, copies_goal, base_rate, base_rate_a, soft_pity_start, hard_pity)
