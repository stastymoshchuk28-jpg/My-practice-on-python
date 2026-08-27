#Done
#v1.0

#On ukrainian language

from time import sleep, time

from random import randint, choice

start_time = time()

player_level = 0

player_xp = 0

need_xp = 25 + (player_level * 10)

random_skills_knight = ["Сильний удар", "Важкий удар", "Розпечений удар мечем", "Швидкий удар"]
random_skills_archer = ["Сильна стріла", "Швидка стріла", "Льодяна стріла", "Вогняна стріла"]
random_skills_mage = ["Фаербол", "Тсунамі", "Заморозка", "Стіна з камню"]

def create_person():
    print("👋 Ласкаво просимо вас, користувач, до гри '✨Magical adventures✨'!")
    print(" ")
    sleep(0.5)
    print("🎮 Давайте створимо ваш аккаунт для гри!")
    print(" ")
    sleep(0.5)
    while True:
        player_name = input("⌨️ Введіть нік для аккаунту: ")
        print(" ")
        sleep(0.5)
        if player_name.isdigit():
            print("❗ Нік не може бути тільки з цифр!")
            print(" ")
            sleep(0.5)
        elif player_name == "":
            print("❗ Нік не може бути порожнім!")
            print(" ")
            sleep(0.5)
        else:
            if len(player_name) >= 8:
                print("✅ Ваш нік збережено!")
                print(" ")
                sleep(0.5)
                break
            else:
                print("❗ Нік занадто короткий, має бути як мінімум 8 символів!")
                print(" ")
                sleep(0.5)
    print(f"👍 {player_name}, дякуємо вам за те, що ви написали свій нік!")
    print(" ")
    sleep(0.5)
    print("⚔️🏹🪄 Оберіть, будь ласка, класс перед тим як грати:")
    sleep(0.1)
    print("1️⃣  1. Лицар")
    sleep(0.1)
    print("2️⃣  2. Лучник")
    sleep(0.1)
    print("3️⃣  3. Маг")
    print(" ")
    sleep(0.5)
    while True:
        player_class_choice = input("⌨️ Введіть номер класса для гри:")
        print(" ")
        sleep(0.5)
        if player_class_choice.isdigit():
            player_class_choice = int(player_class_choice)
            if player_class_choice == 1:
                print("✅ Ви обрали лицаря, ваш класс збережено!")
                print(" ")
                sleep(0.5)
                player_class = "Лицар"
                weapon = "Старий меч"
                skills = ["Слабкий удар"]
                break
            elif player_class_choice == 2:
                print("✅ Ви обрали лучника, ваш класс збережено!")
                print(" ")
                sleep(0.5)
                player_class = "Лучник"
                weapon = "Старий лук"
                skills = ["Слабка стріла"]
                break
            elif player_class_choice == 3:
                print("✅ Ви обрали мага, ваш класс збережено!")
                print(" ")
                sleep(0.5)
                player_class = "Маг"
                weapon = "Старий посох"
                skills = ["Повітряний меч"]
                break
            else:
                print("❗ Неправильний номер классу!")
                print(" ")
                sleep(0.5)
                continue
        elif player_class_choice == "":
            print("❗ Номер классу не може бути порожнім!")
            print(" ")
            sleep(0.5)
            continue
        else:
            print("❗️ Напишіть номер классу замість букв або символів!")
            print(" ")
            sleep(0.5)
            continue
    return player_name, player_class, weapon, skills
player_name, player_class, weapon, skills = create_person()

