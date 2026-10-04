import time
import random
import json

SAVE_FILE = "filya_save.json"

money = 0
pickaxe = 1
total_diamonds = 0
record = 0
auto = False
helpers = 0
depth = 1
tariff = 0
speed = 1
prestige = 0
total_mined = 0
bosses_defeated = []
location = "Common Mine"
potion_effect = None
potion_turns = 0
stars = 0

pets = {
    "Kitten Filya":   {"price": 100000,    "bonus": 0.10, "bought": False, "mines": 1},
    "Dog Sharik":     {"price": 500000,    "bonus": 0.20, "bought": False, "mines": 2},
    "Parrot Kesha":   {"price": 2000000,   "bonus": 0.30, "bought": False, "mines": 3},
    "Hamster Semyon": {"price": 10000000,  "bonus": 0.50, "bought": False, "mines": 5},
    "Dragon Filya":   {"price": 100000000, "bonus": 1.00, "bought": False, "mines": 10},
}

secret_pets = {
    "Cosmo Cat": {"price": 10000000000,   "bonus": 3.00,  "bought": False, "mines": 50,  "description": "+300% and 50 digs"},
    "Filya God": {"price": 1000000000000, "bonus": 10.00, "bought": False, "mines": 200, "description": "+1000% and 200 digs"},
}

golden_vein = False
shop_discount = False

weapons = {
    "Wooden Sword":  {"price": 0,          "damage": 1000,     "bought": True},
    "Stone Sword":   {"price": 50000,      "damage": 5000,     "bought": False},
    "Iron Sword":    {"price": 500000,     "damage": 20000,    "bought": False},
    "Golden Sword":  {"price": 5000000,    "damage": 100000,   "bought": False},
    "Diamond Sword": {"price": 50000000,   "damage": 500000,   "bought": False},
    "Mithril Sword": {"price": 500000000,  "damage": 2000000,  "bought": False},
    "Filya Sword":   {"price": 5000000000, "damage": 10000000, "bought": False},
}

damage_multipliers = {
    "Ring of Power":  {"price": 1000000000,   "multiplier": 2,   "bought": False},
    "Filya Amulet":   {"price": 5000000000,   "multiplier": 5,   "bought": False},
    "Miner's Crown":  {"price": 20000000000,  "multiplier": 10,  "bought": False},
    "Titan's Ring":   {"price": 100000000000, "multiplier": 25,  "bought": False},
    "Filya's Wreath": {"price": 500000000000, "multiplier": 100, "bought": False},
}

potions = {
    "Luck Potion":     {"price": 100000,   "effect": "x2",  "turns": 10},
    "Strength Potion": {"price": 500000,   "effect": "x5",  "turns": 10},
    "Wealth Potion":   {"price": 2000000,  "effect": "x10", "turns": 10},
    "Filya Potion":    {"price": 10000000, "effect": "x25", "turns": 10},
}

locations = {
    "Common Mine":   {"price": 0,           "bonus": 0.0, "unlocked": True},
    "Ice Mine":      {"price": 100000000,   "bonus": 0.5, "unlocked": False},
    "Fire Cave":     {"price": 1000000000,  "bonus": 1.0, "unlocked": False},
    "Crystal Abyss": {"price": 10000000000, "bonus": 2.0, "unlocked": False},
}

bosses = {
    5:  {"name": "Dwarf Guard",  "hp": 10000,     "reward": 500000,      "diamonds": 50},
    10: {"name": "Stone Golem",  "hp": 100000,    "reward": 5000000,     "diamonds": 200},
    15: {"name": "Depth Dragon", "hp": 1000000,   "reward": 50000000,    "diamonds": 1000},
    20: {"name": "Ice Titan",    "hp": 5000000,   "reward": 200000000,   "diamonds": 3000},
    25: {"name": "Fire Demon",   "hp": 20000000,  "reward": 1000000000,  "diamonds": 10000},
    30: {"name": "Filya Boss",   "hp": 100000000, "reward": 10000000000, "diamonds": 50000},
}

diamond_shop = {
    1:  {"diamonds": 10,     "price": 100000},
    2:  {"diamonds": 50,     "price": 400000},
    3:  {"diamonds": 100,    "price": 700000},
    4:  {"diamonds": 500,    "price": 3000000},
    5:  {"diamonds": 1000,   "price": 5000000},
    6:  {"diamonds": 5000,   "price": 20000000},
    7:  {"diamonds": 10000,  "price": 35000000},
    8:  {"diamonds": 50000,  "price": 150000000},
    9:  {"diamonds": 100000, "price": 250000000},
    10: {"diamonds": 1000000,"price": 2000000000},
}

