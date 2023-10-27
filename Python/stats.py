import csv
from datetime import date
from matplotlib import pyplot as plt

def updateData():
    today = date.today()
    dateToday = today.strftime("%Y-%m-%d")
    x = (input("No of questions attempted: ").strip())
    data = []
    with open("records.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    found = False
    for i, row in enumerate(data):
        if row[0] == dateToday:
            data[i][1] = x
            found = True
            break
    if not found:
        data.append([dateToday, x])
    with open("records.csv", mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    return data

def plot(data):
    dates = [row[0] for row in data]
    x= [int(row[1]) for row in data]
    total = sum(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(dates, x, marker='o', linestyle='-', color='b', label='Questions Attempted')
    plt.title('Questions Attempted Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Questions Attempted')
    plt.xticks(rotation=45)
    plt.legend([f'Total: {total}'], loc='upper left')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    data = updateData()
    plot(data)
