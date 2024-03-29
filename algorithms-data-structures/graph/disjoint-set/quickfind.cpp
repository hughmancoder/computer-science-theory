#include <iostream>
#include <vector>
using namespace std;

class unionFind {
private:
  vector<int> roots;

public:
  unionFind(int size) : roots(size) {
    for (int i = 0; i < size; i++) {
      roots[i] = i; // roots initially point to themselves
    }
  }

  int find(int x) { return roots[x]; }

  void unionSet(int x, int y) {
    int root_x = find(x);
    int root_y = find(y);
    for (int i = 0; i < roots.size(); i++) {
      if (roots[i] == root_y) {
        roots[i] = root_x;
      }
    }
  }

  bool connected(int x, int y) { return find(x) == find(y); }
};

int main() {

  // sets the boolalpha format flag for the str stream for 'true' or 'false'
  // rather than 1 or 0
  cout << boolalpha;
  unionFind uf(10);
  // 1-2-5-6-7 3-8-9 4
  uf.unionSet(1, 2);
  uf.unionSet(2, 5);
  uf.unionSet(5, 6);
  uf.unionSet(6, 7);
  uf.unionSet(3, 8);
  uf.unionSet(8, 9);
  cout << uf.connected(1, 5) << endl; // true
  cout << uf.connected(5, 7) << endl; // true
  cout << uf.connected(4, 9) << endl; // false

  uf.unionSet(9, 4); // 1-2-5-6-7 3-8-9-4
  cout << uf.connected(4, 9) << endl;

  uf.unionSet(3, 1); // 1-2-5-6-7-3-8-9-4
  cout << uf.connected(2, 9);

  return 0;
}