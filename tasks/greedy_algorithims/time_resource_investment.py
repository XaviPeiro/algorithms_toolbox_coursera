map = {
    "total": 24*12,
    "things": {
        "sport": 6*3,
        "sleep": 7*7,
        "money": 8*5,
        "eating": 2*7,
        "cooking": 10,
        "higiene+groceries+cooking": 21,
        "rest": 1,
        "context_swap": 7*0.5*7,
        "study": 7*2,
        "own_projects": 7*2,
    }
}

total = 24*12
sport = 6*3
sleep = 7*7

if __name__ == "__main__":

    t = map["total"]
    acc_rel = 0
    acc_t = 0
    for k,v in map["things"].items():
        rel = round((v / t) * 100, 2)
        acc_rel += rel
        acc_t += v
        print(k)
        print(f"total: {v} \n rel:{rel}")
        print(f"acc_rel:{acc_rel} - t_acc:{acc_t}")
        print(f"--------------")