def go_to_dungeon(player_level, player_class, player_name, player_xp, weapon, skills, need_xp):
    global random_skills_knight, random_skills_archer, random_skills_mage
    action_d = randint(0, 2)
    if action_d == 0:
        print(f"🏃 {player_name}, ви відправилися у підземелля!")
        print(" ")
        sleep(0.5)
        print("🏃 Ви йшли дуже довго але побачили щось на підлозі.")
        print(" ")
        sleep(0.5)
        print("💰 Це скриня!")
        print(" ")
        sleep(0.5)
        open_chest = input("⌨️ Ви хочете відкрити скриню? (Так або ні)").lower()
        print(" ")
        sleep(0.5)
        if open_chest == "так":
            random_item = randint(0, 1)
            if random_item == 0:
                print("🫱 Ви відкриваєте скриню... І бачете сяйво!")
                print(" ")
                sleep(0.5)
                print("✨ Там щось дивне! Схоже на золото, але рідина...")
                print(" ")
                sleep(0.5)
                print("✨ Ця рідина освітила вас!")
                print(" ")
                sleep(0.5)
                claimed_lvl = 1
                left_xp = need_xp - player_xp
                if left_xp < 0:
                    left_xp = 0
                print(f"➕ Ви отримали {claimed_lvl} левли!")
                sleep(0.1)
                print(f"✨ Ваш левел {player_level}!")
                sleep(0.1)
                print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
                print(" ")
                sleep(0.1)
                print("➕ Ваш левел збільшено!")
                print(" ")
                sleep(0.1)
                player_level += 1
                player_xp = 0
                need_xp = 25 + (player_level * 10)
                left_xp = need_xp - player_xp
                print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
                print(" ")
                sleep(0.5)
                print("🏃 Ви вийшли з підземелля!")
                print(" ")
                sleep(0.5)
                return player_level, player_xp, need_xp, skills, weapon
            elif random_item == 1:
                if player_class == "Лицар":
                    print("⚔️ Там меч! Ідеальний, новий! Але чому він тут?")
                    print(" ")
                    sleep(0.5)
                    pick_up = input("⌨️ Чи бажаєте ви взяти його? (Так або ні) ").lower()
                    print(" ")
                    sleep(0.5)
                    if pick_up == "так":
                        print("⚔️️ Ви берете цей прекрасний меч!")
                        print(" ")
                        sleep(0.5)
                        random_sk = choice(random_skills_knight)
                        if not random_sk in skills:
                            print(f"✨ Він дарував вам новий скіл, {player_name}")
                            print(" ")
                            sleep(0.5)
                        weapon = "Хороший меч"
                        print(f"⚔️ Ваш меч: {weapon}")
                        if not random_sk in skills:
                            print(f"✨ Розблокований скіл: {random_sk}!")
                            skills.append(random_sk)
                        print(f"✨ Ваші скіли: {skills}")
                        print(" ")
                        sleep(0.5)
                        print("🏃 Ви вийшли з підземелля!")
                        print(" ")
                        sleep(0.5)
                        return player_level, player_xp, need_xp, skills, weapon
                    else:
                        print("👻 Ви не взяли зброю і у скриня почала оживати!")
                        print(" ")
                        sleep(0.5)
                        print("🏃 Ви злякалися і втекли з підземелля!")
                        print(" ")
                        sleep(0.5)
                        return player_level, player_xp, need_xp, skills, weapon
                elif player_class == "Лучник":
                    print("🏹 Там лук! Ідеальний, новий! Але чому він тут?")
                    print(" ")
                    sleep(0.5)
                    pick_up = input("⌨️ Чи бажаєте ви взяти його? (Так або ні) ").lower()
                    print(" ")
                    sleep(0.5)
                    if pick_up == "так":
                        print("🏹️ Ви берете цей прекрасний лук!")
                        print(" ")
                        sleep(0.5)
                        random_sk = choice(random_skills_archer)
                        if not random_sk in skills:
                            print(f"✨ Він дарував вам новий скіл, {player_name}")
                            print(" ")
                            sleep(0.5)
                        weapon = "Хороший лук"
                        print(f"🏹 Ваш лук: {weapon}")
                        if not random_sk in skills:
                            print(f"✨ Розблокований скіл: {random_sk}!")
                            skills.append(random_sk)
                        print(f"✨ Ваші скіли: {skills}")
                        print(" ")
                        sleep(0.5)
                        print("🏃 Ви вийшли з підземелля!")
                        print(" ")
                        sleep(0.5)
                        return player_level, player_xp, need_xp, skills, weapon
                    else:
                        print("👻 Ви не взяли зброю і у скриня почала оживати!")
                        print(" ")
                        sleep(0.5)
                        print("🏃 Ви злякалися і втекли з підземелля!")
                        print(" ")
                        sleep(0.5)
                        return player_level, player_xp, need_xp, skills, weapon
                elif player_class == "Маг":
                    print("✨ Там посох! Ідеальний, новий! Але чому він тут?")
                    print(" ")
                    sleep(0.5)
                    pick_up = input("⌨️ Чи бажаєте ви взяти його? (Так або ні) ").lower()
                    print(" ")
                    sleep(0.5)
                    if pick_up == "так":
                        print("🪄️ Ви берете цей прекрасний посох!")
                        print(" ")
                        sleep(0.5)
                        random_sk = choice(random_skills_mage)
                        if not random_sk in skills:
                            print(f"✨ Він дарував вам новий скіл, {player_name}")
                            print(" ")
                            sleep(0.5)
                        weapon = "Хороший посох"
                        print(f"🪄  Ваш посох: {weapon}")
                        if not random_sk in skills:
                            print(f"✨ Розблокований скіл: {random_sk}!")
                            skills.append(random_sk)
                        print(f"✨ Ваші скіли: {skills}")
                        print(" ")
                        sleep(0.5)
                        print("🏃 Ви вийшли з підземелля!")
                        print(" ")
                        sleep(0.5)
                        return player_level, player_xp, need_xp, skills, weapon
                    else:
                        print("👻 Ви не взяли зброю і у скриня почала оживати!")
                        print(" ")
                        sleep(0.5)
                        print("🏃 Ви злякалися і втекли з підземелля!")
                        print(" ")
                        sleep(0.5)
                        return player_level, player_xp, need_xp, skills, weapon
        elif open_chest == "ні":
            print("👻 Ви не відкрили цю скриню і вона ожила!")
            print(" ")
            sleep(0.5)
            print("🏃 Ви злякалися і втекли з підземелля.")
            print(" ")
            sleep(0.5)
            return player_level, player_xp, need_xp, skills, weapon
        else:
            print("🏃 Ви пройшли повз скрині, але почули дивний звук позаду...")
            print(" ")
            sleep(0.5)
            print("👻 Ви подивилися на цю скриню і вона ожила!")
            print(" ")
            sleep(0.5)
            print("🏃 Ви злякалися і втекли з підземелля.")
            print(" ")
            sleep(0.5)
            return player_level, player_xp, need_xp, skills, weapon
    elif action_d == 1:
        print("🏃 Ви йшли по підземеллю і зустріли гігантського босса - Міфрілового Дракона!")
        print(" ")
        sleep(0.5)
        print("❗ Рекомендований лвл 25+")
        print(" ")
        sleep(0.5)
        want_to_kill = input("⌨️ Чи спробуєте ви його вбити? (Так або ні) ").lower()
        print(" ")
        sleep(0.5)
        if want_to_kill == "так":
            print(f"⚔️🏹🪄 {player_name}, ви напали на нього з своєю зброєю - {weapon}!")
            print(" ")
            sleep(0.5)
            if player_level < 25:
                print("👎 Ви дуже слабкі, щоб вбити його...")
                print(" ")
                sleep(0.5)
                print("🏃 Ви пішли навтіки від нього...")
                print(" ")
                sleep(0.5)
                print("🏃 Ви втекли з підземелля!")
                print(" ")
                sleep(0.5)
                return player_level, player_xp, need_xp, skills, weapon
            elif player_level >= 25:
                print("💪 Вашої сили достатньо щоб перемогти його!")
                print(" ")
                sleep(0.5)
                random_skill_to_kill = choice(skills)
                print(f"⚔️🏹🪄 Ви вбили його скілом - {random_skill_to_kill}!")
                print(" ")
                sleep(0.5)
                claimed_lvl = 5
                left_xp = need_xp - player_xp
                if left_xp < 0:
                    left_xp = 0
                print(f"➕ Ви отримали 5 левлів!")
                sleep(0.1)
                print(f"✨ Ваш левел {player_level}!")
                sleep(0.1)
                print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
                print(" ")
                sleep(0.1)
                print("➕ Ваш левел збільшено!")
                print(" ")
                sleep(0.1)
                player_level += 5
                player_xp = 0
                need_xp = 25 + (player_level * 10)
                left_xp = need_xp - player_xp
                print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
                print(" ")
                sleep(0.5)
                print("🏃 Ви вийшли з підземелля!")
                print(" ")
                sleep(0.5)
                return player_level, player_xp, need_xp, skills, weapon
        elif want_to_kill == "ні":
            print(f"👎 {player_name}, ви вирішили, що краще не ризикувати!")
            print(" ")
            sleep(0.5)
            print("🏃 Тікайте швидше!")
            print(" ")
            sleep(0.5)
            print("🏃 Ви біжете дуже швидко, цей дракон вас майже наздоганяє!")
            print(" ")
            sleep(0.5)
            print("🏃 Ви встигли добіжати до виходу!")
            print(" ")
            sleep(0.5)
            print("🏃 Ви втекли з підземелля!")
            print(" ")
            sleep(0.5)
            return player_level, player_xp, need_xp, skills, weapon
        else:
            print(f"😨 {player_name}, ви побачивши його дуже сильно злякалися!")
            print(" ")
            sleep(0.5)
            print("🏃 Ви бігли зі всіг ніг!")
            print(" ")
            sleep(0.5)
            print("🏃 Та встигли!")
            print(" ")
            sleep(0.5)
            print("🏃 Ви втелки з підземелля!")
            print(" ")
            sleep(0.5)
            return player_level, player_xp, need_xp, skills, weapon
    elif action_d == 2:
        print("🏃 Ви йшли по підземеллю і зустріли зграю монстрів 10 левлу - Кам'яні големи!")
        print(" ")
        sleep(0.5)
        print("❗ Рекомендований лвл 15+")
        print(" ")
        sleep(0.5)
        want_to_kill = input("⌨️ Чи спробуєте ви їх вбити? (Так або ні) ").lower()
        print(" ")
        sleep(0.5)
        if want_to_kill == "так":
            print(f"⚔️🏹🪄 {player_name}, ви напали на цих монстрів з своєю зброєю - {weapon}!")
            print(" ")
            sleep(0.5)
            if player_level < 15:
                print("👎 Ви дуже слабкі, щоб вбити їх...")
                print(" ")
                sleep(0.5)
                print("🏃 Ви пішли навтіки від цеї сильної зграю кам'яних големів...")
                print(" ")
                sleep(0.5)
                print("🏃 Ви втекли з підземелля!")
                print(" ")
                sleep(0.5)
                return player_level, player_xp, need_xp, skills, weapon
            elif player_level >= 15:
                print("💪 Вашої сили достатньо щоб перемогти кам'яних големів!")
                print(" ")
                sleep(0.5)
                random_skill_to_kill = choice(skills)
                print(f"⚔️🏹🪄 Ви вбили їх цим скілом - {random_skill_to_kill}!")
                print(" ")
                sleep(0.5)
                claimed_lvl = 2
                left_xp = need_xp - player_xp
                if left_xp < 0:
                    left_xp = 0
                print(f"➕ Ви отримали 2 левли!")
                sleep(0.1)
                print(f"✨ Ваш левел {player_level}!")
                sleep(0.1)
                print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
                print(" ")
                sleep(0.1)
                print("➕ Ваш левел збільшено!")
                print(" ")
                sleep(0.1)
                player_level += 2
                player_xp = 0
                need_xp = 25 + (player_level * 10)
                left_xp = need_xp - player_xp
                print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
                print(" ")
                sleep(0.5)
                print("🏃 Ви вийшли з підземелля!")
                print(" ")
                sleep(0.5)
                return player_level, player_xp, need_xp, skills, weapon
        elif want_to_kill == "ні":
            print(f"👎 {player_name}, ви вирішили, що краще не ризикувати!")
            print(" ")
            sleep(0.5)
            print("🏃 Тікайте швидше!")
            print(" ")
            sleep(0.5)
            print("🏃 Ви біжете дуже швидко, ці монстри вас майже наздоганяють!")
            print(" ")
            sleep(0.5)
            print("🏃 Ви встигли добіжати до виходу!")
            print(" ")
            sleep(0.5)
            print("🏃 Ви втекли з підземелля!")
            print(" ")
            sleep(0.5)
            return player_level, player_xp, need_xp, skills, weapon
        else:
            print(f"😨 {player_name}, ви побачивши їх дуже сильно злякалися!")
            print(" ")
            sleep(0.5)
            print("🏃 Ви бігли зі всіг ніг!")
            print(" ")
            sleep(0.5)
            print("🏃 Та встигли!")
            print(" ")
            sleep(0.5)
            print("🏃 Ви втелки з підземелля!")
            print(" ")
            sleep(0.5)
            return player_level, player_xp, need_xp, skills, weapon