ores = {
    "stone":         {"price": 10,      "chance": 44.9},
    "iron":          {"price": 50,      "chance": 25},
    "silver":        {"price": 100,     "chance": 12},
    "gold":          {"price": 150,     "chance": 8},
    "emerald":       {"price": 500,     "chance": 4},
    "diamond":       {"price": 500,     "chance": 3},
    "titanium":      {"price": 1500,    "chance": 1.5},
    "quartz":        {"price": 5000,    "chance": 1},
    "uranium":       {"price": 20000,   "chance": 0.5},
    "platinum":      {"price": 10000,   "chance": 0.3},
    "mithril":       {"price": 50000,   "chance": 0.15},
    "Filya Ore":     {"price": 100000,  "chance": 0.05},
    "Adamantite":    {"price": 500000,  "chance": 0.03},
    "Filya Crystal": {"price": 1000000, "chance": 0.01},
}

achievements = {
    "First Diamond": False, "100 Diamonds": False, "1000 Diamonds": False,
    "First Million": False, "First Billion": False, "Trillionaire": False,
    "36 Helpers": False, "Pickaxe 20": False, "Depth 10": False,
    "Prestige 1": False, "Prestige 5": False,
    "Pet": False, "Zoo": False,
    "Lucky": False, "Unlucky": False,
    "Filya Ore": False, "Adamantite": False, "Filya Crystal": False,
    "Boss 1": False, "Boss 2": False, "Boss 3": False,
    "Boss 4": False, "Boss 5": False, "Boss 6": False,
    "Weapon": False, "Potion": False, "New Location": False,
    "Cosmo Cat": False, "Filya God": False,
    "Ring of Power": False, "Filya Amulet": False, "Miner's Crown": False,
    "Titan's Ring": False, "Filya's Wreath": False,
    "Boss Slayer": False,
    "1 Star": False, "5 Stars": False, "10 Stars": False,
}

tariffs = [
    {"name": "Filya 1",      "gb": 20, "min": 100, "sms": 100, "month": 345, "bonus": 0.10},
    {"name": "Filya 2",      "gb": 10, "min": 100, "sms": 30,  "month": 300, "bonus": 0.05},
    {"name": "Filya 3",      "gb": 50, "min": 250, "sms": 100, "month": 445, "bonus": 0.20},
    {"name": "Filya 4",      "gb": 5,  "min": 500, "sms": 0,   "month": 460, "bonus": 0.15},
    {"name": "Filya Kids",   "gb": 100,"min": 90,  "sms": 0,   "month": 630, "bonus": 0.25},
    {"name": "Filya Budget", "gb": 10, "min": 100, "sms": 10,  "month": 299, "bonus": 0.03},
]

prestige_shop = {
    "Strong Pickaxe": {"price": 100, "bonus": 0.20, "description": "+20% to mining"},
    "Deep Mines":     {"price": 150, "bonus": 0.15, "description": "+15% to mining"},
    "Lucky Filya":    {"price": 200, "bonus": 0.25, "description": "+25% to mining"},
    "Golden Hands":   {"price": 300, "bonus": 0.40, "description": "+40% to mining"},
    "Blessing":       {"price": 500, "bonus": 0.75, "description": "+75% to mining"},
}
prestige_bought = {k: False for k in prestige_shop}


def save_game():
    data = {
        "money": money, "pickaxe": pickaxe, "total_diamonds": total_diamonds,
        "record": record, "auto": auto, "helpers": helpers,
        "depth": depth, "tariff": tariff, "speed": speed,
        "prestige": prestige, "total_mined": total_mined,
        "stars": stars,
        "pets": {k: {"bought": v["bought"]} for k, v in pets.items()},
        "bosses_defeated": bosses_defeated,
        "weapons": {k: v["bought"] for k, v in weapons.items()},
        "damage_multipliers": {k: v["bought"] for k, v in damage_multipliers.items()},
        "location": location,
        "locations_unlocked": {k: v["unlocked"] for k, v in locations.items()},
        "secret_pets": {k: v["bought"] for k, v in secret_pets.items()},
    }
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_game():
    global money, pickaxe, total_diamonds, record, auto, helpers
    global depth, tariff, speed, prestige, total_mined, pets, bosses_defeated
    global location, stars
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        money = data.get("money", 0)
        pickaxe = data.get("pickaxe", 1)
        total_diamonds = data.get("total_diamonds", 0)
        record = data.get("record", 0)
        auto = data.get("auto", False)
        helpers = data.get("helpers", 0)
        depth = data.get("depth", 1)
        tariff = data.get("tariff", 0)
        speed = data.get("speed", 1)
        prestige = data.get("prestige", 0)
        total_mined = data.get("total_mined", 0)
        stars = data.get("stars", 0)
        if "pets" in data:
            for name in pets:
                if name in data["pets"]:
                    pets[name]["bought"] = data["pets"][name].get("bought", False)
        if "bosses_defeated" in data:
            bosses_defeated = data["bosses_defeated"]
        if "weapons" in data:
            for name in weapons:
                if name in data["weapons"]:
                    weapons[name]["bought"] = data["weapons"][name]
        if "damage_multipliers" in data:
            for name in damage_multipliers:
                if name in data["damage_multipliers"]:
                    damage_multipliers[name]["bought"] = data["damage_multipliers"][name]
        if "location" in data:
            location = data["location"]
        if "locations_unlocked" in data:
            for name in locations:
                if name in data["locations_unlocked"]:
                    locations[name]["unlocked"] = data["locations_unlocked"][name]
        if "secret_pets" in data:
            for name in secret_pets:
                if name in data["secret_pets"]:
                    secret_pets[name]["bought"] = data["secret_pets"][name]
    except Exception as e:
        print(f"(Save load skipped: {e})")


