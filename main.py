import random


def guess_number():
    # 电脑随机生成 1-100 的整数
    answer = random.randint(1, 100)
    count = 0  # 记录猜测次数

    print("=" * 40)
    print("欢迎来到猜数字小游戏！")
    print("我已经想好了一个 1-100 之间的整数，快来猜猜看吧~")
    print("=" * 40)

    while True:
        user_input = input("请输入你猜的数字：").strip()

        # 输入合法性检查
        if not user_input.isdigit():
            print("⚠️  输入无效，请输入一个正整数！\n")
            continue

        guess = int(user_input)

        if guess < 1 or guess > 100:
            print("⚠️  数字超出范围，请输入 1-100 之间的整数！\n")
            continue

        count += 1  # 有效猜测才计数

        if guess > answer:
            print("📉 大了，再试试小一点的数字~\n")
        elif guess < answer:
            print("📈 小了，再试试大一点的数字~\n")
        else:
            print(f"\n🎉 恭喜你猜中了！答案就是 {answer}")
            print(f"你一共猜了 {count} 次。")

            # 简单评价
            if count == 1:
                print("太神了！一次就中！")
            elif count <= 5:
                print("非常棒，你的直觉很准！")
            elif count <= 10:
                print("表现不错，继续加油！")
            else:
                print("终于猜中啦，下次可以试试二分法哦~")
            break


def main():
    while True:
        guess_number()

        # 单独用一个循环处理 "是否再来一局" 的输入
        while True:
            choice = input("\n再玩一局请输入 y，按 e 退出：").strip().lower()
            if choice in ("y", "e"):
                break
            print("输入无效，请重新选择。")

        if choice == "e":
            print("已退出，再见！")
            break


if __name__ == "__main__":
    main()