def fight_ground_monsters(player_level, player_class, player_name, player_xp, weapon, skills, need_xp):
    global random_skills_knight, random_skills_archer, random_skills_mage
    xp_for_monster = randint(1, 5)
    monsters = randint(1, 5)
    print("🏃 Ви шукали монстрів (Земляних големів) і знайшли!")
    print(" ")
    sleep(0.5)
    if monsters > 3:
        print(f"🧟 Цілу велику зграю з {monsters} монстрів!")
        print(" ")
        sleep(0.5)
        print("❗ В великих зграях вони ще більш не безпечні тому рекомендований лвл 2+")
        print(" ")
        sleep(0.5)
        want_to_kill = input("⌨️ Чи спробуєте ви їх вбити? (Так або ні) ").lower()
        print(" ")
        sleep(0.5)
        if want_to_kill == "так":
            print(f"⚔️🏹🪄 {player_name}, ви вирішили напасти на них з вашою зброєю - {weapon}!")
            print(" ")
            sleep(0.5)
            if player_level < 2:
                print("✨ Ваш левел малий, але ці монстри не набагато сильніші!")
                print(" ")
                sleep(0.5)
                if weapon != "Старий меч" and weapon != "Старий лук" and weapon != "Старий посох":
                    print("✨ І ви це докажете незважаючи на левел!")
                    print(" ")
                    sleep(0.5)
                    print("⚔️🏹🪄 Ваша зброя та скіли дуже сильні, тому ви зможете їх перемогти!")
                    print(" ")
                    sleep(0.5)
                    random_sk = choice(skills)
                    print(f"✨ Для того щоб їх перемогти ви використали цей скіл: {random_sk}!")
                    print(" ")
                    sleep(0.5)
                    print("✨ Через те, що ваш левел був менший ніж рекомендовани ви не знайшли додаткові предмети, але ви зможете отримати багато xp!")
                    print(" ")
                    sleep(0.5)
                    claimed_lvl = 1
                    left_xp = need_xp - player_xp
                    if left_xp < 0:
                        left_xp = 0
                    print(f"➕ Ви отримали {claimed_lvl} левли!")
                    sleep(0.1)
                    print(f"✨ Ваш левел {player_level}!")
                    sleep(0.1)
                    print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
                    print(" ")
                    sleep(0.1)
                    print("➕ Ваш левел збільшено!")
                    print(" ")
                    sleep(0.1)
                    player_level += 1
                    player_xp = 0
                    need_xp = 25 + (player_level * 10)
                    print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
                    print(" ")
                    sleep(0.5)
                    print("🏃 Ви пішли з поляни земляних големів!")
                    print(" ")
                    sleep(0.5)
                    return player_level, player_xp, need_xp, skills, weapon
                else:
                    print(f"👎 Ваша зброя - {weapon} занадто слабка! Ви не зможете їх вбити!")
                    print(" ")
                    sleep(0.5)
                    print("🏃 Тому ви втекли від них!")
                    print(" ")
                    sleep(0.5)
                    return player_level, player_xp, need_xp, skills, weapon
            elif player_level >= 2:
                print("💪 Ваш левел більший ніж у цієї зграї ви з легкістю їх переможете!")
                print(" ")
                sleep(0.5)
                random_sk = choice(skills)
                print(f"✨ Для того щоб їх перемогти ви використали цей скіл: {random_sk}!")
                print(" ")
                sleep(0.5)
                print("🔍 Ваш левел дозволяє вам використати скіл пошуку!")
                print(" ")
                sleep(0.5)
                finded = "'Зілля xp'"
                print(f"✨ Ви знайшли {finded}! Воно додасть вам цілий левел!")
                print(" ")
                sleep(0.5)
                claimed_lvl = 1
                left_xp = need_xp - player_xp
                if left_xp < 0:
                    left_xp = 0
                print(f"➕ Ви отримали {claimed_lvl} левли!")
                sleep(0.1)
                print(f"✨ Ваш левел {player_level}!")
                sleep(0.1)
                print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
                print(" ")
                sleep(0.1)
                print("➕ Ваш левел збільшено!")
                print(" ")
                sleep(0.1)
                player_level += 1
                player_xp = 0
                need_xp = 25 + (player_level * 10)
                print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
                print(" ")
                sleep(0.5)
                print("🏃 Ви пішли з поляни земляних големів!")
                print(" ")
                sleep(0.5)
                return player_level, player_xp, need_xp, skills, weapon
        elif want_to_kill == "ні":
            print("👎 Ви вирішили не нападати на земляних големів!")
            print(" ")
            sleep(0.5)
            print("🏃 Тому ви втекли з поляни Земляних големів")
            print(" ")
            sleep(0.5)
            return player_level, player_xp, need_xp, skills, weapon
        else:
            print("😨 Ви злякалися від їхнього вигляду!")
            print(" ")
            sleep(0.5)
            print("🏃 Тому ви втекли з поляни Земляних големів")
            print(" ")
            sleep(0.5)
            return player_level, player_xp, need_xp, skills, weapon
    elif monsters > 1 and monsters <= 3:
        print(f"🧟 Малу зграю з {monsters} монстрів!")
        print(" ")
        sleep(0.5)
        print("❗ В малих зграях вони більш не безпечні тому рекомендований лвл 1+")
        print(" ")
        sleep(0.5)
        want_to_kill = input("⌨️ Чи спробуєте ви їх вбити? (Так або ні) ").lower()
        print(" ")
        sleep(0.5)
        if want_to_kill == "так":
            print(f"⚔️🏹🪄 {player_name}, ви вирішили напасти на них з вашою зброєю - {weapon}!")
            print(" ")
            sleep(0.5)
            if player_level < 1:
                print("✨ Ваш левел малий, але ці монстри не набагато сильніші!")
                print(" ")
                sleep(0.5)
                if weapon != "Старий меч" and weapon != "Старий лук" and weapon != "Старий посох":
                    print("✨ І ви це докажете незважаючи на левел!")
                    print(" ")
                    sleep(0.5)
                    print("⚔️🏹🪄 Ваша зброя та скіли дуже сильні, тому ви зможете їх перемогти!")
                    print(" ")
                    sleep(0.5)
                    random_sk = choice(skills)
                    print(f"✨ Для того щоб їх перемогти ви використали цей скіл: {random_sk}!")
                    print(" ")
                    sleep(0.5)
                    print("✨ Через те, що ваш левел був менший ніж рекомендовани ви не знайшли додаткові предмети, але ви зможете отримати багато xp!")
                    print(" ")
                    sleep(0.5)
                    claimed_lvl = 1
                    left_xp = need_xp - player_xp
                    if left_xp < 0:
                        left_xp = 0
                    print(f"➕ Ви отримали {claimed_lvl} левли!")
                    sleep(0.1)
                    print(f"✨ Ваш левел {player_level}!")
                    sleep(0.1)
                    print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
                    print(" ")
                    sleep(0.1)
                    if left_xp == 0:
                        print("➕ Ваш левел збільшено!")
                        print(" ")
                        sleep(0.1)
                        player_level += 1
                        player_xp = 0
                        need_xp = 25 + (player_level * 10)
                        print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
                        print(" ")
                        sleep(0.5)
                    print("🏃 Ви пішли з поляни земляних големів!")
                    print(" ")
                    sleep(0.5)
                    return player_level, player_xp, need_xp, skills, weapon
                else:
                    print(f"👎 Ваша зброя - {weapon} занадто слабка! Ви не зможете їх вбити!")
                    print(" ")
                    sleep(0.5)
                    print("🏃 Тому ви втекли від них!")
                    print(" ")
                    sleep(0.5)
                    return player_level, player_xp, need_xp, skills, weapon
            elif player_level >= 1:
                print("💪 Ваш левел більший ніж у цієї зграї ви з легкістю їх переможете!")
                print(" ")
                sleep(0.5)
                random_sk = choice(skills)
                print(f"✨ Для того щоб їх перемогти ви використали цей скіл: {random_sk}!")
                print(" ")
                sleep(0.5)
                print("🔍 Ваш левел дозволяє вам використати скіл пошуку!")
                print(" ")
                sleep(0.5)
                finded = "'Зілля xp'"
                print(f"✨ Ви знайшли {finded}! Воно додасть вам цілий левел!")
                print(" ")
                sleep(0.5)
                claimed_lvl = 1
                left_xp = need_xp - player_xp
                if left_xp < 0:
                    left_xp = 0
                print(f"➕ Ви отримали {claimed_lvl} левли!")
                sleep(0.1)
                print(f"✨ Ваш левел {player_level}!")
                sleep(0.1)
                print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
                print(" ")
                sleep(0.1)
                print("➕ Ваш левел збільшено!")
                print(" ")
                sleep(0.1)
                player_level += 1
                player_xp = 0
                need_xp = 25 + (player_level * 10)
                print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
                print(" ")
                sleep(0.5)
                print("🏃 Ви пішли з поляни земляних големів!")
                print(" ")
                sleep(0.5)
                return player_level, player_xp, need_xp, skills, weapon
        elif want_to_kill == "ні":
            print("👎 Ви вирішили не нападати на земляних големів!")
            print(" ")
            sleep(0.5)
            print("🏃 Тому ви втекли з поляни Земляних големів")
            print(" ")
            sleep(0.5)
            return player_level, player_xp, need_xp, skills, weapon
        else:
            print("😨 Ви злякалися від їхнього вигляду!")
            print(" ")
            sleep(0.5)
            print("🏃 Тому ви втекли з поляни Земляних големів")
            print(" ")
            sleep(0.5)
            return player_level, player_xp, need_xp, skills, weapon
    elif monsters == 1:
        print(f"🧟 Всього навсього одного монстра!")
        print(" ")
        sleep(0.5)
        print("✨ Один - зовсім не зможе нічого вам зробити!")
        print(" ")
        sleep(0.5)
        print(f"⚔️🏹🪄  Ну і тому, {player_name}, ви вирішили напасти на нього з вашою зброєю - {weapon}!")
        print(" ")
        sleep(0.5)
        print("💪 Ви дуже сильні, він навіть не встиг і рукою вдарити вас!")
        print(" ")
        sleep(0.5)
        random_sk = choice(skills)
        print(f"✨ Для того щоб його перемогти ви використали цей скіл: {random_sk}!")
        print(" ")
        sleep(0.5)
        print("🔍 Ви вирішили пошукати щось у нього і знайшли якийсь предмет! ")
        print(" ")
        sleep(0.5)
        finded = "'Зілля xp'"
        print(f"✨ Ви знайшли {finded}! Воно додасть вам цілий левел!")
        print(" ")
        sleep(0.5)
        claimed_lvl = 1
        left_xp = need_xp - player_xp
        if left_xp < 0:
            left_xp = 0
        print(f"➕ Ви отримали {claimed_lvl} левли!")
        sleep(0.1)
        print(f"✨ Ваш левел {player_level}!")
        sleep(0.1)
        print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
        print(" ")
        sleep(0.1)
        print("➕ Ваш левел збільшено!")
        print(" ")
        sleep(0.1)
        player_level += 1
        player_xp = 0
        need_xp = 25 + (player_level * 10)
        print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
        print(" ")
        sleep(0.5)
        print("🏃 Ви пішли з поляни земляних големів!")
        print(" ")
        sleep(0.5)
        return player_level, player_xp, need_xp, skills, weapon

