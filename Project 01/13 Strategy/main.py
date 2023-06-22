from strategy import Strategy, strategy_one, strategy_two

def main():
    s1 = Strategy()
    s1.execute()

    s2 = Strategy(strategy_one)
    s2.execute()

    s3 = Strategy(strategy_two)
    s3.execute()

if __name__ == "__main__":
    main()