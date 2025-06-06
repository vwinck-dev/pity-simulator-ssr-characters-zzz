# Pity Simulator ZZZ

A simulator to calculate the average number of pulls required to obtain 6 copies of a S character in gacha systems like **Zenless Zone Zero (ZZZ)**. This project includes two independent simulators:

- A **generic** pity system (soft + hard pity, with 50/50 rules).
- An **official-like** version based on ZZZ's public/probable pull rates.

Made for data nerds, gacha addicts, and curious developers.

---

## 📂 Files

### `pity_simulator_zzz.py`

Simulates the actual behavior of **Zenless Zone Zero's** character banners:

- 0.6% base chance to get a 5★.
- Soft pity ramps up starting from 75 pulls to 100% at 90.
- 50/50 rule enforced (with banner guarantee on loss).
- Targets 6 total copies of the featured unit.

---

## 🚀 Usage

You need Python 3 installed.

```bash
# Clone this repo
git clone https://github.com/vwinck-dev/pity-simulator-ssr-characters-zzz.git
cd pity-simulator-zzz

# Run the simulation
python pity_simulator_generic.py
python pity_simulator_zzz.py
