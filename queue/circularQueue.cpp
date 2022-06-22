#include <array>
#include <iostream>
using namespace std;

class circularQueue
{
private:
    int size, rear, front, *arr;

public:
    circularQueue(int s) : size(s)
    {
        front = rear = -1;
        arr = new int[s]; // make an array of size s
    };

    bool isFull()
    {
        return ((rear == size - 1 && front == 0) || (rear == front - 1));
    }

    bool isEmpty()
    {
        return front == -1;
    }

    void enqueue(int val)
    {
        if (isFull())
        {
            cout << "queue is full" << endl;
            return;
        }
        else if (front == -1)
        {
            front = rear = 0;
            arr[rear] = val; // insert into rear
        }
        else if (rear == size - 1 && front != 0)
        {
            rear = 0; // go to start if end is full
            arr[rear] = val;
        }
        else
        {
            rear++;
            arr[rear] = val;
        }
    }

    int top()
    {
        if(isEmpty())
        {
            return INT_MIN;
        }
        return arr[front];
    }

    int dequeue()
    {
        if (isEmpty())
        {
            cout << "queue is empty" << endl;
            return INT_MIN;
        }
        int data = arr[front];
        if (front == rear)
        {
            front = rear = -1; // mark queue as empty
        }
        else if (front == size - 1)
        {
            front = 0; // increment front to start
        }
        else
        {
            front++;
        }
        return data;
    }
};

int main()
{
    circularQueue q(5); // creating a queue of size 10;

    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    q.enqueue(4);
    q.enqueue(5);
    q.enqueue(6); // overflow

    cout << q.top() << endl;
    q.dequeue();
    cout << q.top() << endl;
    q.dequeue();
    cout << q.top() << endl;
    cout << q.top() << endl;
    return 0;
}