def dig(helper=False, silent=False):
    global money, total_diamonds, total_mined, golden_vein

    multiplier = 1.0
    multiplier += pickaxe * 0.1
    multiplier += depth * 0.05
    multiplier += prestige * 0.25
    multiplier += stars * 1.0
    if tariff > 0:
        multiplier += tariffs[tariff - 1]["bonus"]
    for p in pets.values():
        if p["bought"]:
            multiplier += p["bonus"]
    for p in secret_pets.values():
        if p["bought"]:
            multiplier += p["bonus"]
    for name, bought in prestige_bought.items():
        if bought:
            multiplier += prestige_shop[name]["bonus"]
    multiplier += locations[location]["bonus"]
    if potion_effect == "x2":
        multiplier *= 2
    elif potion_effect == "x5":
        multiplier *= 5
    elif potion_effect == "x10":
        multiplier *= 10
    elif potion_effect == "x25":
        multiplier *= 25

    if golden_vein:
        multiplier *= 10
        golden_vein = False

    rand = random.uniform(0, 100)
    accumulated = 0
    amount = 0
    found = []

    for name, ore in ores.items():
        accumulated += ore["chance"]
        if rand <= accumulated:
            found.append(name)
            amount = int(ore["price"] * multiplier)
            if name == "diamond":
                total_diamonds += 1
            if name == "Filya Ore":
                achievements["Filya Ore"] = True
                if not silent:
                    print("🌟 YOU FOUND FILYa ORE! 🌟")
            if name == "Adamantite":
                achievements["Adamantite"] = True
                if not silent:
                    print("💠 YOU FOUND ADAMANTITE! 💠")
            if name == "Filya Crystal":
                achievements["Filya Crystal"] = True
                if not silent:
                    print("💎💎💎 FILYa CRYSTAL! 💎💎💎")
            break

    if not found:
        if not silent:
            print("💨 Empty...")
        return 0

    if not silent:
        if helper:
            print(f"🐱 Helper found: {', '.join(found)}")
        else:
            print(f"✅ Found: {', '.join(found)}")
        print(f"💵 Earned: {amount:,} $")

    money += amount
    total_mined += amount
    return amount


def random_event():
    global golden_vein, shop_discount, helpers, total_diamonds, money
    rand = random.randint(1, 100)
    if rand <= 3:
        golden_vein = True
        print("🌟 GOLDEN VEIN! Next dig ×10!")
        achievements["Lucky"] = True
    elif rand <= 5:
        loss = int(money * 0.1)
        money = max(0, money - loss)
        print(f"💥 COLLAPSE! Lost {loss:,} $")
        achievements["Unlucky"] = True
    elif rand <= 6:
        total_diamonds += 10
        print("💎 FILYa TREASURE! +10 diamonds!")
    elif rand <= 8:
        helpers += 1
        print("🧙 GNOME HELPER! +1 helper!")
    elif rand <= 9:
        shop_discount = True
        print("🛒 SHOP DISCOUNT! Next purchase −50%!")


