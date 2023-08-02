#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *head;
    Node *end; // for append method
    Node *next;
    Node *prev;

    Node() : end(NULL), head(NULL){};

    void push(int data) // prepend
    {
        Node *new_node = new Node();
        new_node->data = data;
        new_node->next = head;
        new_node->prev = NULL;

        if (head != NULL)
        {
            head->prev = new_node;
        }
        else // head == NULL
        {
            end = new_node;
        }
        head = new_node;
    }

    void insertAfter(Node *prev_node, int data)
    {
        if (prev_node == NULL)
            return;

        Node *next = new Node();
        next->data = data;
        next->next = prev_node->next;
        prev_node->next = next;
        next->prev = prev_node;

        if (next->next != NULL)
        {
            next->next->prev = next;
        }
        else if (next->next == NULL)
        {
            end = next; // update the last node
        }
    }

    void append(int data)
    {
        Node *next = new Node();
        next->next = NULL;
        next->data = data;

        if(head == NULL)
        {
            head = next; // update our head
            return;
        }
        Node *temp = head;
        while(temp->next)
        {
            temp = temp->next;
        }
        temp->next = next;
        next->prev = temp;
    }

    void printList()
    {
        Node *start = head;
        while (start->next)
        {
            cout << start->data << " ";
            start = start->next;
        }
        cout << endl;
    }
};

int main()
{
    Node *head = new Node();
    head->append(1);
    head->append(2);
    head->append(3);
    head->append(4);

    head->printList();

    // trying push methods
    head->push(0);
    head->push(1);
    head->push(2);
    head->printList();
    return 0;
}