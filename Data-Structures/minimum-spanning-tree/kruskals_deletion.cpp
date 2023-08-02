#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <iostream>
#include <set>
using namespace std;

// converts string input into adjacency matrix
vector<string> getGraph(std::string str)
{
    vector<string> ret;
    stringstream ss(str);
    while (ss.good())
    {
        string substr;
        getline(ss, substr, ',');
        ret.push_back(substr);
    }
    return ret;
}

// union by rank with path compression for efficiency
class UnionFind
{
    int *parent;
    int *rank;
    int size;

public:
    // constructor
    UnionFind(int size)
    {
        this->size = size;
        parent = new int[size];
        rank = new int[size];

        for (int i = 0; i < size; i++)
        {
            // let node number denote root node of union set
            parent[i] = -1;
            rank[i] = -1;
        }
    }

    int find(int i)
    {
        if (parent[i] == -1)
        {
            return i;
        }
        // path compression: recursively update the nodes connecting to parent to contain parent root
        return parent[i] = find(parent[i]);
    }

    // union with path compression: link node b to node a
    void Union(int a, int b)
    {
        int parent_a = find(a);
        int parent_b = find(b);
        // if the parents are different we combine
        if (parent_a != parent_b)
        {
            // rank denots the height of the tree, so we want to connect the shorter struct to flatten it out
            if (rank[parent_a] < rank[parent_b])
            {
                parent[parent_a] = parent_b;
                // update the height (rank) of parent_b
                rank[parent_b] += rank[parent_a];
            }
            else
            {
                parent[parent_b] = parent_a;
                // update the height (rank) of parent_b
                rank[parent_a] += rank[parent_b];
            }
        }
    }

    bool isConnected(int a, int b)
    {
        return find(a) == find(b);
    }

    void showParents()
    {
        for (int i = 0; i < size; i++)
        {
            cout << parent[i] << " ";
        }
        cout << endl;
    }
};

int getWeight(char letter)
{
    // ascii letter to weight conversions
    int weight = letter;
    // capital letter
    if (weight >= 65 and weight <= 90)
    {
        return weight - 65;
    }
    // lowercase
    return weight - 71;
}

class Graph
{
    int N; // number of cities

public:
    priority_queue<vector<int>> destroy;
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> build;
    Graph(int size) : N(size){};
    int KruskalMST()
    {
        // union find object
        UnionFind UF(N);
        int min_cost = 0;
        while (destroy.size())
        {
            vector<int> edge = destroy.top();
            int w = edge[0];
            int i = edge[1];
            int j = edge[2];
            // delete the node if cycle if found
            if (UF.find(i) == UF.find(j))
            {
                min_cost += w;
            }
            else
            {
                UF.Union(i, j);
            }
            destroy.pop();
        }
        // build roads
        while (build.size())
        {
            vector<int> edge = build.top();
            int w = edge[0];
            int i = edge[1];
            int j = edge[2];

            if (!UF.isConnected(i, j))
            {
                min_cost += w;
                UF.Union(i, j);
            }
            build.pop();
        }
        return min_cost;
    }
};

// supplementary
void printGraph(vector<string> graph)
{
    int n = graph[0].size();
    for (int i = 0; i < n; i++)
    {
        cout << endl;
        for (int j = 0; j < n; j++)
        {
            cout << graph[i][j] << " ";
        }
    }
    cout << endl;
}

int main(int argc, char *argv[])
{
    string input;
    getline(cin, input);
    stringstream sstr(input);
    vector<string> v;
    while (sstr.good())
    {
        std::string substr;
        getline(sstr, substr, ' ');
        v.push_back(substr);
    }

    vector<string> graph = getGraph(v[0]);
    vector<string> build = getGraph(v[1]);
    vector<string> destroy = getGraph(v[2]);
    int num_cities = graph[0].size();
    Graph g(num_cities);
    for (int i = 0; i < num_cities; i++)
    {
        for (int j = i + 1; j < num_cities; j++)
        {

            if (i == j)
                continue;
            int destroy_cost = getWeight(destroy[i][j]);
            int build_cost = getWeight(build[i][j]);
            // if connection already present
            if (graph[i][j] == '1')
            {
                g.destroy.push({destroy_cost, i, j});
            }
            else
            {
                g.build.push({build_cost, i, j});
            }
        }
    }
    cout << g.KruskalMST() << " " << endl;
    return 0;
};
