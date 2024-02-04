#include <iostream>
#include <sstream>
#include <string>
using namespace std;

// number of buckets
const int TABLE_SIZE = 26;
struct Node {
  bool used;
  string value;
};
// hash table with linear probing
class HashTable {
public:
  Node arr[TABLE_SIZE];
  int curr_size;
  HashTable() {
    for (int i = 0; i < TABLE_SIZE; i++) {
      arr[i].used = false;
    }
  }

  int hash(string str) {
    int str_end = str[str.size() - 1] - 97;
    int hash = str_end % TABLE_SIZE;
    return hash;
  }

  // finds next available slot
  Node *search(string value) {
    int hash_index = hash(value);
    for (int i = 0; i < TABLE_SIZE; i++) {
      Node *node = &arr[hash_index];
      // entry is empty
      if (!node->used) {
        return node;
      }
      if (node->value == value) {
        return node;
      }
      hash_index += 1;
      hash_index %= TABLE_SIZE;
    }
    // hash table is full
    return nullptr;
  }

  void insert(string value) {
    Node *node = search(value);
    if (node != nullptr and !node->used) {
      node->used = true;
      node->value = value;
    }
  }

  void Delete(string value) {
    Node *node = contains(value);
    if (node != nullptr and node->used) {
      node->used = false;
    }
  }

  // suplementary methods
  bool isEmpty() { return curr_size == 0; }

  // return node if node contains value otherwise we return nullptr
  Node *contains(string value) {
    int hash_index = hash(value);
    for (int i = 0; i < TABLE_SIZE; i++) {
      Node *node = &arr[hash_index];
      if (node->value == value) {
        return node;
      }
      hash_index += 1;
      hash_index %= TABLE_SIZE;
    }
    return nullptr;
  }

  void print() {
    for (int i = 0; i < TABLE_SIZE; i++) {
      if (arr[i].used) {
        cout << arr[i].value << " ";
      }
    }
  }
};

int main() {
  HashTable table = HashTable();
  string input;
  getline(cin, input);
  stringstream ss(input);
  string word;
  while (ss >> word) {
    if (word.size() < 2)
      continue;
    char operation = word[0];
    if (operation == 'A')
      table.insert(word.substr(1));
    else if (operation == 'D')
      table.Delete(word.substr(1));
  }
  table.print();
}