def check_achievements():
    if total_diamonds >= 1 and not achievements["First Diamond"]:
        achievements["First Diamond"] = True; print("🏆 First Diamond!")
    if total_diamonds >= 100 and not achievements["100 Diamonds"]:
        achievements["100 Diamonds"] = True; print("🏆 100 Diamonds!")
    if total_diamonds >= 1000 and not achievements["1000 Diamonds"]:
        achievements["1000 Diamonds"] = True; print("🏆 1000 Diamonds!")
    if money >= 1000000 and not achievements["First Million"]:
        achievements["First Million"] = True; print("🏆 First Million!")
    if money >= 1000000000 and not achievements["First Billion"]:
        achievements["First Billion"] = True; print("🏆 First Billion!")
    if money >= 1000000000000 and not achievements["Trillionaire"]:
        achievements["Trillionaire"] = True; print("🏆 TRILLIONAIRE!")
    if helpers >= 36 and not achievements["36 Helpers"]:
        achievements["36 Helpers"] = True; print("🏆 36 Helpers!")
    if pickaxe >= 20 and not achievements["Pickaxe 20"]:
        achievements["Pickaxe 20"] = True; print("🏆 Pickaxe 20!")
    if depth >= 10 and not achievements["Depth 10"]:
        achievements["Depth 10"] = True; print("🏆 Depth 10!")
    if prestige >= 1 and not achievements["Prestige 1"]:
        achievements["Prestige 1"] = True; print("🏆 Prestige 1!")
    if prestige >= 5 and not achievements["Prestige 5"]:
        achievements["Prestige 5"] = True; print("🏆 Prestige 5!")
    if any(p["bought"] for p in pets.values()) and not achievements["Pet"]:
        achievements["Pet"] = True; print("🏆 First Pet!")
    if all(p["bought"] for p in pets.values()) and not achievements["Zoo"]:
        achievements["Zoo"] = True; print("🏆 ZOO!")
    if 5 in bosses_defeated and not achievements["Boss 1"]:
        achievements["Boss 1"] = True; print("🏆 Boss 1 defeated!")
    if 10 in bosses_defeated and not achievements["Boss 2"]:
        achievements["Boss 2"] = True; print("🏆 Boss 2 defeated!")
    if 15 in bosses_defeated and not achievements["Boss 3"]:
        achievements["Boss 3"] = True; print("🏆 Boss 3 defeated!")
    if 20 in bosses_defeated and not achievements["Boss 4"]:
        achievements["Boss 4"] = True; print("🏆 Boss 4 defeated!")
    if 25 in bosses_defeated and not achievements["Boss 5"]:
        achievements["Boss 5"] = True; print("🏆 Boss 5 defeated!")
    if 30 in bosses_defeated and not achievements["Boss 6"]:
        achievements["Boss 6"] = True; print("🏆 Boss 6 defeated!")
    if any(w["bought"] for w in weapons.values() if w["price"] > 0) and not achievements["Weapon"]:
        achievements["Weapon"] = True; print("🏆 First Weapon!")
    if any(l["unlocked"] for l in locations.values() if l["price"] > 0) and not achievements["New Location"]:
        achievements["New Location"] = True; print("🏆 New Location!")
    if secret_pets["Cosmo Cat"]["bought"] and not achievements["Cosmo Cat"]:
        achievements["Cosmo Cat"] = True; print("🏆 COSMO CAT!")
    if secret_pets["Filya God"]["bought"] and not achievements["Filya God"]:
        achievements["Filya God"] = True; print("🏆 FILYa GOD!")
    if damage_multipliers["Ring of Power"]["bought"] and not achievements["Ring of Power"]:
        achievements["Ring of Power"] = True; print("🏆 Ring of Power!")
    if damage_multipliers["Filya Amulet"]["bought"] and not achievements["Filya Amulet"]:
        achievements["Filya Amulet"] = True; print("🏆 Filya Amulet!")
    if damage_multipliers["Miner's Crown"]["bought"] and not achievements["Miner's Crown"]:
        achievements["Miner's Crown"] = True; print("🏆 Miner's Crown!")
    if damage_multipliers["Titan's Ring"]["bought"] and not achievements["Titan's Ring"]:
        achievements["Titan's Ring"] = True; print("🏆 Titan's Ring!")
    if damage_multipliers["Filya's Wreath"]["bought"] and not achievements["Filya's Wreath"]:
        achievements["Filya's Wreath"] = True; print("🏆 Filya's Wreath!")
    if len(bosses_defeated) >= 6 and not achievements["Boss Slayer"]:
        achievements["Boss Slayer"] = True; print("🏆 BOSS SLAYER!")
    if stars >= 1 and not achievements["1 Star"]:
        achievements["1 Star"] = True; print("🏆 1 STAR!")
    if stars >= 5 and not achievements["5 Stars"]:
        achievements["5 Stars"] = True; print("🏆 5 STARS!")
    if stars >= 10 and not achievements["10 Stars"]:
        achievements["10 Stars"] = True; print("🏆 10 STARS!")


def player_damage():
    base = pickaxe * 1000 + helpers * 500 + prestige * 2000
    best_weapon = 0
    for w in weapons.values():
        if w["bought"] and w["damage"] > best_weapon:
            best_weapon = w["damage"]
    damage = base + best_weapon
    for m in damage_multipliers.values():
        if m["bought"]:
            damage *= m["multiplier"]
    return damage


def fight_boss(boss_depth):
    global money, total_diamonds, bosses_defeated
    if boss_depth in bosses_defeated:
        print(f"❌ {bosses[boss_depth]['name']} already defeated!")
        return
    b = bosses[boss_depth]
    print(f"\n⚔️ BOSS FIGHT: {b['name']}!")
    damage = player_damage()
    print(f"Your damage: {damage:,} HP | Boss HP: {b['hp']:,}")
    if damage >= b["hp"]:
        print(f"🎉 VICTORY! {b['name']} defeated!")
        money += b["reward"]
        total_diamonds += b["diamonds"]
        bosses_defeated.append(boss_depth)
        print(f"💰 +{b['reward']:,} $ | 💎 +{b['diamonds']} diamonds")
    else:
        print(f"❌ You lost! Need {b['hp'] - damage:,} HP more")


def prestige_2_0():
    global money, pickaxe, helpers, depth, prestige, stars
    global location, potion_effect, potion_turns, bosses_defeated
    price = 100000000000 * (stars + 1)
    if prestige < 5:
        print(f"❌ Need 5 prestiges! You have {prestige}/5")
        return
    if money < price:
        print(f"❌ Not enough {price - money:,} $")
        return

    money = 0
    pickaxe = 1
    helpers = 0
    depth = 1
    prestige = 0
    location = "Common Mine"
    potion_effect = None
    potion_turns = 0
    bosses_defeated.clear()
    for p in pets.values(): p["bought"] = False
    for p in secret_pets.values(): p["bought"] = False
    for w in weapons.values():
        if w["price"] > 0: w["bought"] = False
    for m in damage_multipliers.values(): m["bought"] = False
    for l in locations.values():
        if l["price"] > 0: l["unlocked"] = False
    for k in prestige_bought: prestige_bought[k] = False

    stars += 1
    save_game()
    print(f"\n🌟 PRESTIGE 2.0! 🌟")
    print(f"You got {stars} ⭐ (+{stars * 100}% to mining!)")
    print("Everything reset except stars, diamonds and achievements.")


