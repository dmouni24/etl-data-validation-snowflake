import csv

with open('data-mocks/mock_input_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['order_id', 'customer_id', 'order_date', 'total_amount'])
    writer.writerow([1, 101, '2023-01-01', 100.00])
    writer.writerow([2, 102, '2023-01-02', 200.00])
    writer.writerow([3, 103, '2023-01-03', None])