def travel_for_resources(player_level, player_class, player_name, player_xp, weapon, skills, need_xp):
    global random_skills_knight, random_skills_archer, random_skills_mage
    
    random_find = randint(0, 2)
    if random_find == 0:
        print(f"🏃 {player_name}, Ви ходили дуже довго...")
        print(" ")
        sleep(0.5)
        print("🏃 Ви проходили через ліси, річки, поля й інші місця...")
        print(" ")
        sleep(0.5)
        print("🏃 Але нажаль нічого корисного не знайшли!")
        print(" ")
        sleep(0.5)
        print("🏃 І тому ви повернулися назад додому!")
        print(" ")
        sleep(0.5)
        return player_level, player_xp, need_xp, skills, weapon
    elif random_find == 1:
        print(f"🏃 {player_name}, Ви ходили дуже довго...")
        print(" ")
        sleep(0.5)
        print("🏃 Ви проходили через ліси, річки, поля й інші місця...")
        print(" ")
        sleep(0.5)
        print("🏃 І змогли щось знайти!")
        print(" ")
        sleep(0.5)
        finded = "'Зілля xp'"
        print(f"✨ Це - {finded}! Воно додасть вам цілий левел!")
        print(" ")
        sleep(0.5)
        claimed_xp = need_xp
        player_xp += claimed_xp
        left_xp = need_xp - player_xp
        if left_xp < 0:
            left_xp = 0
        print(f"➕ Ви отримали {claimed_xp} xp!")
        sleep(0.1)
        print(f"✨ Ваш левел {player_level}!")
        sleep(0.1)
        print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
        print(" ")
        sleep(0.1)
        if left_xp == 0:
            print("➕ Ваш левел збільшено!")
            print(" ")
            sleep(0.1)
            player_level += 1
            player_xp = 0
            need_xp = 25 + (player_level * 10)
            print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
            print(" ")
            sleep(0.5)
        print("🏃 Ви пішли назад додому!")
        print(" ")
        sleep(0.5)
        return player_level, player_xp, need_xp, skills, weapon
    elif random_find == 2:
        print(f"🏃 {player_name}, Ви ходили дуже довго...")
        print(" ")
        sleep(0.5)
        print("🏃 Ви проходили через ліси, річки, поля й інші місця...")
        print(" ")
        sleep(0.5)
        print("🏃 Ви знайшли 'Камінь чарування'!")
        print(" ")
        sleep(0.5)
        finded = "'Камінь чарування'"
        print(f"✨ За допомогою нього ви зможете зачарувати свою зброю - {weapon}!")
        print(" ")
        sleep(0.5)
        if player_class == "Лицар":
            print("⚔️️ Ви зачаровуєте свій меч!")
            print(" ")
            sleep(0.5)
            random_sk = choice(random_skills_knight)
            if not random_sk in skills:
                print(f"✨ Зачар подарував вам новий скіл, {player_name}")
                print(" ")
                sleep(0.5)
            if not "Зачарований" in weapon:
                weapon = "Зачарований " + weapon.lower()
            print(f"⚔️ Ваш меч: {weapon}")
            if not random_sk in skills:
                print(f"✨ Розблокований скіл: {random_sk}!")
                skills.append(random_sk)
            print(f"✨ Ваші скіли: {skills}")
            print(" ")
            sleep(0.5)
            print("🏃 Ви пішли назад додому!")
            print(" ")
            sleep(0.5)
            return player_level, player_xp, need_xp, skills, weapon
        elif player_class == "Лучник":
            print("🏹️ Ви зачаровуєте свій лук!")
            print(" ")
            sleep(0.5)
            random_sk = choice(random_skills_archer)
            if not random_sk in skills:
                print(f"✨ Зачар подарував вам новий скіл, {player_name}")
                print(" ")
                sleep(0.5)
            if not "Зачарований" in weapon:
                weapon = "Зачарований " + weapon.lower()
            print(f"🏹 Ваш лук: {weapon}")
            if not random_sk in skills:
                print(f"✨ Розблокований скіл: {random_sk}!")
                skills.append(random_sk)
            print(f"✨ Ваші скіли: {skills}")
            print(" ")
            sleep(0.5)
            print("🏃 Ви пішли назад додому!")
            print(" ")
            sleep(0.5)
            return player_level, player_xp, need_xp, skills, weapon
        elif player_class == "Маг":
            print("🪄 Ви зачаровуєте свій посох!")
            print(" ")
            sleep(0.5)
            random_sk = choice(random_skills_mage)
            if not random_sk in skills:
                print(f"✨ Зачар подарував вам новий скіл, {player_name}")
                print(" ")
                sleep(0.5)
            if not "Зачарований" in weapon:
                weapon = "Зачарований " + weapon.lower()
            print(f"🪄  Ваш посох: {weapon}")
            if not random_sk in skills:
                print(f"✨ Розблокований скіл: {random_sk}!")
                skills.append(random_sk)
            print(f"✨ Ваші скіли: {skills}")
            print(" ")
            sleep(0.5)
            print("🏃 Ви пішли назад додому!")
            print(" ")
            sleep(0.5)
            return player_level, player_xp, need_xp, skills, weapon

