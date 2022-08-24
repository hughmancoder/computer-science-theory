#include <iostream>
# include <vector>
using namespace std;

class UnionFind {
public:
    UnionFind(int sz) : root(sz) {
        for (int i = 0; i < sz; i++) {
            root[i] = i;
        }
    }

    int find(int x) {
        if (x == root[x]) {
            return x;
        }

        int parent = find(root[x]);
        cout << x << " set to " << parent << endl;
        return root[x] = parent;

        // return root[x] = find(root[x]);
    }

    void unionSet(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            root[rootY] = rootX;
        }
    }

    bool connected(int x, int y) {
        return find(x) == find(y);
    }

    void showRoots() {
        for (auto r : root) {
            cout << r << " ";
        }
        cout << endl;
    }

private:
    vector<int> root;
};

int main() {
    cout << boolalpha;
    UnionFind uf(10);
    // 1-2-5-6-7 3-8-9 4
    uf.unionSet(1, 2);
    uf.unionSet(2, 5);
    uf.unionSet(5, 6);
    uf.unionSet(6, 7);
    uf.showRoots();

    uf.unionSet(3, 8);
    uf.unionSet(8, 9);
    uf.showRoots();

    cout << uf.connected(1, 5) << endl;  // true
    cout << uf.connected(5, 7) << endl;  // true
    cout << uf.connected(4, 9) << endl;  // false
    // 1-2-5-6-7 3-8-9-4
    uf.showRoots();

    // 1-2-5-6-7-3-8-9-4
    uf.unionSet(3, 1);
    cout << uf.connected(8, 1) << endl;  // true
    cout << uf.connected(9, 5) << endl;  // true
    uf.showRoots();

    return 0;
}