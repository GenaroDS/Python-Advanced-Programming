# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    total1 = (person1["result1"] + person1["result2"] + person1["result3"]) / 3
    total2 = (person2["result1"] + person2["result2"] + person2["result3"]) / 3
    total3 = (person3["result1"] + person3["result2"] + person3["result3"]) / 3
    data = min(total1, total2, total3)
    if data == total1:
        return person1
    elif data == total2:
        return person2
    elif data == total3:
        return person3 

if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
    print(smallest_average(person1, person2, person3))
#Name correct