def gladiator_arena(player_level, player_class, player_name, player_xp, weapon, skills, need_xp):
    global random_skills_knight, random_skills_archer, random_skills_mage
        
    gladiators = randint(100, 250)
    
    if player_level < 50:
        print(f"⛵ Ви, {player_name}, дуже довго пливли через океан на своєму маленькому човнику...")
        print(" ")
        sleep(0.5)
        print("⛵ Навіть через шторми і безсонні ночі ви змогли дістатися до острова 'Дресс Роуз'!")
        print(" ")
        sleep(0.5)
        print("🗾 Саме на цьому острові розташований коллізей 'Кариди' в якому проходять гладіаторські бої серед всіх океанів, островів!")
        print(" ")
        sleep(0.5)
        print("✍ Ви спробували записатися як участник...")
        print(" ")
        sleep(0.5)
        print(f"👎 Все це було марно... Які ж ви були розгнівані, {player_name}! Адже пливли туди так довго!")
        print(" ")
        sleep(0.5)
        print(f"👎️ Вам сказали: 'Мінімальний левел для нашого коллізею - це 50, а у вас всього {player_level}!'")
        print(" ")
        sleep(0.5)
        return player_level, player_xp, need_xp, skills, weapon
    elif player_level >= 50:
        print(f"⛵ Ви, {player_name}, дуже довго пливли через океан на своєму маленькому човнику...")
        print(" ")
        sleep(0.5)
        print("⛵ Навіть через шторми і безсонні ночі ви змогли дістатися до острова 'Дресс Роуз'!")
        print(" ")
        sleep(0.5)
        print("🗾 Саме на цьому острові розташований коллізей 'Кариди' в якому проходять гладіаторські бої серед всіх океанів, островів!")
        print(" ")
        sleep(0.5)
        print("✍ Ви спробували записатися як участник...")
        print(" ")
        sleep(0.5)
        print(f"👍 Вам сказали: '{player_name}, ох... Не часто зустрінеш такий левел, звичайно ж ви прийняті!'")
        print(" ")
        sleep(0.5)
        print(f"✨ Він: 'Почекайте, {player_name}, не йдіть так швидко до коллізею!  Наш приз - гігантське зілля xp, воно дає 10 левлів!'")
        print(" ")
        sleep(0.5)
        print(f"✨ На арені коллізею було аж {gladiators} гладіаторів!")
        print(" ")
        sleep(0.5)
        print("✨ Кількість - це не головне і ви це знаєте! Ви спробували і у вас вийшло, ви їх усіх перемогли!")
        print(" ")
        sleep(0.5)
        print("✨ Приз ваш! Ви отримали приз!")
        print(" ")
        sleep(0.5)
        claimed_lvl = 10
        left_xp = need_xp - player_xp
        if left_xp < 0:
            left_xp = 0
        print(f"➕ Ви отримали 10 левлів!")
        sleep(0.1)
        print(f"✨ Ваш левел {player_level}!")
        sleep(0.1)
        print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
        print(" ")
        sleep(0.1)
        print("➕ Ваш левел збільшено!")
        print(" ")
        sleep(0.1)
        player_level += 10
        player_xp = 0
        need_xp = 25 + (player_level * 10)
        left_xp = need_xp - player_xp
        print(f"✨ Вам потрібно - {need_xp} xp, щоб збільшити левел!")
        print(" ")
        sleep(0.5)
        print("🏃 Ви вийшли з підземелля!")
        print(" ")
        sleep(0.5)
        return player_level, player_xp, need_xp, skills, weapon
 
