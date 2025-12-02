import random
import time

class Character:
    """플레이어 캐릭터 클래스"""
    def __init__(self, name):
        self.name = name
        self.max_hp = 100
        self.hp = self.max_hp
        self.attack_power = 20
        self.exp = 0
        self.level = 1
        self.next_level_exp = 100

    def attack(self, target):
        """대상을 공격하여 데미지를 입힘"""
        damage = random.randint(self.attack_power - 2, self.attack_power + 2)
        print(f"\n⚔️ {self.name}의 공격! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        target.take_damage(damage)

    def take_damage(self, damage):
        """데미지를 입음"""
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"🩸 {self.name}의 체력: {self.hp}/{self.max_hp}")

    def gain_exp(self, amount):
        """경험치 획득 및 레벨업 처리"""
        print(f"✨ {amount} 경험치를 획득했습니다.")
        self.exp += amount
        if self.exp >= self.next_level_exp:
            self.level_up()

    def level_up(self):
        """레벨업 처리"""
        self.level += 1
        self.exp -= self.next_level_exp
        self.next_level_exp = int(self.next_level_exp * 1.2)
        self.max_hp += 20
        self.hp = self.max_hp # 레벨업 시 체력 회복
        self.attack_power += 5
        print(f"\n🎉 축하합니다! 레벨이 {self.level}로 올랐습니다!")
        print(f"💪 최대 체력이 {self.max_hp}로 증가하고, 공격력이 {self.attack_power}로 증가했습니다.\n")

    def show_status(self):
        """현재 상태 출력"""
        print(f"\n[{self.name}의 상태]")
        print(f"Lv. {self.level}")
        print(f"HP: {self.hp} / {self.max_hp}")
        print(f"공격력: {self.attack_power}")
        print(f"경험치: {self.exp} / {self.next_level_exp}")
        print("--------------------------")

class Monster:
    """몬스터 클래스"""
    def __init__(self, name, hp, attack_power, exp_reward):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack_power = attack_power
        self.exp_reward = exp_reward

    def attack(self, target):
        """대상을 공격"""
        damage = random.randint(self.attack_power - 1, self.attack_power + 1)
        print(f"\n👾 {self.name}의 공격! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        target.take_damage(damage)

    def take_damage(self, damage):
        """데미지를 입음"""
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"👾 {self.name}의 체력: {self.hp}/{self.max_hp}")

def get_random_monster():
    """랜덤 몬스터 생성"""
    monsters = [
        Monster("슬라임", 30, 5, 20),
        Monster("고블린", 50, 8, 40),
        Monster("오크", 80, 12, 70),
        Monster("드래곤", 200, 25, 300)
    ]
    # 난이도 조절을 위해 확률적으로 등장하게 할 수도 있지만, 지금은 단순 랜덤
    return random.choice(monsters)

def battle(player, monster):
    """전투 로직"""
    print(f"\n❗ 야생의 {monster.name}이(가) 나타났습니다!")
    
    while monster.hp > 0 and player.hp > 0:
        print(f"\n--- {player.name}의 턴 ---")
        print(f"1. 공격하기")
        print(f"2. 도망가기")
        choice = input("행동을 선택하세요: ")

        if choice == "1":
            player.attack(monster)
            if monster.hp > 0:
                time.sleep(0.5) # 전투 속도 조절
                monster.attack(player)
        elif choice == "2":
            print("💨 무사히 도망쳤습니다.")
            return
        else:
            print("잘못된 입력입니다.")
            continue

        if player.hp == 0:
            print(f"\n💀 {player.name}은(는) 쓰러졌습니다... 게임 오버.")
            return
        
        if monster.hp == 0:
            print(f"\n🏆 {monster.name}을(를) 물리쳤습니다!")
            player.gain_exp(monster.exp_reward)

def main():
    print("=====================================")
    print("   텍스트 RPG 게임에 오신 것을 환영합니다!   ")
    print("=====================================")
    name = input("플레이어의 이름을 입력하세요: ")
    player = Character(name)

    while True:
        print("\n==================")
        print("1. 🏕️ 모험 떠나기")
        print("2. 📊 상태 확인")
        print("3. 🚪 종료")
        print("==================")
        choice = input("무엇을 하시겠습니까? ")

        if choice == "1":
            monster = get_random_monster()
            battle(player, monster)
            if player.hp == 0:
                break
        elif choice == "2":
            player.show_status()
        elif choice == "3":
            print("게임을 종료합니다. 즐거운 모험이었습니다!")
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()