print("=" * 40)
print("   🐱 FILYa IN THE MINE v13.0")
print("=" * 40)

load_game()


def show_menu():
    print(f"\n💰 Money: {money:,} $")
    print(f"⛏️ Pickaxe: {pickaxe} | 💎 Diamonds: {total_diamonds} | 🏆 Record: {record:,} $")
    print(f"🐱 Helpers: {helpers} | 🏔️ Depth: {depth} | ⚡ Speed: x{speed}")
    print(f"🌟 Prestige: {prestige} (+{prestige*25}%) | ⭐ Stars: {stars} (+{stars*100}%)")
    print(f"🗺️ Location: {location}")
    if potion_effect:
        print(f"🧪 Potion: {potion_effect} ({potion_turns} turns)")
    if tariff > 0:
        print(f"📱 Tariff: {tariffs[tariff-1]['name']}")
    if auto:
        print("⚡ Auto-dig: ON")
    bought = sum(1 for p in pets.values() if p["bought"])
    sec_bought = sum(1 for p in secret_pets.values() if p["bought"])
    print(f"🐾 Pets: {bought}/{len(pets)} | 🚀 Secret: {sec_bought}/{len(secret_pets)}")
    print(f"⚔️ Damage: {player_damage():,}")
    print("─" * 30)
    print("1-dig 2-salary 3-shop 4-auto 5-record")
    print("6-helper 7-save 8-exit 9-depth 10-tariffs")
    print("11-achievements 12-reset 13-stats 14-prestige")
    print("15-editor 16-pets 17-prestige shop 18-bosses")
    print("19-challenge boss 20-weapons 21-potions 22-locations")
    print("23-diamond shop 24-secret pets 25-damage multipliers")
    print("26-🌟 PRESTIGE 2.0")