def sleep_day():
    print("🛏️ Ви вирішили просто відпочити!")
    print(" ")
    sleep(0.5)
    print("🌙 Ви заснули та ніч була спокійна!")
    print(" ")
    sleep(0.5)
    
def show_stats(player_level, player_class, player_name, player_xp, weapon, skills):
    print("✨ Ось ваша статистика:")
    print(" ")
    sleep(0.5)
    print(f"👨 Ваш нік: {player_name}")
    sleep(0.1)
    print(f"⚔️🏹🪄 Ваш класс: {player_class}!")
    print(" ")
    sleep(0.5)
    print(f"⚔️🏹🪄 Ваша зброя: {weapon}")
    sleep(0.1)
    ryad = "✨ Ваші скіли: "
    for sk in skills:
        ryad = ryad + sk + ", "
    ryad = ryad[0: -2: 1]
    print(ryad)
    print(" ")
    sleep(0.5)
    print(f"✨ Ваш левел: {player_level}")
    print(" ")
    sleep(0.5)
    
print("Світ '✨Magical adventures✨' чекає вас!")
print(" ")
sleep(0.5)

while True:
    print("🎮 Оберіть дію: ")
    sleep(0.1)
    print("1️⃣  1. Піти у підземелля")
    sleep(0.1)
    print("2️⃣  2. Битися з слабкими монстрами на землі")
    sleep(0.1)
    print("3️⃣  3. Подорожувати та шукати ресурси")
    sleep(0.1)
    print("4️⃣  ️4. Піти на арену гладіаторів та битися з гладіаторами за приз (Рекомандовий лвл: 50+)")
    sleep(0.1)
    print("5️⃣  5. Спати в цей ігровий день")
    sleep(0.1)
    print("6️⃣  6. Подивитися статиску")
    sleep(0.1)
    print("7️⃣  7. Завершити гру")
    print(" ")
    sleep(0.5)
    choice_user = input("Оберайте номер: ")
    if choice_user.isdigit():
        choice_user = int(choice_user)
        if choice_user == 1:
            player_level, player_xp, need_xp, skills, weapon = go_to_dungeon(player_level, player_class, player_name, player_xp, weapon, skills, need_xp)
        elif choice_user == 2:
            player_level, player_xp, need_xp, skills, weapon = fight_ground_monsters(player_level, player_class, player_name, player_xp, weapon, skills, need_xp)
        elif choice_user == 3:
            player_level, player_xp, need_xp, skills, weapon = travel_for_resources(player_level, player_class, player_name, player_xp, weapon, skills, need_xp)
        elif choice_user == 4:
            player_level, player_xp, need_xp, skills, weapon = gladiator_arena(player_level, player_class, player_name, player_xp, weapon, skills, need_xp)
        elif choice_user == 5:
            sleep_day()
        elif choice_user == 6:
            show_stats(player_level, player_class, player_name, player_xp, weapon, skills)
        elif choice_user == 7:
            print("👍 Дякуємо вам за те, що грали!")
            print(" ")
            sleep(0.5)
            print("🎮 Ось ваша кінцева статистика:")
            print(f"👨 Нік: {player_name}")
            print(f"⚔️🏹🪄 Класс: {player_class}")
            print(f"✨ Левел: {player_level}")
            print(" ")
            sleep(0.5)
            end_time = time()
            time_played = end_time - start_time
            print(f"⌛ Ви грали: {time_played}!")
            print(" ")
            sleep(0.5)
            print(f"👋 До побачення, {player_name}!")
            print(" ")
            break
        else:
            print("❗ Не правильний номер дії!")
            print(" ")
            sleep(0.5)
            continue
    elif choice_user == "":
        print("❗ Номер дії не може бути порожнім!")
        print(" ")
        sleep(0.5)
        continue
    else:
        print("❗ Номер дії не може бути буквами або символами!")
        print(" ")
        sleep(0.5)
        continue
    