# Program for Restaurant Table Booking System
import time
start = time.time()

tables = [
    [1, 0],
    [2, 0],
    [3, 0],
    [4, 0],
    [5, 0]
]

while True:
    # Display menu
    print('Restaurant Table Booking System')
    print('1. Book Table')
    print('2. View Table Bookings')
    print('3. Cancel Booking')
    print('Enter your choice (1-3):')
    choice = int(input())

    # Book a table
    if choice == 1:
        flag = 0
        for table in tables:
            if table[1] == 0:
                print('Table %d is available. Do you want to book it? (y/n)' % table[0])
                if input().lower() == 'y':
                    table[1] = 1
                    print('Table %d booked successfully.' % table[0])
                    flag = 1
                    break
        if flag == 0:
            print('Sorry! All tables are booked.')

    # View table bookings
    elif choice == 2:
        print('Table Booking Status')
        print('Table No.\tBooked')
        for table in tables:
            if table[1] == 1:
                print('%d\t\tYes' % table[0])
            else:
                print('%d\t\tNo' % table[0])

    # Cancel booking
    elif choice == 3:
        print('Please enter the table number to cancel booking:')
        table_no = int(input())
        flag = 0
        for table in tables:
            if table[0] == table_no:
                if table[1] == 1:
                    table[1] = 0
                    print('Table %d booking cancelled successfully.' % table_no)
                    flag = 1
                    break
        if flag == 0:
            print('Table %d already available.' % table_no)

    # Invalid choice
    else:
        print('Invalid Choice.')
        
end = time.time()
print("The time of execution of above program is :",(end-start), "sec")