while True:
    show_menu()
    cmd = input("What to do? ")

    if cmd == "1":
        print("⭕️⛏️🐈‍⬛ Filya digs...")
        time.sleep(0.3)
        dig()
        if random.randint(1, 100) <= 10:
            random_event()

    elif cmd == "2":
        salary = random.randint(5000, 35000)
        salary += helpers * 1000
        salary += depth * 500
        salary += int(salary * stars * 1.0)

        rand = random.randint(1, 100)
        if rand <= 1:
            salary *= 3
            print("💎💎💎 TRIPLE SALARY!!! 💎💎💎")
        elif rand <= 11:
            salary *= 2
            print("🎉 DOUBLE SALARY!")

        money += salary
        total_mined += salary
        print(f"🗃👨‍💼 Manager gave {salary:,} $")

    elif cmd == "3":
        print("\n🏪 SHOP")
        pickaxe_price = 10000 * pickaxe
        speed_price = 200000 * speed
        if shop_discount:
            pickaxe_price //= 2
            speed_price //= 2
            print("🛒 DISCOUNT −50%!")
        print(f"1 - Pickaxe ({pickaxe}→{pickaxe+1}) — {pickaxe_price:,} $")
        print(f"2 - Speed (x{speed}→x{speed+1}) — {speed_price:,} $")
        print("3 - Back")
        shop = input("What to buy? ")
        if shop == "1":
            if money >= pickaxe_price:
                money -= pickaxe_price; pickaxe += 1
                print(f"✅ Pickaxe: {pickaxe}")
                shop_discount = False
            else:
                print(f"❌ Not enough {pickaxe_price - money:,} $")
        elif shop == "2":
            if money >= speed_price:
                money -= speed_price; speed += 1
                print(f"✅ Speed: x{speed}")
                shop_discount = False
            else:
                print(f"❌ Not enough {speed_price - money:,} $")

    elif cmd == "4":
        if auto:
            print("⚡ Already ON")
        elif money >= 100000:
            money -= 100000; auto = True
            print("⚡ Auto-dig ON!")
        else:
            print("❌ Need 100000 $")

    elif cmd == "5":
        if money > record:
            record = money
            print(f"🏆 New record: {record:,} $!")
        else:
            print(f"🏆 Record: {record:,} $")

    elif cmd == "6":
        price = 50000 * (helpers + 1)
        if money >= price:
            money -= price; helpers += 1
            print(f"🐱 Helper: {helpers}")
        else:
            print(f"❌ Need {price:,} $")

    elif cmd == "7":
        save_game()
        print("💾 Saved!")

    elif cmd == "8":
        save_game()
        print(f"\n🐱 Filya earned: {money:,} $")
        break

    elif cmd == "9":
        print(f"\n🏔️ DEPTH: {depth}")
        price = 100000 * (depth ** 2)
        print(f"Go deeper → {depth+1} — {price:,} $")
        new_depth = depth + 1
        if new_depth in bosses and new_depth not in bosses_defeated:
            b = bosses[new_depth]
            print(f"⚠️ BOSS AHEAD: {b['name']}!")
        print("1-go deeper 2-back")
        if input() == "1":
            if money >= price:
                money -= price
                depth += 1
                print(f"✅ Depth: {depth}")
                if depth in bosses and depth not in bosses_defeated:
                    fight_boss(depth)
            else:
                print(f"❌ Not enough {price - money:,} $")

    elif cmd == "10":
        print("\n📱 TARIFFS")
        for i, t in enumerate(tariffs, 1):
            status = "✅" if tariff == i else "  "
            print(f"{status} {i}. {t['name']}: {t['gb']}GB — {t['month']}$ (+{int(t['bonus']*100)}%)")
        print("0-disable 1-enable")
        choice = input("What? ")
        if choice == "1":
            num = int(input("Tariff number: "))
            if 1 <= num <= len(tariffs):
                tariff = num
                print(f"✅ {tariffs[num-1]['name']}!")
        elif choice == "0":
            tariff = 0
            print("❌ Disabled")

    elif cmd == "11":
        print("\n🏆 ACHIEVEMENTS")
        for name, done in achievements.items():
            print(f"{'✅' if done else '⬜'} {name}")

    elif cmd == "12":
        if input("⚠️ Reset? 1-yes 2-no: ") == "1":
            money=0; pickaxe=1; total_diamonds=0; record=0
            auto=False; helpers=0; depth=1; tariff=0
            speed=1; prestige=0; total_mined=0; stars=0
            bosses_defeated.clear()
            location = "Common Mine"
            potion_effect = None; potion_turns = 0
            for p in pets.values(): p["bought"] = False
            for k in prestige_bought: prestige_bought[k] = False
            for w in weapons.values():
                if w["price"] > 0: w["bought"] = False
            for l in locations.values():
                if l["price"] > 0: l["unlocked"] = False
            for p in secret_pets.values(): p["bought"] = False
            for m in damage_multipliers.values(): m["bought"] = False
            save_game()
            print("🔄 Reset!")

    elif cmd == "13":
        print("\n📊 STATS")
        print(f"Total mined: {total_mined:,} $")
        print(f"Diamonds: {total_diamonds}")
        print(f"Damage: {player_damage():,} HP")
        print(f"Stars: {stars} ⭐ (+{stars * 100}%)")
        m = 1.0 + pickaxe*0.1 + depth*0.05 + prestige*0.25 + stars*1.0
        if tariff > 0: m += tariffs[tariff-1]["bonus"]
        for p in pets.values():
            if p["bought"]: m += p["bonus"]
        for p in secret_pets.values():
            if p["bought"]: m += p["bonus"]
        for name, bought in prestige_bought.items():
            if bought: m += prestige_shop[name]["bonus"]
        m += locations[location]["bonus"]
        print(f"Mining multiplier: ×{m:.2f}")

    elif cmd == "14":
        print(f"\n🌟 PRESTIGE: {prestige} (+{prestige*25}%)")
        price = 1000000000 * (prestige + 1)
        print(f"Price: {price:,} $")
        print("1-do 2-back")
        if input() == "1":
            if money >= price:
                money=0; pickaxe=1; helpers=0
                depth=1; tariff=0; auto=False
                prestige += 1
                save_game()
                print(f"🌟 +{prestige*25}%!")
            else:
                print(f"❌ Not enough {price - money:,} $")

    elif cmd == "15":
        print("\n⚙️ EDITOR")
        for i, (name, ore) in enumerate(ores.items(), 1):
            print(f"{i}. {name}: {ore['price']} $ ({ore['chance']}%)")
        print("q-back")
        choice = input("What? ")
        if choice != "q":
            try:
                num = int(choice)
                name = list(ores.keys())[num - 1]
                print("1-price 2-chance")
                edit = input()
                if edit == "1":
                    ores[name]["price"] = int(input("New price: "))
                elif edit == "2":
                    ores[name]["chance"] = float(input("New chance: "))
                print("✅")
            except:
                print("❌")

    elif cmd == "16":
        print("\n🐾 PETS")
        pet_list = list(pets.keys())
        for i, name in enumerate(pet_list, 1):
            p = pets[name]
            status = "✅ Bought" if p["bought"] else f"{p['price']:,} $"
            print(f"{i}. {name}: +{int(p['bonus']*100)}% — {status} | mines x{p['mines']}")
        print("0 - Back")
        try:
            choice = int(input("Which to buy? "))
            if choice == 0:
                pass
            elif 1 <= choice <= len(pet_list):
                name = pet_list[choice - 1]
                if pets[name]["bought"]:
                    print("❌ Already bought")
                else:
                    price = pets[name]["price"]
                    if shop_discount:
                        price //= 2
                        print(f"🛒 DISCOUNT −50%! Price: {price:,} $")
                    if money >= price:
                        money -= price
                        pets[name]["bought"] = True
                        shop_discount = False
                        print(f"✅ {name} bought!")
                    else:
                        print(f"❌ Not enough {price - money:,} $")
            else:
                print("❌ Invalid number")
        except:
            print("❌ Enter a number")

    elif cmd == "17":
        print(f"\n🛒 PRESTIGE SHOP (you have {total_diamonds} 💎)")
        prestige_list = list(prestige_shop.keys())
        for i, name in enumerate(prestige_list, 1):
            b = prestige_shop[name]
            status = "✅" if prestige_bought[name] else f"{b['price']} 💎"
            print(f"{i}. {name}: {b['description']} — {status}")
        print("0-back")
        try:
            choice = int(input("What to buy? "))
            if choice == 0:
                pass
            elif 1 <= choice <= len(prestige_list):
                name = prestige_list[choice - 1]
                if prestige_bought[name]:
                    print("❌ Already bought")
                elif total_diamonds >= prestige_shop[name]["price"]:
                    total_diamonds -= prestige_shop[name]["price"]
                    prestige_bought[name] = True
                    print(f"✅ {name} bought!")
                else:
                    print(f"❌ Need {prestige_shop[name]['price']} 💎")
            else:
                print("❌ Invalid number")
        except:
            print("❌ Enter a number")

    elif cmd == "18":
        print("\n⚔️ BOSSES")
        for d, b in bosses.items():
            status = "✅ Defeated" if d in bosses_defeated else "⬜ Not defeated"
            print(f"Depth {d}: {b['name']} (HP {b['hp']:,}) — {status}")

    elif cmd == "19":
        print("\n⚔️ CHALLENGE BOSS")
        for d, b in bosses.items():
            if d not in bosses_defeated:
                print(f"{d}. {b['name']} — depth {d}, HP {b['hp']:,}")
        print("0-back")
        try:
            choice = int(input("Which to challenge? "))
            if choice == 0:
                pass
            elif choice in bosses:
                fight_boss(choice)
            else:
                print("❌ No such boss")
        except:
            print("❌ Enter a number")

    elif cmd == "20":
        print(f"\n🗡️ WEAPONS (your damage: {player_damage():,})")
        weapon_list = list(weapons.keys())
        for i, name in enumerate(weapon_list, 1):
            w = weapons[name]
            status = "✅ Bought" if w["bought"] else f"{w['price']:,} $"
            print(f"{i}. {name}: +{w['damage']:,} damage — {status}")
        print("0 - Back")
        try:
            choice = int(input("What to buy? "))
            if choice == 0:
                pass
            elif 1 <= choice <= len(weapon_list):
                name = weapon_list[choice - 1]
                if weapons[name]["bought"]:
                    print("❌ Already bought")
                elif money >= weapons[name]["price"]:
                    money -= weapons[name]["price"]
                    weapons[name]["bought"] = True
                    print(f"✅ {name} bought!")
                else:
                    print(f"❌ Not enough {weapons[name]['price'] - money:,} $")
            else:
                print("❌ Invalid number")
        except:
            print("❌ Enter a number")

    elif cmd == "21":
        print("\n🧪 POTIONS")
        potion_list = list(potions.keys())
        for i, name in enumerate(potion_list, 1):
            p = potions[name]
            print(f"{i}. {name}: {p['effect']} mining for {p['turns']} turns — {p['price']:,} $")
        print("0 - Back")
        try:
            choice = int(input("What to buy? "))
            if choice == 0:
                pass
            elif 1 <= choice <= len(potion_list):
                name = potion_list[choice - 1]
                if money >= potions[name]["price"]:
                    money -= potions[name]["price"]
                    potion_effect = potions[name]["effect"]
                    potion_turns = potions[name]["turns"]
                    achievements["Potion"] = True
                    print(f"✅ {name} drunk! {potion_effect} for {potion_turns} turns")
                else:
                    print(f"❌ Not enough {potions[name]['price'] - money:,} $")
            else:
                print("❌ Invalid number")
        except:
            print("❌ Enter a number")

    elif cmd == "22":
        print("\n🗺️ LOCATIONS")
        location_list = list(locations.keys())
        for i, name in enumerate(location_list, 1):
            l = locations[name]
            status = "✅ Unlocked" if l["unlocked"] else f"{l['price']:,} $"
            print(f"{i}. {name}: +{int(l['bonus']*100)}% — {status}")
        print("0 - Back")
        try:
            choice = int(input("Where to go? "))
            if choice == 0:
                pass
            elif 1 <= choice <= len(location_list):
                name = location_list[choice - 1]
                if locations[name]["unlocked"]:
                    location = name
                    print(f"✅ Moved to {name}!")
                elif money >= locations[name]["price"]:
                    money -= locations[name]["price"]
                    locations[name]["unlocked"] = True
                    location = name
                    achievements["New Location"] = True
                    print(f"✅ {name} unlocked! Moved there!")
                else:
                    print(f"❌ Not enough {locations[name]['price'] - money:,} $")
            else:
                print("❌ Invalid number")
        except:
            print("❌ Enter a number")

    elif cmd == "23":
        print(f"\n💎 DIAMOND SHOP (you have {total_diamonds} 💎)")
        for i, (num, pack) in enumerate(diamond_shop.items(), 1):
            print(f"{num}. {pack['diamonds']:,} 💎 — {pack['price']:,} $")
        print("0 - Back")
        try:
            choice = int(input("What to buy? "))
            if choice == 0:
                pass
            elif choice in diamond_shop:
                pack = diamond_shop[choice]
                if money >= pack["price"]:
                    money -= pack["price"]
                    total_diamonds += pack["diamonds"]
                    print(f"✅ +{pack['diamonds']:,} 💎! Now you have {total_diamonds} diamonds")
                else:
                    print(f"❌ Not enough {pack['price'] - money:,} $")
            else:
                print("❌ Invalid number")
        except:
            print("❌ Enter a number")

    elif cmd == "24":
        print("\n🚀 SECRET PETS")
        sec_list = list(secret_pets.keys())
        for i, name in enumerate(sec_list, 1):
            p = secret_pets[name]
            status = "✅ Bought" if p["bought"] else f"{p['price']:,} $"
            print(f"{i}. {name}: {p['description']} — {status}")
        print("0 - Back")
        try:
            choice = int(input("Which to buy? "))
            if choice == 0:
                pass
            elif 1 <= choice <= len(sec_list):
                name = sec_list[choice - 1]
                if secret_pets[name]["bought"]:
                    print("❌ Already bought")
                elif money >= secret_pets[name]["price"]:
                    money -= secret_pets[name]["price"]
                    secret_pets[name]["bought"] = True
                    print(f"✅ {name} bought!")
                else:
                    print(f"❌ Not enough {secret_pets[name]['price'] - money:,} $")
            else:
                print("❌ Invalid number")
        except:
            print("❌ Enter a number")

    elif cmd == "25":
        print(f"\n💍 DAMAGE MULTIPLIERS (your damage: {player_damage():,})")
        mult_list = list(damage_multipliers.keys())
        for i, name in enumerate(mult_list, 1):
            m = damage_multipliers[name]
            status = "✅ Bought" if m["bought"] else f"{m['price']:,} $"
            print(f"{i}. {name}: ×{m['multiplier']} damage — {status}")
        print("0 - Back")
        try:
            choice = int(input("What to buy? "))
            if choice == 0:
                pass
            elif 1 <= choice <= len(mult_list):
                name = mult_list[choice - 1]
                if damage_multipliers[name]["bought"]:
                    print("❌ Already bought")
                elif money >= damage_multipliers[name]["price"]:
                    money -= damage_multipliers[name]["price"]
                    damage_multipliers[name]["bought"] = True
                    print(f"✅ {name} bought! Now damage ×{damage_multipliers[name]['multiplier']}")
                else:
                    print(f"❌ Not enough {damage_multipliers[name]['price'] - money:,} $")
            else:
                print("❌ Invalid number")
        except:
            print("❌ Enter a number")

    elif cmd == "26":
        price = 100000000000 * (stars + 1)
        print(f"\n🌟 PRESTIGE 2.0")
        print(f"Current stars: {stars} ⭐ (+{stars * 100}%)")
        print(f"Prestiges done: {prestige}/5")
        print(f"Price: {price:,} $")
        print(f"\nWill be reset:")
        print("- Money, pickaxe, helpers, depth")
        print("- Prestige, pets, secret pets")
        print("- Weapons, multipliers, locations, bosses")
        print(f"\nWill remain:")
        print(f"- {stars + 1} ⭐ (+{(stars + 1) * 100}%)")
        print(f"- {total_diamonds} 💎")
        print("- Achievements 🏆")
        print("\n1 - Do Prestige 2.0")
        print("2 - Back")
        if input("Choice: ") == "1":
            prestige_2_0()

    check_achievements()

    if tariff > 0:
        fee = tariffs[tariff - 1]["month"]
        if money >= fee:
            money -= fee
        else:
            tariff = 0
            print("❌ Tariff disabled!")

    if auto:
        for _ in range(speed):
            dig(silent=True)

    total_digs = min(helpers * speed, 20)
    if total_digs > 0:
        helper_sum = 0
        for _ in range(total_digs):
            helper_sum += dig(helper=True, silent=True)
        print(f"🐱 Helpers: +{helper_sum:,} $")

    for name, p in pets.items():
        if p["bought"]:
            pet_sum = 0
            for _ in range(p["mines"]):
                pet_sum += dig(helper=True, silent=True)
            if pet_sum > 0:
                print(f"🐾 {name}: +{pet_sum:,} $")

    for name, p in secret_pets.items():
        if p["bought"]:
            pet_sum = 0
            for _ in range(p["mines"]):
                pet_sum += dig(helper=True, silent=True)
            if pet_sum > 0:
                print(f"🚀 {name}: +{pet_sum:,} $")

    if potion_turns > 0:
        potion_turns -= 1
        print(f"🧪 Potion: {potion_turns} turns left")
        if potion_turns == 0:
            print("🧪 Potion expired!")
            potion_effect = None