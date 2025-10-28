import random  #библиотека для рандома

def roll():
    #Сумма рандомных чисел двух кубиков
    return random.randint(1, 6) + random.randint(1, 6)


def play_round(balance, bet):
    # Проверка ставки
    if bet <= 0 or bet > balance:
        print(f"Bet {bet} bet is not avaliable with this balance {balance}.")
        return balance

    you = roll()
    cpu = roll()

    if you > cpu:
        balance += bet
        print(f"you={you}, cpu={cpu} → +{bet}, balance={balance}")
    elif you < cpu:
        balance -= bet
        print(f"you={you}, cpu={cpu} → -{bet}, balance={balance}")
    else:
        print(f"you={you}, cpu={cpu} → even, balance={balance}")

    return balance

def run_game(start_balance, rounds, bet_strategy):
    balance = start_balance

    for r in range(1, rounds + 1):
        bet = bet_strategy(balance, r)
        if bet <= 0 or bet > balance:
            print(f"R{r}: Bet {bet} is not avaliable. The game is over!.")
            break

        print(f"R{r}:", end=" ")
        balance = play_round(balance, bet)

        if balance <= 0:
            print(f"R{r}: You lost all your balance. The game is over!")
            break

    print(f"Final balance: {balance}")

def fixed_bet_strategy(balance, round_idx):
    # Простая стратегия — всегда ставим 100
    return 100

# === Запуск ===
start_balance = 1000
rounds = 10
run_game(start_balance, rounds, fixed_bet_strategy)